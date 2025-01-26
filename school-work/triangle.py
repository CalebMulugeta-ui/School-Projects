userRows = int(input("Enter number of row: "))

num = 0
for colouns in range(0, userRows):
    num += 1
    for rows in range(0, num):
        print(num, end='')
    print()