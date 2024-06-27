calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_seconds} {name_of_unit}"


def validate_and_execute():
    try:
        num_of_days = int(input("Enter the number of days and I will convert it to hours!"))

        if num_of_days > 0:
            print(days_to_units(num_of_days))
        elif num_of_days == 0:
            print("You entered 0, Please enter valid number of days!")
        elif num_of_days < 0:
            print("You entered a negative value, Please enter valid number of days!")
    except ValueError:
        print("Your input is not a number!!!")


validate_and_execute()
