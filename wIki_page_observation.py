import wikipedia
import mediawiki
import pandas as pd
import wiki_page_scraper
import df_wiki_djia_co
from bs4 import BeautifulSoup

CSV_PAGE_DATA_FILENAME = 'dj_ia_companies.csv'

def get_page_observations(title):
    try:
        page = wikipedia.page(title=title)
        page_entry = {
            "categories" : page.categories,
            "content" : page.content,
            #"html" : page.html,
            "images" : page.images,
            "image_count": len(page.images),
            "links" : page.links,
            "link_count" : len(page.links),
            "parent_id" : page.parent_id,
            "references" : page.references,
            "revision_id" : page.revision_id,
            "sections" : page.sections,
            "section_count": len(page.sections),
            "summary" : page.summary
        }
        return page_entry
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    except   wikipedia.exceptions.PageError as e:
        print(e)
        print("Problem with " + title)
        return None


def collect_obs_from_wikipedia(companies):
    # use the Wikipedia library - github shows its old, last updated in 2016
    # some pages don't load with wikipedia.page(title=title)
    # Page id "caterpillar inc" does not match any pages. Try another id!
    # Page id "the cock coal company" does not match any pages. Try another id!
    # Problem with The_Coca-Cola_Company
    # Page id "johnson 26 johnson" does not match any pages. Try another id!
    # Problem with Johnson_%26_Johnson
    # Page id "mercer 26 cm" does not match any pages. Try another id!
    # Problem with Merck_%26_Co.
    # Page id "proctor 26_gamble" does not match any pages. Try another id!
    # Problem with Procter_%26_Gamble
    # Page id "visa inc" does not match any pages. Try another id!
    # Problem with Visa_Inc.
    djia_wiki_pages = []
    for company in companies:
        print("Getting Wikipedia page data for : " + company)
        page_obs = get_page_observations(company)
        if page_obs:
            djia_wiki_pages.append(get_page_observations(company))

    pages_df = pd.DataFrame(djia_wiki_pages)
    print(pages_df.head())
    print(pages_df.describe())
    pages_df.to_csv(CSV_PAGE_DATA_FILENAME)


def collect_obs_scraper(companies):
    djia_wiki_pages = []
    for company in companies:
        page = wiki_page_scraper.WikiPage(company)
        # have to do all the parsing


def get_page_obs(title):
    # this also has the issue of some of the titles not being recognized.
    # need to use the page_ids rather than the partial URLs
    # this blog gives a roadmap http://2015.compjour.org/tutorials/exploring-wikipedia-api-via-python/
    wiki = mediawiki.MediaWiki()
    p = wiki.page(title)
    page_entry = {
        "categories": p.categories,
        "content": p.content,
        # "html" : p.html,
        "images": p.images,
        "image_count": len(p.images),
        "links": p.links,
        "link_count": len(p.links),
        "page_id": p.pageid,
        "parent_id": p.parent_id,
        "redirects": p.redirects,
        "redirect_count": len(p.redirects),
        "references": p.references,
        "references_count": len(p.references),
        "revision_id": p.revision_id,
        "sections": p.sections,
        "section_count": len(p.sections),
        "summary": p.summary,
        "title": p.title,
        "url": p.url
    }
    return page_entry


def collect_obs_pymediawiki(companies):
    djia_wiki_pages = []
    for company in companies:
        print("Getting Wikipedia page data for : " + company)
        page_obs = get_page_obs(company)
        if page_obs:
            djia_wiki_pages.append(get_page_observations(company))

    pages_df = pd.DataFrame(djia_wiki_pages)
    print(pages_df.head())
    print(pages_df.describe())
    pages_df.to_csv(CSV_PAGE_DATA_FILENAME)


def main(options):
    djia_comps = df_wiki_djia_co.WikipediaDjiaCompanies()
    #collect_obs_from_wikipedia(djia_comps.df['Wiki_Page_Name'])
    #collect_obs_scraper(djia_df['Wiki_Link'])
    collect_obs_pymediawiki(djia_comps.df['Wiki_Page_Name'])


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser(description="Wiki page data for the Dow Jones Industrial Average Companies")

    main(p.parse_args())