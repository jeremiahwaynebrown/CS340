from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username='root', password='6TrnXMk2d6'):
        # Connection Variables
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 34731
        DB = 'AAC'
        COL = 'animals'
        
        # Initialize Connection
        self.client = MongoClient(f'mongodb://{username}:{password}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # CREATE method
    def create(self, data):
        if data:
            result = self.collection.insert_one(data)
            return result.acknowledged
        else:
            raise ValueError("Nothing to insert: data parameter is empty")

    # READ method
    def read(self, query):
        if query is not None:
            results = list(self.collection.find(query))
            return results
        else:
            raise ValueError("Query parameter is None")
            
    # UPDATE method
    def update(self, query, update_data):
        try:
            result = self.database.animals.update_many(query, {"$set": update_data})
            return result.modified_count
        except Exception as e:
            print(f"Update error: {e}")
            return 0
    
    def delete(self, query):
        try:
            result = self.database.animals.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Delete error: {e}")
            return 0
