# Data Types
print("Neha")  # String
print(10)  # int
print(10.7)  # float

# Arithmetic operations
print(20 * 24 * 60)

# String Concatenation
# Way 1
print("20 days are " + str(20 * 24 * 60) + " minutes")
# Way 2
print(f"20 days are {str(20 * 24 * 60)} minutes")
print(f"20 days are {str(20 * 24 * 60 * 60)} seconds")

# Variables
calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"
print(f"One day has {calculation_to_seconds} {name_of_unit}")
print(f"20 days are {20 * calculation_to_seconds} {name_of_unit}")


# Functions
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_seconds} {name_of_unit}"


days_to_units(7)
days_to_units(2)
days_to_units(1)


# Scope
def scope_check():
    my_var = "Variable inside function"
    print(name_of_unit)  # Global variable
    # print(num_of_days) => Error => Variable local to function


def validate_and_execute():
    # User Input
    num_of_days = input("Enter the number of days and I will convert it to hours!")

    # Conditional Statements
    if num_of_days.isdigit():
        num_of_days = int(num_of_days)
        if num_of_days == 0:
            print(days_to_units(num_of_days))
        else:
            return "Please enter valid number of days!"
    else:
        print("Your input is not a number!!!")


validate_and_execute()
