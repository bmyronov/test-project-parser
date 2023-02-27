import os
from typing import Any

from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from deep_translator.exceptions import NotValidPayload


def translate(tags: Any) -> None:
    try:
        for tag in tags:
            if tag.string != None:
                try:
                    old_tag = tag.string
                    translated = GoogleTranslator(source="en", target="hi").translate(
                        tag.string
                    )
                    if old_tag.string != "":
                        tag.string = translated
                    print(old_tag.string)
                    print(tag)
                    print(f"Original: {old_tag} \t" f"Translated: {tag.string}\n")

                except TypeError:
                    pass
                except NotValidPayload:
                    pass

    except TypeError:
        pass

        # text = tag.text.split("\n")
        # formated_text = [f_text for f_text in text if f_text != ""]
        # print(formated_text)

        """
        try:
            if formated_text == []:
                del formated_text
            else:
                formated_text = [f_text for f_text in formated_text if f_text != []]
                translated = GoogleTranslator(source="en", target="hi").translate(
                    formated_text[0]
                )
                print(translated)
                tag.replace_with(translated)
                print(tag)
        except TypeError as err:
            pass
        """


def translate_index_page() -> None:
    with open("./index.html") as file:
        page = file.read()
    soup = BeautifulSoup(page, "lxml")
    favicons = soup.find_all("link")
    for favicon in favicons:
        if favicon["href"] == "/favicon-32x32.png":
            favicon["href"] == "./favicon-32x32.png"

        if favicon["href"] == "/favicon-16x16.png":
            favicon["href"] == "./favicon-16x16.png"

    title = soup.find(itemprop="name")
    translate(title)

    try:
        span_tags = soup.find_all("span")
        translate(span_tags)

        button_tag = soup.find_all("button")
        translate(button_tag)

        a_tags = soup.find_all("a")
        translate(a_tags)

        p_tags = soup.find_all("p")
        translate(p_tags)

        h2_tags = soup.find_all("h2")
        translate(h2_tags)

        h3_tags = soup.find_all("h3")
        translate(h3_tags)

        h4_tags = soup.find_all("h4")
        translate(h4_tags)

        h5_tags = soup.find_all("h5")
        translate(h5_tags)

        strong_tags = soup.find_all("strong")
        translate(strong_tags)

    except TypeError:
        pass

    logo = soup.find(class_="block medium-up-margin-right-large cmpt-nav-logo")
    logo["span"] = "Class Central"

    """
    try:
        nav_bar = soup.find(
            class_="cmpt-nav row nowrap vert-align-middle absolute width-100 padding-horz-medium border-box"
        )
        if nav_bar:
            login = nav_bar.find(class_="hidden xlarge-up-inline-block")
            login_a_tag = login.find_all(class_="text-1 weight-semi color-charcoal")
            translate(login_a_tag)

            span_tags = nav_bar.find_all("span")
            translate(span_tags)

            button_tag = nav_bar.find_all("button")
            translate(button_tag)

            a_tags = nav_bar.find_all("a")
            translate(a_tags)

            p_tags = nav_bar.find_all("p")
            translate(p_tags)

            logo = nav_bar.find(
                class_="block medium-up-margin-right-large cmpt-nav-logo"
            )
            logo["span"] = "Class Central"

        main_section = soup.find(
            class_="max-950 row vert-align-middle width-centered padding-horz-medium margin-vert-large large-up-padding-vert-large large-up-padding-vert-xxlarge border-box"
        )
        if main_section:
            span_tags = main_section.find_all("span")
            translate(span_tags)

            h2_tags = main_section.find_all("h2")
            translate(h2_tags)

            h3_tags = main_section.find_all("h3")
            translate(h3_tags)

            p_tags = main_section.find_all("p")
            translate(p_tags)

            under_search_bar_p = main_section.find(
                class_="row vert-align-top horz-align-left text-2 medium-up-text-1 margin-top-xsmall padding-horz-xxsmall"
            )
            translate(under_search_bar_p)

            a_tags = main_section.find_all("a")
            translate(a_tags)

        section_discover = soup.find(id="home-discover")
        if section_discover:
            h2_tags = section_discover.find_all("h2")
            translate(h2_tags)

            h3_tags = section_discover.find_all("h3")
            translate(h3_tags)

            span_tags = section_discover.find_all("span")
            translate(span_tags)

            strong_tags = section_discover.find_all("strong")
            translate(strong_tags)

        section_rankings = soup.find(
            class_="width-100 large-down-padding-horz-medium padding-vert-xxlarge border-box"
        )
        if section_rankings:
            h2_tags = section_rankings.find(
                class_="head-2 medium-up-head-1 row horz-align-center vert-align-middle text-center margin-bottom-xsmall"
            )
            translate(h2_tags)

            p_tags = section_rankings.find_all("p")
            translate(p_tags)

            span_tags = section_rankings.find_all("span")
            translate(span_tags)

        section_as_seen = soup.find(
            class_="padding-vert-xxlarge large-down-padding-horz-medium margin-bottom-large border-box"
        )
        if section_as_seen:
            h2_tags = section_as_seen.find_all("h2")
            translate(h2_tags)

        section_home_stats = soup.find(
            class_="relative row vert-align-middle large-up-nowrap width-page width-centered"
        )
        if section_home_stats:
            h2_tags = section_home_stats.find(
                class_="head-2 medium-up-head-1 color-white margin-bottom-medium large-up-margin-bottom-xxlarge"
            )
            translate(h2_tags)

            span_tags = section_home_stats.find_all("span")
            translate(span_tags)

            strong_tags = section_home_stats.find_all("strong")
            translate(strong_tags)

            p_tags = section_home_stats.find_all("p")
            translate(p_tags)

            folowers_p_tags = section_home_stats.find_all(
                class_="text-1 color-white relative padding-left-xlarge"
            )
            translate(folowers_p_tags)

            signups_p_tags = section_home_stats.find_all(
                class_="head-2 weight-semi color-white margin-bottom-xxlarge relative padding-left-xlarge"
            )
            translate(signups_p_tags)

        section_news = soup.find(
            class_="width-page width-centered padding-vert-xxlarge large-down-padding-horz-medium border-box"
        )
        if section_news:
            h2_header_tag = section_news.find(
                class_="head-2 medium-up-head-1 margin-bottom-xsmall color-charcoal"
            )
            translate(h2_header_tag)

            h2_tags = section_news.find_all("h2")
            translate(h2_tags)

            h3_tags = section_news.find_all("h3")
            translate(h3_tags)

            strong_tags = section_news.find_all("strong")
            translate(strong_tags)

            a_tags = section_news.find_all("a")
            translate(a_tags)

            span_tags = section_news.find_all("span")
            translate(span_tags)

            more_span_tag = section_news.find(
                class_="text-1 weight-semi icon-chevron-right-charcoal icon-right-small color-charcoal"
            )
            translate(more_span_tag)

            report = section_news.find(
                class_="margin-left-xxsmall relative inline-block symbol-report"
            )
            translate(report)

        section_home_collections = soup.find(
            class_="z-mid relative width-page width-centered"
        )
        if section_home_collections:
            h2_tags = section_home_collections.find(
                class_="head-2 medium-up-head-1 margin-bottom-xsmall color-charcoal"
            )
            translate(h2_tags)

            strong_tags = section_home_collections.find_all("strong")
            translate(strong_tags)

            span_tags = section_home_collections.find_all("span")
            translate(span_tags)

        footer = soup.find(
            class_="width-page large-down-padding-horz-medium padding-vert-large border-box"
        )
        if footer:
            home_tag = footer.find(class_="text-2 inline-block color-charcoal")
            translate(home_tag)

            a_tags = footer.find_all("a")
            translate(a_tags)

            p_tags = footer.find_all("p")
            translate(p_tags)

    except TypeError:
        pass
    """

    path_to_file = "./translated/index.html"
    with open(path_to_file, "w", encoding="utf-8") as file:
        file.write(str(soup))


def translate_web_pages() -> None:
    page_path = "./classcentral/"
    pages = os.listdir(page_path)

    parsed_path = "./translated/classcentral"
    parsed = os.listdir(parsed_path)

    new_list = [f_name for f_name in pages if f_name not in parsed]

    for filename in new_list:
        with open(page_path + filename) as file:
            print("\n\n", page_path + filename, "\n")
            page = file.read()

            soup = BeautifulSoup(page, "lxml")

            favicons = soup.find_all("link")
            if favicons:
                for favicon in favicons:
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

            title = soup.find("title")
            translate(title)

            try:
                span_tags = soup.find_all("span")
                translate(span_tags)

                button_tag = soup.find_all("button")
                translate(button_tag)

                a_tags = soup.find_all("a")
                translate(a_tags)

                p_tags = soup.find_all("p")
                translate(p_tags)

                h2_tags = soup.find_all("h2")
                translate(h2_tags)

                h3_tags = soup.find_all("h3")
                translate(h3_tags)

                h4_tags = soup.find_all("h4")
                translate(h4_tags)

                h5_tags = soup.find_all("h5")
                translate(h5_tags)

                strong_tags = soup.find_all("strong")
                translate(strong_tags)

            except TypeError:
                pass

            page_folder = "./translated/classcentral/"
            if not os.path.exists(page_folder):  # create only once
                os.mkdir(page_folder)

            translated_path = "./translated/classcentral/"
            with open(translated_path + filename, "w", encoding="utf-8") as file:
                file.write(str(soup))


def main() -> None:
    page_folder = "./translated/"
    if not os.path.exists(page_folder):  # create only once
        os.mkdir(page_folder)

    translate_index_page()
    # translate_web_pages()


if __name__ == "__main__":
    main()
