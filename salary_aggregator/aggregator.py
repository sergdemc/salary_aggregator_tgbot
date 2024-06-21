from datetime import datetime

from salary_aggregator.db import get_db
from salary_aggregator.utils import (
    add_month,
    get_dt_delta,
    get_format_data,
    get_group_id,
)


def aggregate_salaries(dt_from: str, dt_upto: str, group_type: str):
    db = get_db()
    collection = db['salaries']

    dtfrom = datetime.fromisoformat(dt_from)
    dtupto = datetime.fromisoformat(dt_upto)

    group_id, date_format = get_group_id(group_type)

    pipeline = [
        {'$match': {'dt': {'$gte': dtfrom, '$lte': dtupto}}},
        {'$group': {
            '_id': group_id,
            'total': {'$sum': '$value'}
        }},
        {'$sort': {'_id': 1}}
    ]

    results = list(collection.aggregate(pipeline))
    filled_results = fill_missing_periods(results, dt_from, dt_upto, group_type, date_format)

    return filled_results


def fill_missing_periods(results: list, dt_from: str, dt_upto: str, group_type: str, date_format: str) -> dict:
    filled_results = {
        'dataset': [],
        'labels': []
    }

    delta = get_dt_delta(group_type)

    current_period = datetime.fromisoformat(dt_from)
    dt_upto = datetime.fromisoformat(dt_upto)
    result_index = 0

    while current_period <= dt_upto:
        if result_index < len(results):
            result_date = get_format_data(date_format, result_index, results)

            if result_date == current_period.strftime(date_format):
                filled_results['dataset'].append(results[result_index]['total'])
                filled_results['labels'].append(result_date)
                result_index += 1
            else:
                filled_results['dataset'].append(0)
                filled_results['labels'].append(current_period.strftime(date_format))
        else:
            filled_results['dataset'].append(0)
            filled_results['labels'].append(current_period.strftime(date_format))

        if group_type == 'month':
            current_period = add_month(current_period)
        else:
            current_period += delta

    return filled_results
