# import pymongo
from pymongo import MongoClient
# import datetime


class MongoService(object):
    def __init__(self):
        self.conn = MongoClient(host='127.0.0.1', port=27017)
        self.db = self.conn.english
        self.vocabulary = self.db.vocabulary
        self.iciba = self.db.iciba

    def update(self, collection, query, udata, upsert=True):
        return collection.update(query, {'$set': udata}, upsert=upsert)

    def find(self, collection, query, field={}):
        ret = collection.find(query, field)
        return list(ret)



