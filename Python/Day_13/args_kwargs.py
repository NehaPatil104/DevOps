# args => any number of arugments, those are stored in tuple
# kwargs => keyword-args, any number of arguments, stored in dictionary
def my_func(*args,**kwargs):
    print(args)
    print(kwargs)


my_func(1, 2, 3, a=3, b=4, name="Neha")