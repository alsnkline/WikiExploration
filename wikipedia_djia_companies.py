import wikipedia
import os
from bs4 import BeautifulSoup
import pandas as pd

class WikipediaDjiaCompanies():
    """An class that uses the wikipedia page to create a list of Dow Jones Industrial Average companies
        gathering elements of data for them
        creating a pandas dataframe that can be saved to csv or used directly"""


    def __init__(self):
        self.df = self.get_df()


    def get_df(self):

        CSV_DJIA_FILENAME = 'data/dow_jones_ia_companies.csv'

        if os.path.exists(CSV_DJIA_FILENAME):
            # use local data copy
            print("Found " + CSV_DJIA_FILENAME + " locally ---- LOADING")
            self.company_data = pd.read_csv(CSV_DJIA_FILENAME, index_col=0)
        else:
            # get data from wikipedia
            self.company_data = self.get_company_data()

        djia_df = pd.DataFrame(self.company_data)
        djia_df.to_csv(CSV_DJIA_FILENAME)
        print(djia_df.head())
        return djia_df


    def get_company_data(self):

        print("No data locally ---- PARSING from Wikipedia")
        djia_companies = []
        page = wikipedia.page(title="Dow_Jones_Industrial_Average")
        html_soup = BeautifulSoup(page.html(), 'html.parser')
        components_table = html_soup.find('table', class_='wikitable sortable')

        for r in [row for row in components_table.contents if row.name == 'tr']:
            # print(r.prettify)
            cells = [td for td in r.contents if td.name == 'td']
            if cells:  # first row has only 'th' and doesn't need to be parsed
                djia_entry = {
                    "Company_Name": cells[0].text.rstrip('\n'),
                    "Wiki_Link": cells[0].find('a')['href'],
                    "Wiki_Page_Name": cells[0].find('a')['href'].replace('/wiki/', ''),
                    "Exchange": cells[1].text.rstrip('\n'),
                    "Ticker_Symbol": cells[2].text.rstrip('\n'),
                    "Industry": cells[3].text.rstrip('\n'),
                    "Date_Added_To_DJIA": cells[4].text.rstrip('\n')
                }
                djia_companies.append(djia_entry)
        return djia_companies


def main():
    companies = WikipediaDjiaCompanies()


if __name__ == '__main__':

    main()