from .db import db
from .abstractModel import AbstractModel


class MessageModel(AbstractModel):
    _collection = db["chat"]

    def __init__(self, json_data):
        super().__init__(json_data)

    def to_dict(self):
        return {
            "message": self.data["message"],
            "to": self.data["to"],
            "from": self.data["from"],
            "time": self.data["time"],
        }
