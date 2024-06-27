name = "Neha"
password = "Neha@123"

# Checks if input is empty
def isEmpty(parameter):
    if len(parameter) == 0:
        return True
    return False

# Checks min length
def is_length(parameter):
    if len(parameter) < 15:
        return False
    return True

def is_atleat_on_char_uppercase(password):
    for ch in password:
        if (ch >= 'A' and ch <= 'Z'):
            return True

# Validates password
def validate_password(password):
    if isEmpty():
        return False 
    
    if is_length(password):
        return False
    
    if is_atleat_on_char_uppercase(password):
        return True
    
    return True

# Validates name
def validate_name(name):
    if isEmpty():
        return False



def validate_input(name, password):
    if validate_password(password) and validate_name(name):
        return True
    return False
    
    

        

