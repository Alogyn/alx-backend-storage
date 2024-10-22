#!/usr/bin/env python3

def list_all(mongo_collection):
    '''
    Function that lists all documents in Collection.
    '''
    return [doc for doc in mongo_collection.find()]
