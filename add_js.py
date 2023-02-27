import asyncio
from typing import Any

import aiofiles
import aiofiles.os

from bs4 import BeautifulSoup


async def add_js(filename: str) -> None:
    pass_list = ["index.js", "favicon-16x16.png", "favicon-32x32.png"]
    if filename in pass_list:
        return

    page_path = "./async_translated/classcentral/"
    async with aiofiles.open(str(page_path + filename)) as file:
        print("\n\n", page_path + filename, "\n")
        page = await file.read()

    soup = BeautifulSoup(page, "lxml")
    script_tag = soup.new_tag("script")
    script_tag["type"] = "text/javascript"
    script_tag["src"] = "./index.js"

    body = soup.find("body")
    body.append(script_tag)

    async with aiofiles.open(str(page_path + filename), "w", encoding="utf-8") as file:
        await file.write(str(soup))


async def main() -> None:
    page_path = "./async_translated/classcentral/"
    pages = await aiofiles.os.listdir(page_path)

    await asyncio.gather(*[add_js(filename) for filename in pages])


if __name__ == "__main__":
    asyncio.run(main())
