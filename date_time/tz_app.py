import pytz
from datetime import datetime

# 
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

# local_timezone = pytz.timezone('America/New_York')
local_timezone = pytz.timezone('US/Pacific')
print(local_timezone)

localized_time = current_datetime.astimezone(local_timezone)

print("Local Time (LA):", localized_time)