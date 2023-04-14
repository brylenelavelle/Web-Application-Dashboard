from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:52051/test?authSource=AAC' % ("aacuser", "password")) 
        # Select the 'AAC' database
        self.database = self.client['AAC']

    # To define create method for AnimalShelter class
    def create(self, data):
        # To check if data is empty
        if data is not None:
            try:
                # To insert data into 'animals' collection
                insert = self.database.animals.insert(data)  # data should be dictionary    
                # To check if the data has been successfully inserted
                if insert:
                    return True
                else:
                    return False
             # If an error occurs during insertion, return False
            except:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # To define read method for AnimalShelter class
    def read(self, query):
        # If a query is provided, retrieve data based on query
        if query is not None:
            data = self.database.animals.find(query,{"_id": False})
        # If no query is provided, retrieve all data in the collection
        else:
            data = self.database.animals.find({}, {"_id": False})
            
        return data

    # To define update method for AnimalShelter class
    def update(self, query, update_data):
        # Check if query and update_data are not empty
        if query is not None and update_data is not None:
            try:
                # Update documents matching the query with the provided update data
                result = self.database.animals.update_many(query, {"$set": update_data})
                # Check if any document has been updated successfully
                if result.modified_count > 0:
                    # Return a JSON success message with the number of documents updated
                    return {"success": True, "message": f"{result.modified_count} document(s) updated."}
                else:
                    # Return a JSON error message if no documents were updated
                    return {"success": False, "message": "No documents updated."}
            # If an error occurs during the update, return a JSON error message
            except:
                return {"success": False, "message": "Error during update."}
        else:
            raise Exception("Query and update_data parameters cannot be empty.")

    # To define delete method for AnimalShelter class
    def delete(self, query):
        # Check if query is not empty
        if query is not None:
            try:
                # Delete documents matching the query
                result = self.database.animals.delete_many(query)
                # Check if any document has been deleted successfully
                if result.deleted_count > 0:
                    # Return a JSON success message with the number of documents deleted
                    return {"success": True, "message": f"{result.deleted_count} document(s) deleted."}
                else:
                    # Return a JSON error message if no documents were deleted
                    return {"success": False, "message": "No documents deleted."}
            # If an error occurs during the deletion, return a JSON error message
            except:
                return {"success": False, "message": "Error during deletion."}
        else:
            raise Exception("Query parameter cannot be empty.")