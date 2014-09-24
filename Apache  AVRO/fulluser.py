import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import urllib2
import json
import os

from pymongo import MongoClient
client = MongoClient()

schema = avro.schema.parse(open("user.avsc").read())

writer = DataFileWriter(open("users.avro", "w"), DatumWriter(), schema)

index=0
db=client.xtb

cur=db.gene.find(timeout=False)

fd=open("error_id.txt","w")

count=0
error_count=0

for item in cur:
	index=index+1
	if index>=50000:
		writer.close()
		os.remove("users.avro")
		writer = DataFileWriter(open("users.avro", "w"), DatumWriter(), schema)
		index=0
		count=count+50000
		print '===%d=='%count
	try:
		item["_timestamp"]=str(item["_timestamp"])
		writer.append(item)
	except Exception:
		error_count=error_count+1
		print "error %d"%error_count
		str=",%s"%item["_id"]
		fd.writelines(str)
		fd.flush()
print "====end===="
writer.close()
fd.close()


#reader = DataFileReader(open("users.avro", "r"), DatumReader())
#for user in reader:
#    print user
#reader.close()

