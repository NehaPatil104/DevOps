# First floor 
# Third Kids

age = 40

if age > 25:
    print("First Floor")
elif age >= 18:
    print("Second Floor")
else:
    print("Sorry. You are kiddo!. Third Floor")  


# and => First falsy value => Last Truthy value
# or => First truthy value => Last Falsy value
print("" and 0 or "a" and False) # False
print("" and 0 or "a" and "abcd") # abcd
print("" and 0 and "a" and "abcd") # ""
print("" or 0 or "a" or "abcd") # a


print([] or "abcd") # abcd
print([] and "abcd") # []
print([] or not "abcd") # []
