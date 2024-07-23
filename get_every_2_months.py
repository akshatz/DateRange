import datetime
import argparse


def get_every_two_months(timestamp):
    current_date = datetime.datetime.fromtimestamp(timestamp)
    current_year = current_date.year
    # Calculate the start date of the current interval
    if current_date.month == 1:
        end_month = 11
        start_year = current_date.year - 1
        start_date = current_date.replace(day=1, month=11, year=start_year)
        start_month = 11
    elif current_date.month == 2:
        start_year = current_date.year - 1
        start_date = current_date.replace(day=1, month=12, year=start_year)
    else:
        end_month = current_date.month - 1
        start_date = current_date.replace(day=1, month=end_month - 1, year=current_date.year)
    start_month = start_date.month
    # Calculate the end day of the current interval
    month_numbers = [5, 7, 8, 10, 12]
    end_year = current_year
    if current_date.month in month_numbers:
        end_day = 30
        end_month = current_date.month - 1
        end_year = current_date.year
        if current_date.month == 8:
            end_day = 31
            end_month = current_date.month - 1
            end_year = current_date.year
    if current_date.month == 3:
        end_month = current_date.month -1
        if current_year % 4 == 0 and current_year % 100 != 0:
            end_day = 29
        else:
            end_day = 28
    if current_date.month in [4, 6, 9, 11]:
        end_day = 31
        end_month =current_date.month -1
        end_year = current_date.year
    if current_date.month -1 == 0:
        end_month = 12
    if current_date.month == 1:
        end_day = 31
        end_month = 12
        end_year = current_year - 1
    if current_date.month == 2:
        end_month = 1
        end_day = 31
        end_year = current_date.year
    end_date = start_date.replace(day=end_day, month=end_month, year=end_year, hour=23, minute=59, second=59)

    # Format the dates as strings
    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())
    start_date_obj = datetime.datetime.fromtimestamp(start_timestamp)
    start_date = start_date_obj.strftime('%B %d, %Y')
    end_date_obj = datetime.datetime.fromtimestamp(end_timestamp)
    end_date = end_date_obj.strftime('%B %d, %Y')
    return start_timestamp, end_timestamp, start_date, end_date

# Example usage
timestamp_example = input()
timestamp_example = datetime.datetime.timestamp(datetime.datetime.strptime(timestamp_example, '%Y-%m-%d'))
start_timestamp,end_timestamp, start_date, end_date  = get_every_two_months(timestamp_example)

print(f"  Start date of two months ago: {start_date} (timestamp: {start_timestamp})")
print(f"  End date of previous month: {end_date} (timestamp: {end_timestamp})")
