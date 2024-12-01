from datetime import date, datetime, timedelta

def datetime_by_format(datetime_srt, datetime_format):
    return datetime.strptime(datetime_srt, datetime_format)

def days_ago(days_count):
    return date.today() - timedelta(days=days_count)
