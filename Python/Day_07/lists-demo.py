# Lists are mutable
s3_bucket_list = ["neha_bucket", "js_bucket", "mongo_bucket", "img_bucket"]
print(s3_bucket_list)

print(type(s3_bucket_list))

# Append => Adding to list
s3_bucket_list.append("scirpt_bucket")
print(s3_bucket_list)

# Remove
s3_bucket_list.remove("neha_bucket")
print(s3_bucket_list)

# Accessing elements in list
print(s3_bucket_list[0]) # first element
print(s3_bucket_list[-1]) # last element

# Length
print("Length: ", len(s3_bucket_list))

# Slicing
new_list = s3_bucket_list[1:]
print("New list: ", new_list)

# Sort
numbers = [32, 5, 0]
numbers.sort()
print("Sort: ", numbers)

# Reverse
numbers.reverse()
print("Reverse: ", numbers)

# Insert at position
numbers.insert(2, 40)
print("Insert: ", numbers)

# Pop => Pops last element if position not specified
numbers.pop();
print("Pop: ", numbers)

# Clear
numbers.clear()
print("Clear: ", numbers)

# Count
numbers = [32, 5, 0, 5, 1, 5]
print("Count: ", numbers.count(5))