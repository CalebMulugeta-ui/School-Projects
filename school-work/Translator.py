
#COMP 1005/1405 Section [A] - Assignment [1] Program [3]
#Project Details
    #Name: Caleb Mulugeta
    #Student #: 101352144
    #Date Created: [Septemper 27th]


#Get User Inputs
userString = input("Enter a string: ")
userValue = int(input("Enter a shift value:"))

#Make user string uppercase
stringUpper = userString.upper()

#Gets encoded message
finalMessage = ''
for u in stringUpper:
    numbers = int(ord(u[:1:])) #Changes the words into numbers
    if numbers > 64 and numbers < 91: #Changes postition of Numbers
        newNumber = (numbers+userValue)
        if newNumber > 90:
            newNumber -= 26 #Loops number back to 26 numbers if they go over 90
        finalMessage += chr(newNumber) 
    else:
        finalMessage += (chr(numbers))
print(finalMessage)