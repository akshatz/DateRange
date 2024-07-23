import datetime

def get_previous_month_range(timestamp):
    # Convert the given timestamp to a datetime object in the UTC timezone
    dt_utc = datetime.datetime.fromtimestamp(timestamp)
    if dt_utc.month == 1:
        first_day_of_previous_month = dt_utc.replace(day=1) - datetime.timedelta(days=31)
    # Calculate the first day of the previous month
    if dt_utc.month in [3, 5, 7, 8, 10, 12]:
        if dt_utc.month == 8:
            first_day_of_previous_month = dt_utc.replace(day=1) - datetime.timedelta(days=31)
        else:
            first_day_of_previous_month = dt_utc.replace(day=1) - datetime.timedelta(days=30)
        if dt_utc.month == 3:
            if (dt_utc.year % 4 == 0) and (dt_utc.year % 100 !=0):
                end_day = 29
            else:
                end_day =28
            first_day_of_previous_month = dt_utc.replace(day=1) - datetime.timedelta(days=end_day) 
    elif dt_utc.month in [4, 6, 9, 11]:
        first_day_of_previous_month = dt_utc.replace(day=1) - datetime.timedelta(days=31)
    elif dt_utc.month == 2:
        if (dt_utc.year % 4 == 0) and (dt_utc.year % 100 != 0):
            first_day_of_previous_month = dt_utc.replace(day=1) - datetime.timedelta(days=31)
        else:
            first_day_of_previous_month = dt_utc.replace(day=1) - datetime.timedelta(days=31)
    elif dt_utc.month == 3:

        first_day_of_previous_month = dt_utc.replace(day=1)
    if first_day_of_previous_month.month in [1, 3, 5, 7, 8, 10, 12]:
        last_day_of_previous_month = first_day_of_previous_month.replace(day=31, hour=23, minute=59, second=59)
    elif first_day_of_previous_month.month in [4, 6, 9, 11]:
        last_day_of_previous_month = first_day_of_previous_month.replace(day=30, hour=23, minute=59, second=59)
    elif first_day_of_previous_month.month == 2:
        if (first_day_of_previous_month.year % 4 == 0 and first_day_of_previous_month.year % 100 != 0):
            last_day_of_previous_month = first_day_of_previous_month.replace(day=29, hour=23, minute=59, second=59)
        else:
            last_day_of_previous_month = first_day_of_previous_month.replace(day=28, hour=23, minute=59, second=59)
    # Calculate the last day of the previous month without using the calendar module
    start_timestamp = int(first_day_of_previous_month.replace(tzinfo=datetime.timezone.utc).timestamp())
    end_timestamp = int(last_day_of_previous_month.replace(tzinfo=datetime.timezone.utc).timestamp())

    # Format the dates as strings
    start_date = first_day_of_previous_month.strftime("%B %d, %Y")
    end_date = last_day_of_previous_month.strftime("%B %d, %Y")

    return start_timestamp, end_timestamp, start_date, end_date

timestamp_example = input()
timestamp_example = datetime.datetime.timestamp(datetime.datetime.strptime(timestamp_example, '%Y-%m-%d'))
start_timestamp,end_timestamp, start_date, end_date  = get_previous_month_range(timestamp_example)

print(f"  Start date of two months ago: {start_date} (timestamp: {start_timestamp})")
print(f"  End date of previous month: {end_date} (timestamp: {end_timestamp})")
