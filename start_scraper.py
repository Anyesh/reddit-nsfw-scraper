from config import ROOT_URL, host_config
from src.Scraper import NSFWScraper

nsfw_scraper = NSFWScraper(url=ROOT_URL, config=host_config)
nsfw_scraper.start("hidori rose")
