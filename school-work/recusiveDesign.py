''' 
    COMP 1005/1405 Section A - Assighnment 5 - Problem 1
    Project Details
        Name: Caleb Mulugeta
        Student #: 101352144
        Date: December 6, 2024
    
    External Libraries Used
        None    
'''


def main():
    """
    Function Description:
        The purpose of this function is to let the user to input a list 
        of numbers, compute the sum of even and odd numbers 
        both recursive and non-recursive methods, and display the results. 
    Parameters:
        None
    Return:
        None
    """
    while True:
        numList = []
        while True:
                userInput = input('Enter a Number to add to list or "quit" to exit:  ').lower()
                if userInput == 'quit':
                    break
                try:
                    userNum = int(userInput)
                    numList.append(userNum)
                except ValueError:
                    print('Please Enter a Vaild Number.')

                    
        nonRecursiveEven = sum_of_evens_non_recursive(numList)      
        nonRecursiveOdd = sum_of_odds_non_recursive(numList)
        recursiveEven = sum_of_evens_recursive(numList)
        recursiveOdd = sum_of_odds_recursive(numList)
        

        print('\nSum of Lists Even & Odd: ')
        print(f'Sum of Evens (non-Recursive): {nonRecursiveEven}')
        print(f'Sum of Odds (non-Recursive): {nonRecursiveOdd}')
        print(f'Sum of Even (Recursive): {recursiveEven}')
        print(f'Sum of Odds (Recursive): {recursiveOdd}')

        userChoice = input('Do you want to conintue (Y/N): ').upper()
        if userChoice == 'N':
            break
        else:
            continue


def sum_of_evens_non_recursive(list):
    """
    Function Description:
        The purpose of this function  is to take the sum of all
        even numbers, non-recursively
    Parameters:
        list(list): list of numbers
    Return:
        sum(int): sum of even numbers
    """ 
    sumOfEven = 0
    for i in list:
        if i%2 == 0:
            sumOfEven += i
    return sumOfEven

def sum_of_odds_non_recursive(list):
    """
    Function Description:
        The purpose of this function  is to take the sum of all
        odd numbers, non-recursively
    Parameters:
        aList(list): list of numbers
    Return:
        sum(int): sum of odd numbers
    """ 
    sumOfOdd = 0
    for i in list:
        if i%2 != 0:
            sumOfOdd += i
    return sumOfOdd


def sum_of_evens_recursive(list):
    """
    Function Description:
        The purpose of this function is to calculate the sum of all 
        even numbers in the input list, recursively.
    Parameters:
        list(list): A list of integers
    Return:
        sum(int): Sum of all even numbers in the list
    """

    evenNums = []
    for i in range(len(list)):
        if list[i]%2 == 0:
             evenNums.append(list[i])
    if evenNums == []:
        return 0
    #Base Case
    if len(evenNums) == 1:
         return evenNums[0]
    
    return evenNums[0] + sum_of_evens_recursive(evenNums[1:])


def sum_of_odds_recursive(list):
    """
    Function Description:
        The purpose of this function is to calculate the sum of all 
        odd numbers in the input list, recursively.
    Parameters:
        list(list): A list of integers
    Return:
        sum(int): Sum of all odd numbers in the list
    """
    oddNums = []
    for i in range(len(list)):
        if list[i]%2 != 0:
             oddNums.append(list[i])

    if oddNums == []:
        return 0

    #Base Case
    if len(oddNums) == 1:
         return oddNums[0]
    
    return oddNums[0] + sum_of_odds_recursive(oddNums[1:])

main()