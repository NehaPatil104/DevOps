# String => '', "", ''' ...''', """ ..."""
# Strings are immutable

# String concatenation
str1 = "Hello"
str2 = "Neha"
result = str1 + " " + str2
print(result)
print(f"{str1} {str2}")

# length
print("Length: ", len(str1))

# lowercase
lowercase = str1.lower()
print("Lowercase: ", lowercase)
print(str1)

# replace
text = "Good. Morning!"
print("Replace: ", text.replace("Morning", "Night"))

# split
words = text.split(".")
print("Split: ", words)
print("Type of words: ", type(words))

# strip
text = "  hello  hiii "
stripped_text = text.strip()
print("Strip: ", stripped_text)

# substring
substring = "hiii"
if substring in text:
    print(substring, "found in the text!")

#capitalize
print("Capitalize: ", substring.capitalize())

# find => returns lowest index in the string where substring is found
print("Find: ", text.find("hiii"))

# count
print("Count: ", text.count("h"))

# join
myTuple = ("Neha", "Patil", "Coditas")
myStr = " ".join(myTuple)
print("Join: ", myStr)


# DAMPING FUCTIONS 
sentence = "This is a  sentence"
print(len(sentence))
print(sentence.__len__())
print(str.__len__(sentence))

#Slicing
    #   654321 
word = "bottle"
#1 => btl
print(word[0:5:2])
print(word[-6:-1:2])
print(word[0:-1:2])
print(word[-6:5:2])
#2 =>tle
print(word[3:6])
print(word[-3:6])
print(word[-3:])
#3 => ltb
print(word[-2::-2])
print(word[4:-7:-2])
print(word[4::-2])
print(word[-2:-7:-2])

print(word[-1:-6:2])

