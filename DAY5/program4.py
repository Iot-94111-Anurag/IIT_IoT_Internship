import datetime

current_date_time = datetime.datetime.now()
print(f"current date and time = {current_date_time}")

day_of_week = current_date_time.strftime("%A")

print(f"current day is {day_of_week}")