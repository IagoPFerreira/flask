from .db import db
from .abstractModel import AbstractModel


class MessageModel(AbstractModel):
    _collection = db["messages"]

    def __init__(self, json_data):
        super().__init__(json_data)

    def to_dict(self):
        return {
            '_id': str(self.data['_id']),
            'message': self.data['message'],
            'from': self.data['from'],
            'to': self.data['to'],
            'time': self.data['time']
        }
