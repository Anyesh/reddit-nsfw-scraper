import argh

from config import ROOT_URL, host_config
from src.Scraper import NSFWScraper


@argh.arg("--title", "-t", help="Title to scrape the reddit.")
@argh.arg("--max-pages", "-p", help="Max # pages to scrape.")
def main(title: str = "hidori rose", max_pages: int = 5) -> None:
    nsfw_scraper = NSFWScraper(url=ROOT_URL, config=host_config)
    nsfw_scraper.start(query=title, max_pages=max_pages)


if __name__ == "__main__":
    argh.dispatch_command(main)
