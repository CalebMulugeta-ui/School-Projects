#COMP 1005/1405 Section [A] - Assignment [1] Program [2]
#Project Details
    #Name: Caleb Mulugeta
    #Student #: 101352144
    #Date Created: [Septemper 26th]

#Get the user input value
userValue = float(input("Enter a value between 0.0 and 1.0: "))

#Evalutes the users grade based on thier input
if 0.0 <= userValue < 0.6:
    print("Grade: F") 

if 0.7 > userValue >= 0.6:
    print("Grade: D")

if 0.8 > userValue >= 0.7:
    print("Grade: C")

if 0.9 > userValue >= 0.8:
    print("Grade: B")

if 1.0 >= userValue >= 0.9:
    print("Grade: A")

#If users input isnt within range
if userValue < 0.0:
    print("Error")

if userValue > 1.0:
    print("Error")
