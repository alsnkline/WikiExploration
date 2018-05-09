# reference: http://blog.kaggle.com/2017/01/31/scraping-for-craft-beers-a-dataset-creation-tutorial/?utm_medium=email&utm_source=intercom&utm_campaign=new+user+onboarding
# and: http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

class WikiPage:
    """A particular Wikipedia page and its data"""
    EN_WIKI_URL = "https://en.wikipedia.org/wiki/"      # base URL for English wikipedia

    def __init__(self, name):
        self.name = name      # Wiki page name, last part of wiki URL, also often the displayed title
        if ('/wiki/' in name):
            self.url = self.EN_WIKI_URL + self.name.replace('/wiki/', '')
        else:
            self.url = self.EN_WIKI_URL + self.name
        self.html_soup = self.getRawPageData()

    def getRawPageData(self):
        html = urlopen(self.url)
        html_soup = BeautifulSoup(html, 'html.parser')
        return html_soup

    def ak_description(self):
        print("Class: " + type(self).__name__, end=' ')
        print("doc: " + self.__doc__)
        print("Page URL: " + self.url)


def main(options):
    page = WikiPage(options.pn)
    print("Retrived data for " + page.name)
    print(page.ak_description())


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser(description="Wiki page and data object")
    p.add_argument("-pn", help="the target wikipedia Page Name", default="Caterpillar_Inc.")

    main(p.parse_args())