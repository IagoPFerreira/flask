from abc import ABC
from pymongo.collection import ReturnDocument
from bson.objectid import ObjectId


class AbstractModel(ABC):
    _collection = None

    def __init__(self, deadline):
        self.deadline = deadline

    def save(self):
        result = self._collection.insert_one(self.deadline)
        inserted_document = self._collection.find_one({
            "_id": result.inserted_id
        })
        self.deadline = inserted_document
        return self.deadline

    def update(self, deadline):
        result = self._collection.find_one_and_update(
            {"_id": self.deadline["_id"]},
            {"$set": deadline},
            return_document=ReturnDocument.AFTER,
        )

        self.deadline = result
        return self.deadline

    def delete(self):
        self._collection.delete_one({"_id": ObjectId(self.deadline["_id"])})

    @classmethod
    def find(cls, query={}):
        deadline = cls._collection.find(query)
        return [cls(d) for d in deadline]

    @classmethod
    def find_one(cls, query={}):
        deadline = cls._collection.find_one(query)
        print(deadline)
        return cls(deadline) if deadline else None
