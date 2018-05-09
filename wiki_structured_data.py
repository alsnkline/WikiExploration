# exploring what we get from DBPedia
# http://skipperkongen.dk/2016/08/18/how-to-get-structured-wikipedia-data-via-dbpedia/
import json
import requests as re

URL_DBPEDIA_BASE = "http://dbpedia.org/data/"
URL_DBPEDIA_ONTOLOGY_BASE= "http://dbpedia.org/ontology/"
PATH_DBPEDIA_RESOURCE = "http://dbpedia.org/resource/"



class DBPediaEntry:
    """A particular DBPedia's Entry"""

    def __init__(self, name):
        self.name = name
        self.url = URL_DBPEDIA_BASE + name
        self.full_json = re.get(self.url +'.json').json()
        print("Full json keys /n" + str(self.full_json.keys()))
        self.name_json = self.full_json[PATH_DBPEDIA_RESOURCE + self.name.replace("%26", "&").replace("%27", "'")]
        print("{} self.name_json keys: {} /n".format(PATH_DBPEDIA_RESOURCE + self.name, str(self.name_json.keys())))

        self.wiki_page_id = self.get_node(self.name_json, 'wikiPageID')
        self.wiki_page_revision_id = self.get_node(self.name_json, 'wikiPageRevisionID')

        self.wiki_page_redirects = self.get_node(self.name_json, 'wikiPageRedirects')
        if self.wiki_page_redirects :
            print("Page redirects to : {}".format(self.wiki_page_redirects))
        else :
            self.en_abstract = self.get_abstract(self.name_json)
            self.type = self.get_node(self.name_json, 'type')
            self.industry = self.get_node(self.name_json, 'industry')
            self.founded_by = self.get_node(self.name_json, 'foundedBy')
            self.foundation_place = self.get_node(self.name_json, 'foundationPlace')
            self.no_employees = self.get_node(self.name_json, 'numberOfEmployees')


    def get_abstract(self, data):
        abstract = data[URL_DBPEDIA_ONTOLOGY_BASE + 'abstract']
        res = ""
        for i in abstract:
            #print("Has abstract in : " + i['lang'])
            if (i['lang'] == "en"):
                res = i['value']
                print('En abstract = ', res)
        return res if res else None


    def get_node(self, data, node_name):

        if (URL_DBPEDIA_ONTOLOGY_BASE + node_name in data):
            node = data[URL_DBPEDIA_ONTOLOGY_BASE + node_name]
            # print(node)
            res = []
            if isinstance(node, (list)):
                for i in node:
                    res.append(i['value'])

            # returning the right thing
            if len(res) == 1:
                print(node_name + ' = ', res[0])
                return res[0]
            else:
                print(node_name + ' = ', res)
                return res
        else:
            print(node_name + ' = ', 'not found')
            return None


def main(options):
    print("Retriving data for " + options.pn)
    db_entry = DBPediaEntry(options.pn)
    #print("second time \n" + json.dumps(db_entry.full_json, indent=4, sort_keys=True))


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser(description="Wiki target")
    #name = "166826"
    name = "Johnson_%26_Johnson"
    #name = "Johnson_&_Johnson"
    p.add_argument("-pn", help="the target wikipedia Page Name", default=name)

    main(p.parse_args())