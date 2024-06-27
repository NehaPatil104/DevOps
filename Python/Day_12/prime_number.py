# next prime number

def is_prime(num):
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True

def next_prime(n + 1):
    while is_prime(n):

n = 7
print(is_prime(n))

print(next_prime(n+1))

