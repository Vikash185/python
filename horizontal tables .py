# Pyramid of horizontal tables of numbers
rows = 10
rows = 10
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i * j, end=' ')
    print()
