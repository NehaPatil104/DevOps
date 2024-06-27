def outer(func):
    print("outer")
    def middle():
        print("middle")
    return middle

# message = outer(message)

@outer
def message():
    print("message")

# message = middle

message()
message()