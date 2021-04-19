import os
import shutil
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


class NSFWScraper:
    def __init__(self, url, config) -> None:
        self.url = url
        self.config = config

    def __save_media(self, media_url: str, handle: str):
        Path(f"output/{handle.replace(' ', '_')}").mkdir(parents=True, exist_ok=True)
        local_filename = (
            Path("output") / handle.replace(" ", "_") / media_url.split("/")[-1]
        )

        if not os.path.exists(local_filename):
            with requests.get(media_url, stream=True) as r:
                with open(local_filename, "wb") as f:
                    shutil.copyfileobj(r.raw, f)
        return local_filename

    def __next(self):
        pass

    @staticmethod
    def crawl(url: str) -> BeautifulSoup:
        raw = requests.get(url).text
        soup = BeautifulSoup(raw, "html.parser")
        return soup

    def __get_media_url(self, item: BeautifulSoup):
        media_url = None
        a_el = item.find("a", {"class": "slider_init_href"})
        if a_el:
            el_source = a_el.get("href")
            soup = self.crawl(el_source)
            media_col = soup.find("div", {"class": "col-lg-6 sh-section__item stamp"})
            img_section = media_col.find("div", {"class": "sh-section__image"})
            vid_section = img_section.find("video")
            if vid_section:
                return vid_section.find("source").get("src")

            img_ = img_section.find("img")
            media_url = img_["src"] if img_ else None

            return media_url

    def __parse_items(self, soup_data: BeautifulSoup, handle: str) -> BeautifulSoup:
        items = soup_data.find_all(eval(handle))
        return items

    def __assemble_url(self, page: int, query: str):
        query_: str = query.replace(" ", "+")
        return (
            self.url + "/search-page/" + str(page) + self.config + "&q=" + str(query_)
        )

    def start(self, query: str, max_pages: int = 2):
        page: int = 1
        while page <= max_pages:
            full_url: str = self.__assemble_url(page, query)
            print(f"Scraping page: {page} of {query}")
            soup: BeautifulSoup = self.crawl(full_url)
            items = self.__parse_items(
                soup, handle=""""div", {"class": "sh-section__item"}"""
            )
            for item in items:
                media_url = self.__get_media_url(item)
                if media_url:
                    filename = self.__save_media(media_url, handle=query)
                    print(f"Saved: {filename}")

            page += 1
