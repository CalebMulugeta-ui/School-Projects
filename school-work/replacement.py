list = []
while True:
    userNumbers = int(input("Enter a number between 1-10, enter -1 to finish: "))
    if userNumbers == -1:
        break
    list.append(userNumbers)


while True:
    userInput = input("Enter a number to change ['q' to quit]>> ").lower()
    if userInput == 'q':
        break
    numChange = int(userInput)
    stringChange = input("with string >> ")
    for e in list:
        if e == numChange:
            index = list.index(e)
            list.insert(index,stringChange)
            list.remove(e)
    print(list)