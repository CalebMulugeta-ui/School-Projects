''' 
    COMP 1005/1405 Section A 
    Project Details
        Name: Caleb Mulugeta
        Student #: 101352144
        Date: October 19, 2024
    
    External Libraries Used
        None    
'''

#Initilizes an empty list to store the divisors in
divisor = []
userNum = int(input("Enter a number between 1 and 30: "))

#Loops from 1 to the entered number (inclusive) to find the divisors
for i in range(1, userNum+1):
        if userNum % i == 0:
                #appends the divisors
                divisor.append(i)

#Checks if the divisors meets the conditon to be a prime number or not
if divisor == [1, userNum]:
        print(f"{userNum} is a prime number")
else:
        print(f"{userNum} is not a prime number")



