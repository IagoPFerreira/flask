import random
from .db import db
from .abstractModel import AbstractModel


class MusicModel(AbstractModel):
    _collection = db["musics"]

    def __init__(self, json_data):
        super().__init__(json_data)

    @classmethod
    def get_random(cls):
        data = cls.find()
        if not data:
            return
        return random.choice(data)

    def to_dict(self):
        return {
            '_id': str(self.data['_id']),
            'name': self.data['name'],
            'artist': self.data['artist'],
            'album': self.data['album'],
            'release_year': str(self.data['release_year']),
            'gender': self.data['gender'],
            'image': self.data['image'],
        }
