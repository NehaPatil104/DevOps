# Pattern Matching

import re

# search, match
text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)

if(search):
    print("Pattern found: ", search.group())
else:
    print("Pattern not found")

# replace
text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)  

# split

import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)