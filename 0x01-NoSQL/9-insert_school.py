#!/usr/bin/env python3
''' Task 9. Insert a document in Python
'''


def insert_school(mongo_collection, **kwargs):
    ''' Function that inserts a new document in a collection based on "kwargs".
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
