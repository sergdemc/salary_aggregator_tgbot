from pymongo import MongoClient

import config


def get_db():
    client = MongoClient(config.MONGO_URI)
    db = client['salary_stats']
    return db
