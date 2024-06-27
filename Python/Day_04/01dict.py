arr = [
    {"name" : "xyz"},
    {"name" : "abc"},
    {"name" : "xyz"}
]
print(arr)
arr.pop(1)
print(arr)
arr[1] = {"name" : "neha"}
print(arr)
arr.remove({"name" : "xyz"})
print(arr)

odd = [1, 3, 5]
even = [2, 4, 6]

odd_even = [*odd, *even]
print(odd_even)

print("Deep Copy")
import copy

persons = [
    {"name" : "xyz"},
    {"name" : "abc"},
    {"name" : "lmn"}
]

people = copy.deepcopy(persons)
print(people)
print(persons)
people.remove({"name" : "abc"})
print(people)
print(persons)

person = {
    "name": "Neha",
    "age": 22
}

def print_dict(name, age):
    print(f"I am {name}, {age} years old.")

print_dict(**person)