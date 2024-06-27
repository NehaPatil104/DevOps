# * * * *
#   * * *
#     * *
#       *

n = int(input("Enter the number of rows: "))

# for i in range(1, n + 1):
#     for j in range(1,i):
#         print("  ", end="")
#     for j in range(i, n + 1):
#         print("* ", end="")
#     print()

for i in range(0, n):
    print("  " * i, end="")
    print("* " * (n-i), end="")
    print()