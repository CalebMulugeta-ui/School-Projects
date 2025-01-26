''' 
    COMP 1005/1405 Section A - Assighnment 5 - Problem 3
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
        The purpose of this function is to separate a list of integers 
        into negative and non-negative numbers, sort these lists in both ascending 
        and descending order, and display the results.
    Parameters:
        None
    Return:
        None
    """

    integerList = [12, -7, 3, -45, 22, 8, 0, -13, 19, -21, 5, -9, -11, 15, 30, -33,-4, 7, 25, -2]
    seperated_list = separate_numbers(integerList)
    negList = seperated_list[0] 
    nonNeglist = seperated_list[1]

    
    print(f'Original List: {integerList}')
    print(f'non-Negative Asceding: {bubble_sort(nonNeglist, True)}')
    print(f'non-Negative Descending: {bubble_sort(nonNeglist, False)}')
    print(f'Negative Ascending: {bubble_sort(negList, True)}')
    print(f'Negative Descending: {bubble_sort(negList, False)}')


def separate_numbers(aList):
    """
    Function Description:
        The purpose of this function is to separate the input list into two lists,
        one with negative numbers and the other with non-negative numbers.
    Parameters:
        aList (list): A list of integers.
    Return:
        tuple: A tuple containing two lists:
               - neg (list): A list of negative numbers.
               - nonNeg (list): A list of non-negative numbers.
    """
    neg = []
    nonNeg = []
    for i in range(0,len(aList)):
        if aList[i] < 0:
            neg.append(aList[i])
        else:
            nonNeg.append(aList[i])
    return neg, nonNeg

def bubble_sort(aList, ascending):
    """
    Credit to Sean Benjamin & Yanan Mao from COMP 1005/1405 - Lecture 18 Bubble Sort
    Function Description:
        The purpose of this function is to separate the input list into two lists: 
        one containing negative numbers and the other containing non-negative numbers.
    Parameters:
        aList (list): A list of integers.
    Return:
        tuple: A tuple containing two lists:
               - neg (list): A list of negative numbers.
               - nonNeg (list): A list of non-negative numbers.
    """

    if ascending == True: #Small to Big
        n = len(aList)
        for i in range(n):
            # Flag to check if any swapping happened in this pass
            swapped = False
            for j in range(0, n - i - 1):
                if aList[j] > aList[j + 1]:
                    # Swap the elements
                    temp = aList[j]             # Temporarily store arr[j]
                    aList[j] = aList[j + 1]       # Move arr[j + 1] to arr[j]
                    aList[j + 1] = temp 
                    swapped = True
            # If no swapping happened, the list is already sorted
            if not swapped:
                break
        return aList
    else:
        for i in range(0, len(aList)):
            # Flag to check if any swapping happened in this pass
            swapped = False
            for j in range(0, (len(aList)) - i - 1):
                if aList[j] < aList[j + 1]:
                    # Swap the elements
                    temp = aList[j]             # Temporarily store arr[j]
                    aList[j] = aList[j + 1]       # Move arr[j + 1] to arr[j]
                    aList[j + 1] = temp 
                    swapped = True
            # If no swapping happened, the list is already sorted
            if not swapped:
                break
        return aList
  
main()