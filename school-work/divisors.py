''' 
    COMP 1005/1405 Section A 
    Project Details
        Name: Caleb Mulugeta
        Student #: 101352144
        Date: October 19, 2024
    
    External Libraries Used
        None    
'''

def findDivisor():
        """
    Function Description:
        Finds and display all the divisor of the users input
    Parameters:
        None
    Return:
        None
    """
        #Initilizes an empty list to store the divisors in
        divisor = []
        userNum = int(input("Enter a number to get its divisors: "))
        #Loops from 1 to the entered number (inclusive) to find the divisors
        for i in range(1, userNum+1):
                if userNum % i == 0:
                        #appends the divisors
                        divisor.append(i)
        print(f"The divisors of {userNum} are: {divisor}")
findDivisor()