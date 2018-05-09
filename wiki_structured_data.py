# exploring what we get from DBPedia
# http://skipperkongen.dk/2016/08/18/how-to-get-structured-wikipedia-data-via-dbpedia/
import json
import requests as re

URL_DBPEDIA_BASE = "http://dbpedia.org/data/"
PATH_DBPEDIA_RESOURCE = "http://dbpedia.org/resource/"
URL_DBPEDIA_ONTOLOGY_ABSTRACT = "http://dbpedia.org/ontology/abstract"


class DBPediaEntry:
    """A particular DBPedia's Entry"""

    def __init__(self, name):
        self.name = name
        self.url = URL_DBPEDIA_BASE + name
        self.full_json = re.get(self.url +'.json').json()
        print("first time /n" + str(self.full_json.keys()))
        self.abstract = self.get_abstract(self.full_json)

    def get_abstract(self, data):
        abstract = data[PATH_DBPEDIA_RESOURCE + self.name][URL_DBPEDIA_ONTOLOGY_ABSTRACT]
        for i in abstract:
            print(i['value'])
            if (i['lang'] == "en"):
                print(i['value'])

def main(options):
    db_entry = DBPediaEntry(options.pn)
    print("Retrived data for " + options.pn)
    print(len(db_entry.full_json.keys()))
    print("second time \n" + json.dumps(db_entry.full_json, indent=4, sort_keys=True))


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser(description="Wiki target")
    p.add_argument("-pn", help="the target wikipedia Page Name", default="The_Coca-Cola_Company")

    main(p.parse_args())