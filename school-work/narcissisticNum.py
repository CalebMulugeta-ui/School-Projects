''' 
    COMP 1005/1405 Section A 
    Project Details
        Name: Caleb Mulugeta
        Student #: 101352144
        Date: October 19, 2024
    
    External Libraries Used
        None    
'''

#Start a loop that continues as long as flag is true
flag = True
while flag:
    num1 = int(input("Enter 1st 3 Digit number: "))
    num2 = int(input("Enter 2nd 3 Digit number: "))

    #Checks if either of the enterned numbers are not 3 digits
    if (num1 < 100 or num1 > 999) or (num2 < 100 or num2 > 999):
        print("ERROR")
    else:

        #Loops from users first number to users second number
        for i in range(num1, num2):
            #Calculates if current number is narcissistic or not
            firstNum = i % 10 
            remove1 = i // 10 
            secondNum = remove1 % 10 
            thirdNum = remove1//10 
            addedNums = (firstNum**3) + (secondNum**3) + (thirdNum**3)
            #Prints the number if it is narcissistic
            if addedNums == i:
                print(i)
    
    #Ask the user if they want try a new range, depending on input, the program will start again or end
    userChoice=input("Do you want to try anohter Range? (Yes or No): ")
    upper = userChoice.upper()
    if upper == "YES":
        flag = True
    else: 
        flag = False