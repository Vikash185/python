rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("*", end=" ")
    print()  # Move to the next line after each row
