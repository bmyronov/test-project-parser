import asyncio
from typing import Any

import aiofiles
import aiofiles.os

from bs4 import BeautifulSoup


async def set_favicon(filename: str) -> None:
    pass_list = ["index.js", "favicon-16x16.png", "favicon-32x32.png"]
    if filename in pass_list:
        return

    page_path = "./async_translated/classcentral/"
    async with aiofiles.open(str(page_path + filename)) as file:
        print("\n\n", page_path + filename, "\n")
        page = await file.read()

    soup = BeautifulSoup(page, "lxml")
    link = soup.find_all("link")

    for favicon in link:
        if favicon == None or favicon == "":
            return
        try:
            if favicon["href"] == "/favicon-32x32.png":
                print(filename)
                print(favicon["href"])
                favicon["href"] = "./favicon-32x32.png"
                print(favicon, "\n")
        except KeyError:
            pass

        try:
            if favicon["href"] == "/favicon-16x16.png":
                print(filename)
                print(favicon["href"])
                favicon["href"] = "./favicon-16x16.png"
                print(favicon, "\n")
        except KeyError:
            pass

    async with aiofiles.open(str(page_path + filename), "w", encoding="utf-8") as file:
        await file.write(str(soup))


async def main() -> None:
    page_path = "./async_translated/classcentral/"
    pages = await aiofiles.os.listdir(page_path)

    await asyncio.gather(*[set_favicon(filename) for filename in pages])


if __name__ == "__main__":
    asyncio.run(main())
