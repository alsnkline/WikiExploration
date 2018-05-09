import wiki_structured_data
import df_wiki_djia_co
import pandas as pd

class WikipediaCompanyInfo:
    """takes a list of wikipedia final paths for companies and returns a pandas dataFrame with various attributes for each company"""

    def __init__(self, target_co_list):
        self.df = self.get_df(target_co_list)

    def get_df(self, list):
        comp_data = []
        for co in list:
            comp_data.append(wiki_structured_data.DBPediaEntry(co))
        print(comp_data)


def main():
    companies = df_wiki_djia_co.WikipediaDjiaCompanies()
    df = WikipediaCompanyInfo(companies.df['Wiki_Page_Name'])

if __name__ == '__main__':
    main()