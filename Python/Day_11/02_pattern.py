# * * * *
# * * *
# * *
# *

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(i, n + 1):
        print("* ", end="")
    print()