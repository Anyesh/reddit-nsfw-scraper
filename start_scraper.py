import argh

from config import ROOT_URL, host_config
from nsfw_scraper.Scraper import NSFWScraper


# @argh.arg("--title", "-t", help="Title to scrape the reddit.")
# @argh.arg("--max-pages", "-p", help="Max # pages to scrape.")
def main(title: str, max_pages: int = 5) -> None:
    nsfw_scraper = NSFWScraper(url=ROOT_URL, config=host_config)
    nsfw_scraper.start(query=title, max_pages=max_pages)


def cli():
    argh.dispatch_command(main)


if __name__ == "__main__":
    cli()
