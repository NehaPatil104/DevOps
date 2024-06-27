from datetime import datetime
# check if user has enough permissions

def log_time(config):
    def lt(func):
        def inner(*args):
            if len(config) > 2:
                print(datetime.now())
                return func(*args)
            return "INVAlID"
        return inner
    return lt

@log_time([2,4, 7,6])
def user_list(user_name):
    print("This is user list...")
    print(user_name)
    return True

@log_time([2, 3, 1])
def product_list():
    print("This is products list...")
    return False


print(user_list("Neha")) 
print(product_list())