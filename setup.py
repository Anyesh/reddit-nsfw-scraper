import sys

from setuptools import find_packages, setup


def read_file(name):
    with open(name) as fd:
        return fd.read()


setup(
    name="nsfw-scraper",
    version="0.1.6",
    description=("Reddit NSFW scraper"),
    url="https://github.com/Anyesh/reddit-nsfw-scraper",
    # download_url="https://github.com/Anyesh/reddit-nsfw-scraper",
    author="Anish Shrestha",
    author_email="hello@anyesh.xyz",
    license="Public domain",
    packages=find_packages(exclude=["tests"]),
    install_requires=read_file("requirements.txt").splitlines(),
    entry_points={
        "console_scripts": ["nsfw-scraper=start_scraper:cli"],
    },
    test_suite="nose.collector",
    zip_safe=False,
    keywords=["reddit", "nsfw", "scraper"],
)
