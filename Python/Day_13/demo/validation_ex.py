name = "Neha"
password = "dafdaf32s1233f"

def validate_input(input, *validations):

    for validator in validations:
        if validator(input):
            return True
    return False


def is_type(data_type):
    return lambda input : type(input) == data_type

def has_length(length):
    return lambda input: len(input) == length

validations_dict = {
    "is_string": is_type(str),
    "is_integer": is_type(int),
    "has_length": has_length
}

print(validate_input(name, validations_dict['has_length'](4), validations_dict["is_string"]))
print(validate_input(password, validations_dict['has_length'](10)))