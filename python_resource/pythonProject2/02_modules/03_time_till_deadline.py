# Module is a python file
# Package is a collection of modules i.e python files
import datetime

user_input = input("Enter your goal with a deadline, separated by colon: \n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_date - today_date
print(f"Time remaining for your goal is => {time_till.days} days")
print(f"Time remaining for your goal is => {int(time_till.total_seconds() / 60 / 60)} hours")
