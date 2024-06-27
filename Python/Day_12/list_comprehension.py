# # list comprehension
# squares = [(num, num * num) for num in range(1, 11)]
# print(squares)

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]

# # nested list comprehension
# matrix_transpose = [[row[i] for row in matrix] for i in range(0, 4)]
# print(matrix_transpose)

arr_list = [[1,2,3], [4,5], [6, 7, 8, 9]]
# flatten_list = [[col for col in len(arr_list[row])] for row in len(arr_list)]  
# print(flatten_list)


#print([value for array in arr_list for value in array])
arr_list = [[1,2,3], [4,5], [6, 7, 8, 9]]
#

print([[value for value in inner_list if value%2==0] for inner_list in arr_list])

#prime numbers from 30 to 40

prime_numbers = [[number for i in range(2, number) if number%i==0 ] for number in range(30, 41)]
print(prime_numbers)

people = [
    {"name": "Alice", "friend_list": ["Bob", "Charlie"], "age": 30, "location": {"city": "New York", "country": "USA"}},
    {"name": "Bob", "friend_list": ["Alice", "David"], "age": 25, "location": {"city": "London", "country": "UK"}},
    {"name": "Charlie", "friend_list": ["Alice", "Emily"], "age": 28, "location": {"city": "Paris", "country": "France"}},
    {"name": "David", "friend_list": ["Bob", "Emily"], "age": 32, "location": {"city": "Berlin", "country": "Germany"}},
    {"name": "Emily", "friend_list": ["Charlie", "David"], "age": 27, "location": {"city": "Madrid", "country": "Spain"}},
]

#friend = Alice location = Paris

get_people = [dict["name"] for dict in people if "Alice" in dict["friend_list"] and dict["location"]["city"] == "Paris"]
print(get_people)

