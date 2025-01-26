usersNumber = int(input("Enter a number (1-9): "))

for coloumns in range(1, usersNumber+1):
    for rows in range(1, usersNumber+1):
        print(rows * coloumns, end = '\t')
    print()