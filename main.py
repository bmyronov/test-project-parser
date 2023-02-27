import os, sys, re
import time
from typing import Any

import cloudscraper
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from googletrans import Translator


"""
def savePage(url, scraper, pagepath='page'):
    def savenRename(soup, pagefolder, session, url, tag, inner):
        if not os.path.exists(pagefolder): # create only once
            os.mkdir(pagefolder)
        for res in soup.findAll(tag):   # images, css, etc..
            if res.has_attr(inner): # check inner tag (file object) MUST exists  
                try:
                    filename, ext = os.path.splitext(os.path.basename(res[inner])) # get name and extension
                    filename = re.sub('\W+', '', filename) + ext # clean special chars from name
                    fileurl = urljoin(url, res.get(inner))
                    filepath = os.path.join(pagefolder, filename)
                    # rename html ref so can move html and folder of files anywhere
                    res[inner] = os.path.join(os.path.basename(pagefolder), filename)
                    if not os.path.isfile(filepath): # was not downloaded
                        with open(filepath, 'wb') as file:
                            filebin = session.get(fileurl)
                            file.write(filebin.content)
                except Exception as exc:
                    print(exc, file=sys.stderr)
    
    page = scraper.get(url).text
    soup = BeautifulSoup(page, "lxml")
    path, _ = os.path.splitext(pagepath)
    pagefolder = path+'_files' # page contents folder
    tags_inner = {'img': 'src', 'link': 'href', 'script': 'src'} # tag&inner tags to grab
    
    for tag, inner in tags_inner.items(): # saves resource files and rename refs
        savenRename(soup, pagefolder, scraper, url, tag, inner)
    with open(path+'.html', 'wb') as file: # saves modified html doc
        file.write(soup.prettify('utf-8'))
"""


def remove_href_whitespaces(soup: Any) -> None:
    # Remove whitespace at the end of href link in id="home-subjects"
    home_subjects = soup.find(id="home-subjects")
    home_subject_links = home_subjects.find_all("a")
    for link in home_subject_links:
        page_link = link["href"].split(" ")
        page_link.pop(1)
        link["href"] = page_link[0]


def remove_ads(soup: Any) -> None:
    li_tags = soup.find_all(
        class_="bg-white border-all border-gray-light padding-xsmall radius-small margin-bottom-small medium-up-padding-horz-large medium-up-padding-vert-medium relative"
    )

    for li in li_tags:
        li.decompose()


def scrape_images(soup: Any) -> None:
    images = soup.find_all("img")
    for image in images:
        try:
            image["src"] = image["data-src"]
            del image["data-src"]
        except KeyError as kerr:
            # print(kerr, image)
            pass


def scrape_links(soup: Any) -> None:
    a_tags = soup.find_all("a")
    for link in a_tags:
        if link["href"].startswith("/"):
            link["href"] = "https://www.classcentral.com" + link["href"]

    iframes = soup.find_all("iframe")
    for iframe in iframes:
        if iframe["src"].startswith("/"):
            iframe["src"] = "https://www.classcentral.com" + iframe["src"]


def save_to_html(soup: Any, filename: str) -> None:
    scrape_images(soup)
    scrape_links(soup)

    """
    images = soup.find_all("img")
    for image in images:
        try:
            image["src"] = image["data-src"]
            del image["data-src"]
        except KeyError as kerr:
            print(kerr, image)
    print(*images)

    a_tags = soup.find_all("a")

    for link in a_tags:
        if link["href"].startswith("/"):
            print(link["href"])
            link["href"] = "https://www.classcentral.com" + link["href"]
            print(link["href"])
            print("\n")
    """
    """
    if filename == "index":
        for link in a_tags:
            page_name = [page_name.split("/") for page_name in link]
            link["href"] = "./" + [filename[-1] for filename in page_name]
    """

    page_folder = "./classcentral/"
    if not os.path.exists(page_folder):  # create only once
        os.mkdir(page_folder)

    path_to_file = page_folder + filename + ".html"
    with open(path_to_file, "w", encoding="utf-8") as file:
        file.write(str(soup))

    time.sleep(5)


def parse_all_pages(soup: Any, scraper: Any) -> None:
    scrape_links(soup)
    a_tags = soup.find_all("a")
    links = [link["href"] for link in a_tags]

    for link in links:
        print(link)
        page = scraper.get(link).text
        soup = BeautifulSoup(page, "lxml")
        remove_ads(soup)

        page_names = link.split("/")
        filename = [filename for filename in page_names if filename != ""][-1]

        save_to_html(soup, filename)


def index_page(soup: Any) -> None:
    scrape_images(soup)
    scrape_links(soup)

    a_tags = soup.find_all("a")
    for link in a_tags:
        page_name = link["href"].split("/")
        page = [page for page in page_name if page != ""]
        print(page[-1])

        link["href"] = "./classcentral/" + page[-1] + ".html"

    path_to_file = "./index.html"
    with open(path_to_file, "w", encoding="utf-8") as file:
        file.write(str(soup))


def main() -> None:
    scraper = cloudscraper.create_scraper(
        browser={"browser": "firefox", "platform": "windows", "mobile": False}
    )
    url = "https://www.classcentral.com/"
    page = scraper.get(url).text
    soup = BeautifulSoup(page, "lxml")

    remove_href_whitespaces(soup)
    parse_all_pages(soup, scraper)
    # index_page(soup)


if __name__ == "__main__":
    main()
