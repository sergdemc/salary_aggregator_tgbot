from datetime import datetime, timedelta


def get_group_id(group_type: str) -> tuple[dict, str]:
    if group_type == 'hour':
        return {
            'year': {'$year': '$dt'},
            'month': {'$month': '$dt'},
            'day': {'$dayOfMonth': '$dt'},
            'hour': {'$hour': '$dt'}
        }, '%Y-%m-%dT%H:00:00'
    elif group_type == 'day':
        return {
            'year': {'$year': '$dt'},
            'month': {'$month': '$dt'},
            'day': {'$dayOfMonth': '$dt'}
        }, '%Y-%m-%dT00:00:00'
    elif group_type == 'month':
        return {
            'year': {'$year': '$dt'},
            'month': {'$month': '$dt'}
        }, '%Y-%m-01T00:00:00'
    else:
        raise ValueError('Invalid group_type')


def get_format_data(date_format, result_index, results):
    year = results[result_index]['_id']['year']
    month = results[result_index]['_id'].get('month', 1)
    day = results[result_index]['_id'].get('day', 1)
    hour = results[result_index]['_id'].get('hour', 0)
    result_date = datetime(year, month, day, hour).strftime(date_format)
    return result_date


def add_month(start_date: datetime) -> datetime:
    month = start_date.month
    year = start_date.year + month // 12
    month = month % 12 + 1
    day = min(start_date.day, [31, 29 if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0 else 28, 31, 30, 31,
                               30, 31, 31, 30, 31, 30, 31][month - 1])
    return datetime(year, month, day, start_date.hour)


def get_dt_delta(group_type: str) -> timedelta:
    if group_type == 'hour':
        delta = timedelta(hours=1)
    elif group_type == 'day':
        delta = timedelta(days=1)
    elif group_type == 'month':
        delta = timedelta(days=30)
    else:
        raise ValueError('Invalid group_type')
    return delta
