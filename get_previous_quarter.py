import datetime
import calendar

def get_previous_quarter_range(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp)
    quarter = (dt.month - 1) // 3 + 1
    # year = dt.year if quarter != 1 else dt.year - 1
    year = dt.year
    if quarter == 1:
        start_month = 10
        start_year = year - 1
    else:
        start_month = ((quarter - 2) * 3) + 1
        start_year = year
    start_dt = datetime.datetime(start_year, start_month, 1)
    end_dt = start_dt.replace(month=start_dt.month+2, day=calendar.monthrange(start_dt.year, start_dt.month+2)[1], hour=23, minute=59, second=59)

    start_timestamp = int(start_dt.replace(tzinfo=datetime.timezone.utc).timestamp())
    end_timestamp = int(end_dt.replace(tzinfo=datetime.timezone.utc).timestamp())
    start_date = start_dt.strftime("%B %d, %Y")
    end_date = end_dt.strftime("%B %d, %Y")
    return start_timestamp, end_timestamp, start_date, end_date


timestamp_example = input()
timestamp_example = datetime.datetime.timestamp(datetime.datetime.strptime(timestamp_example, '%Y-%m-%d'))
start_timestamp,end_timestamp, start_date, end_date = get_previous_quarter_range(timestamp_example)

print(f"  Start date of two months ago: {start_date} (timestamp: {start_timestamp})")
print(f"  End date of previous month: {end_date} (timestamp: {end_timestamp})")
