import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import urllib2
import json

schema = avro.schema.parse(open("user.avsc").read())

writer = DataFileWriter(open("users.avro", "w"), DatumWriter(), schema)

#list_id = raw_input(u"aa\n")
#list_id = list_id.split(' ')
list_id=range(1,1000)


from pymongo import MongoClient
client = MongoClient()
db=client.xtb
cur=db.gene.find_one({'_id':'1132577'})
cur['_timestamp']=str(cur['_timestamp'])

for item in [1]:
    try:
        writer.append(cur)
        print str(item) + "   success"
       # print str(item)
    except Exception:
        print str(item) + "   faile"



writer.close()

#reader = DataFileReader(open("users.avro", "r"), DatumReader())
#for user in reader:
#    print user
#reader.close()

