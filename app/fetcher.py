from pymongo import MongoClient

class fetcher:
   def __init__(self, uri, dbname, collection):
       self.mongodb_client = MongoClient(uri)
       self.database = self.mongodb_client[dbname]
       self.collection = collection

   def get_collection(self):
       collection = self.database[self.collection]
       return collection

   def find(self, filter = None, limit=0):
       collection = self.database[self.collection]
       items = list(collection.find(filter=filter, limit=limit))
       return items

