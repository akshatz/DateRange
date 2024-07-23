import datetime
from dateutil.relativedelta import relativedelta, MO, FR, SU
from datetime import timedelta

def get_previous_week(timestamp):
    input_datetime = datetime.datetime.fromtimestamp(timestamp)

    # Subtract 7 days from the input date
    input_datetime -= datetime.timedelta(days=7)
    if input_datetime.weekday() == 0:
        start_date = input_datetime + relativedelta(weekday=MO(-1))
        end_date = start_date + relativedelta(weekday=SU(1))
        print(start_date, end_date)
    else:
        start_date = input_datetime + relativedelta(weekday=MO(-1))
        end_date = start_date + relativedelta(weekday=SU(1))

    start_date = start_date.replace(hour=0, minute=0, second=0)
    # if input_datetime.weekday() == 4:
    #     input_datetime -= datetime.timedelta(days=7)
    #     start_date = input_datetime + relativedelta(weekday=MO(-1))
    #     end_date = input_datetime + relativedelta(weekday=SU(1))

    # Set the time to 23:59:59 for Friday
    end_date = end_date.replace(hour=23, minute=59, second=59)
    # Convert to timestamp
    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())
    # Convert to required 
    start_date = start_date.strftime('%B %d, %Y')
    end_date = end_date.strftime('%B %d, %Y')
    
    return start_date, end_date, start_timestamp, end_timestamp

# Example usage
timestamp_example = input()
timestamp_example = datetime.datetime.timestamp(datetime.datetime.strptime(timestamp_example, '%Y-%m-%d'))
start_date, end_date, start_timestamp, end_timestamp = get_previous_week(timestamp_example)

print(f"  Start date of previous week: {start_date}(timestamp: {start_timestamp})")
print(f"  End date of previous week: {end_date} (timestamp: {end_timestamp})")
