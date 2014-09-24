import sys, glob
sys.path.append('gen-py')

from gene import Gene
from gene.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import requests

class GeneHandler:
  def __init__(self):
    self.log = {}

  def get(self):
    hits=hits_item()
    work = cdk2()
    r=requests.get("http://mygene.info/v2/query?q=cdk2")
    date = r.json()
    hits_list=[]
    for item in date["hits"]:
        hits.entrezgene = item["entrezgene"]
        hits.name=item["name"]
        hits._score=item["_score"]
        hits.symbol=item["symbol"]
        hits._id=item["_id"]
        hits.taxid=item["taxid"]
        hits_list.append(hits)
    work.hits=hits_list
    work.max_score={"max_score": 386.08304}
    work.took={"took": 5}
    work.total={"total": 26}
    print "process a request "
    return work


handler = GeneHandler()
processor = Gene.Processor(handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

# You could do one of these for a multithreaded server
#server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
#server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

print 'Starting the server...'
server.serve()
print 'done.'
