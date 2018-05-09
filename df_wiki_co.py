import wiki_structured_data
import df_wiki_djia_co
import pandas as pd
import os

class WikipediaCompanyInfo(object):
    """takes a list of wikipedia final paths for companies and returns a pandas dataFrame with various attributes for each company"""

    def __init__(self, target_co_list):
        self.df = self.get_df(target_co_list)

    def get_df(self, list):

        CSV_FILENAME = 'data/djia_detail_data.csv'

        if os.path.exists(CSV_FILENAME):
            # use local data copy
            print("Found " + CSV_FILENAME + " locally ---- LOADING")
            data_df = pd.read_csv(CSV_FILENAME, index_col=0)
        else:
            # get data from wikipedia
            comp_data = []
            for co in list:
                co_data = vars(wiki_structured_data.DBPediaEntry(co))
                del co_data["full_json"]
                del co_data["name_json"]
                print(co_data)
                comp_data.append(co_data)

            data_df = pd.DataFrame(comp_data)
            data_df.to_csv(CSV_FILENAME)
        print(data_df.head())
        return data_df


def main():
    companies = df_wiki_djia_co.WikipediaDjiaCompanies()
    df = WikipediaCompanyInfo(companies.df['Wiki_Page_Name'])
    print('stop')

if __name__ == '__main__':
    main()