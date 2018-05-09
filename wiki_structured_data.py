# exploring what we get from DBPedia
# http://skipperkongen.dk/2016/08/18/how-to-get-structured-wikipedia-data-via-dbpedia/
import json
import requests as re

URL_DBPEDIA_BASE = "http://dbpedia.org/data/"
PATH_DBPEDIA_RESOURCE = "http://dbpedia.org/resource/"
URL_DBPEDIA_ONTOLOGY_BASE= "http://dbpedia.org/ontology/"



class DBPediaEntry:
    """A particular DBPedia's Entry"""

    def __init__(self, name):
        self.name = name
        self.url = URL_DBPEDIA_BASE + name
        self.full_json = re.get(self.url +'.json').json()
        print("Full json keys /n" + str(self.full_json.keys()))
        self.name_json = self.full_json[PATH_DBPEDIA_RESOURCE + self.name]
        print("Name json keys /n" + str(self.name_json.keys()))
        self.en_abstract = self.get_abstract(self.name_json)
        self.type = self.get_node(self.name_json, 'type')
        self.wiki_page_id = self.get_node(self.name_json, 'wikiPageID')
        self.industry = self.get_node(self.name_json, 'industry')
        self.founded_by = self.get_node(self.name_json, 'foundedBy')
        self.foundation_place = self.get_node(self.name_json, 'foundationPlace')
        self.no_employees = self.get_node(self.name_json, 'numberOfEmployees')


    def get_abstract(self, data):
        node = data[URL_DBPEDIA_ONTOLOGY_BASE + 'abstract']
        res = ""
        for i in node:
            #print("Has abstract in : " + i['lang'])
            if (i['lang'] == "en"):
                res = i['value']
                print('En abstract = ', res)
        return res if res else None


    def get_node(self, data, node_name):
        node = data[URL_DBPEDIA_ONTOLOGY_BASE + node_name]
        print(node)
        res = []
        if isinstance(node, (list)):
            for i in node:
                print(node_name + ' = ', res)

        # returning the right thing
        if len(res) < 1:
            print(node_name + ' = ', 'not found')
            return None
        elif len(res) < 2:
            print(node_name + ' = ', res[0])
            return res[0]
        else:
            print(node_name + ' = ', res)
            return res


def main(options):
    print("Retrived data for " + options.pn)
    db_entry = DBPediaEntry(options.pn)
    print(len(db_entry.full_json.keys()))
    print (db_entry)
    #print("second time \n" + json.dumps(db_entry.full_json, indent=4, sort_keys=True))


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser(description="Wiki target")
    p.add_argument("-pn", help="the target wikipedia Page Name", default="The_Coca-Cola_Company")

    main(p.parse_args())