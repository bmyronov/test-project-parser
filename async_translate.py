import asyncio
from typing import Any

import aiofiles
import aiofiles.os

from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from deep_translator.exceptions import NotValidPayload

import translators as ts


async def translate(tag: Any) -> None:
    try:
        if tag.string != None:
            try:
                old_tag = tag.string
                translated = await asyncio.to_thread(
                    GoogleTranslator(source="auto", target="hi").translate, tag.string
                )

                if old_tag.string != "":
                    tag.string = translated

                print(tag)
                print(f"Original: {old_tag} \t" f"Translated: {tag.string}\n")

            except TypeError:
                pass
            except NotValidPayload:
                pass

    except AttributeError:
        pass

    await asyncio.sleep(2.5)


async def check_favicon(favicon: Any) -> None:
    try:
        if favicon["href"] == "/favicon-32x32.png":
            favicon["href"] == "./favicon-32x32.png"
    except KeyError:
        pass

    try:
        if favicon["href"] == "/favicon-16x16.png":
            favicon["href"] == "./favicon-16x16.png"
    except KeyError:
        pass


async def translate_index_page() -> None:
    async with aiofiles.open("./index.html") as file:
        page = await file.read()
    soup = BeautifulSoup(page, "lxml")
    favicons = soup.find_all("link")
    await asyncio.gather(*[check_favicon(favicon) for favicon in favicons])

    title = soup.find("title")
    await translate(title)

    try:
        span_tags = soup.find_all("span")
        await asyncio.gather(*[translate(span_tag) for span_tag in span_tags])

        button_tags = soup.find_all("button")
        await asyncio.gather(*[translate(button_tag) for button_tag in button_tags])

        a_tags = soup.find_all("a")
        await asyncio.gather(*[translate(a_tag) for a_tag in a_tags])

        p_tags = soup.find_all("p")
        await asyncio.gather(*[translate(p_tag) for p_tag in p_tags])

        h1_tags = soup.find_all("h1")
        await asyncio.gather(*[translate(h1_tag) for h1_tag in h1_tags])

        h2_tags = soup.find_all("h2")
        await asyncio.gather(*[translate(h2_tag) for h2_tag in h2_tags])

        h3_tags = soup.find_all("h2")
        await asyncio.gather(*[translate(h3_tag) for h3_tag in h3_tags])

        h4_tags = soup.find_all("h4")
        await asyncio.gather(*[translate(h4_tag) for h4_tag in h4_tags])

        h5_tags = soup.find_all("h5")
        await asyncio.gather(*[translate(h5_tag) for h5_tag in h5_tags])

        strong_tags = soup.find_all("strong")
        await asyncio.gather(*[translate(strong_tag) for strong_tag in strong_tags])

        i_tags = soup.find_all("i")
        await asyncio.gather(*[translate(i_tag) for i_tag in i_tags])

        div_tags = soup.find_all("div")
        await asyncio.gather(*[translate(div_tag) for div_tag in div_tags])

        section_tags = soup.find_all("section")
        await asyncio.gather(*[translate(section_tag) for section_tag in section_tags])

    except TypeError:
        pass

    logo = soup.find(class_="block medium-up-margin-right-large cmpt-nav-logo")
    logo["span"] = "Class Central"

    path_to_file = "./async_translated/index.html"
    async with aiofiles.open(path_to_file, "w", encoding="utf-8") as file:
        await file.write(str(soup))


async def translate_web_pages(filename: str) -> None:
    pass_list = ["index.js", "favicon-16x16.png", "favicon-32x32.png"]
    if filename in pass_list:
        return

    page_path = "./classcentral/"
    async with aiofiles.open(str(page_path + filename)) as file:
        print("\n\n", page_path + filename, "\n")
        page = await file.read()

    soup = BeautifulSoup(page, "lxml")

    favicons = soup.find_all("link")
    await asyncio.gather(*[check_favicon(favicon) for favicon in favicons])

    title = soup.find("title")
    await translate(title)

    try:
        span_tags = soup.find_all("span")
        await asyncio.gather(*[translate(span_tag) for span_tag in span_tags])

        button_tags = soup.find_all("button")
        await asyncio.gather(*[translate(button_tag) for button_tag in button_tags])

        a_tags = soup.find_all("a")
        await asyncio.gather(*[translate(a_tag) for a_tag in a_tags])

        p_tags = soup.find_all("p")
        await asyncio.gather(*[translate(p_tag) for p_tag in p_tags])

        h1_tags = soup.find_all("h1")
        await asyncio.gather(*[translate(h1_tag) for h1_tag in h1_tags])

        h2_tags = soup.find_all("h2")
        await asyncio.gather(*[translate(h2_tag) for h2_tag in h2_tags])

        h3_tags = soup.find_all("h2")
        await asyncio.gather(*[translate(h3_tag) for h3_tag in h3_tags])

        h4_tags = soup.find_all("h4")
        await asyncio.gather(*[translate(h4_tag) for h4_tag in h4_tags])

        h5_tags = soup.find_all("h5")
        await asyncio.gather(*[translate(h5_tag) for h5_tag in h5_tags])

        strong_tags = soup.find_all("strong")
        await asyncio.gather(*[translate(strong_tag) for strong_tag in strong_tags])

        i_tags = soup.find_all("i")
        await asyncio.gather(*[translate(i_tag) for i_tag in i_tags])

        div_tags = soup.find_all("div")
        await asyncio.gather(*[translate(div_tag) for div_tag in div_tags])

        section_tags = soup.find_all("section")
        await asyncio.gather(*[translate(section_tag) for section_tag in section_tags])

    except TypeError:
        pass

    translated_path = "./async_translated/classcentral/"
    async with aiofiles.open(
        str(translated_path + filename), "w", encoding="utf-8"
    ) as file:
        await file.write(str(soup))


async def main() -> None:
    # create a directory
    page_path = "./async_translated/"
    await aiofiles.os.makedirs(str(page_path), exist_ok=True)

    page_folder = "./async_translated/classcentral/"
    await aiofiles.os.makedirs(str(page_folder), exist_ok=True)

    # index_page = await translate_index_page()

    page_path = "./classcentral/"
    pages = await aiofiles.os.listdir(page_path)

    parsed_path = "./async_translated/classcentral/"
    parsed = await aiofiles.os.listdir(parsed_path)

    new_list = [f_name for f_name in pages if f_name not in parsed]

    # translate = await asyncio.gather(
    #    *[translate_web_pages(filename) for filename in pages]
    # )

    # translate = await translate_web_pages("about.html")

    # in case you keep getting banned
    for page in new_list:
        await translate_web_pages(page)


if __name__ == "__main__":
    asyncio.run(main())
