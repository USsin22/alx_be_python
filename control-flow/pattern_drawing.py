
size = int(input("Enter the size of the pattern: "))

row = 0

# While loop for rows
while row < size:
    # For loop for columns
    for col in range(size):
        print("*", end="")
    print()
    row += 1
