# exploring what we get from DBPedia
# http://skipperkongen.dk/2016/08/18/how-to-get-structured-wikipedia-data-via-dbpedia/
import argparse
import json
import requests as re

DBPEDIA_BASE_URL = 'http://dbpedia.org/data/'
DBPEDIA_ONTOLOGY = 'http://dbpedia.org/ontology/abstract'

def main(options):
    raw_data = re.get(DBPEDIA_BASE_URL + options.pn + '.json').json()
    print("Retrived data for " + options.pn)
    print(len(raw_data.keys()))
    print(json.dumps(raw_data, indent=4, sort_keys=True))

    #abstract = raw_data['http://dbpedia.org/resource/Caterpillar_Inc.']['http://dbpedia.org/ontology/abstract']
    abstract = raw_data['http://dbpedia.org/resource/'+ options.pn]['http://dbpedia.org/ontology/abstract']
    for i in abstract:
        if (i['lang'] == "en"):
            print(i['value'])

    #print(json.dumps(ddata, indent=4, sort_keys=True))


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser(description="Wiki target")
    p.add_argument("-pn", help="the target wikipedia Page Name", default="The_Coca-Cola_Company")

    main(p.parse_args())