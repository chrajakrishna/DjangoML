import pymongo
from pymongo import MongoClient
import urllib

class MongoConnection(object):

    def __init__(self):
        databname = "cheesepy"
        mongo_uri = "mongodb://cheesepydev:" + urllib.parse.quote("dev@123") + "@ds141082.mlab.com:41082/" + databname 
        connMongo = MongoClient(mongo_uri)
        self.db = connMongo['cheesepy']

    def get_collection(self,name):
        self.collection = self.db[name]



