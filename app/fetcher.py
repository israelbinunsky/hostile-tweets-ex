from pymongo import MongoClient
import pandas as pd

class fetcher:
   def __init__(self, uri, dbname, collection):
       self.mongodb_client = MongoClient(uri)
       self.database = self.mongodb_client[dbname]
       self.collection = collection

   def get_collection(self, filter = None, limit=0):
       collection = self.database[self.collection]
       collection = list(collection.find(filter=filter, limit=limit))
       return collection

