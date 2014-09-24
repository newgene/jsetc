#!/usr/bin/env python
# coding=utf-8
import requests
from requests.exceptions import HTTPError
from pyld import jsonld
import json
import os

url_mod = r"http://mygene.info/v2/gene/%d?fields= \
            name,symbol,entrezgene,taxid,uniprot"

context = {
    "@context": {
                "xsd": "http://www.w3.org/2001/XMLSchema#",
                "name": "https://identifiers.org/name",
                "_id": "https://identifiers.org/productID",
                "symbol": "https://identifiers.org/symbol",
                "uniprot": "http://identifiers.org/uniprot/",
                "Swiss-Prot": "https://identifiers.org/Swiss-Prot",
        "TrEMBL": {
                        "@id": "https://identifiers.org/TrEMBL",
                        "@container": "@list"
        },
        "entrezgene": {
                        "@id": "https://identifiers.org/entrezgene",
                        "@type": "xsd:integer"
        },
        "taxid": {
                        "@id": "https://identifiers.org/taxid",
                        "@type": "xsd:integer"
        }
    }

}

while True:
    os.system("clear")
    gene_id = raw_input("input gene id\n")
    url = url_mod % int(gene_id)
    try:
        r = requests.get(url)
        r.raise_for_status()
    except HTTPError:
        print "no id"

    data = r.json()
    print "\nraw json data"
    print  json.dumps(data)

    data["@context"] = context["@context"]
    print "\ncompacted  data"
    print json.dumps(data)

    doc = jsonld.expand(data)
    print "\nexpanded data"
    print json.dumps(doc)

    data_nor = jsonld.normalize(doc, {'format': 'application/nquads'})
    print "\n N-Quads data"
    print data_nor
    raw_input("input any key to continue")
