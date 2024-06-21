from bson import decode_all
from pymongo.errors import DuplicateKeyError

from salary_aggregator.db import get_db


def load_data_to_mongo(filepath: str) -> None:
    db = get_db()
    collection = db['salaries']

    with open(filepath, 'rb') as file:
        records = decode_all(file.read())

        for record in records:
            if not collection.find_one({'_id': record['_id']}):
                try:
                    collection.insert_one(record)
                except DuplicateKeyError:
                    print(f"Document with _id {record['_id']} already exists and will be skipped.")


if __name__ == '__main__':
    load_data_to_mongo('sampleDB/sample_collection.bson')
