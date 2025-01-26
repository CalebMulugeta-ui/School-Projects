def printLists(customerList):
    """ Function Description:
            Prints the customer informations
        Parameter(s): 
            customerList [list]: The list of the customers information
            
        Return:  
            none
    """

    for i in customerList:
        printIndividualList(i)

    return

def printIndividualList(customer):

    """ Function Description:
            Outputs certain message depending on the users customer status (G, S, B)
        Parameter(s):
            customer [list]: list of users information
        Return: none
    """

    dis1 = customer[2] * (10/100)
    dis2 = customer[2] * (5/100)
    dis3 = customer[2] * (2/100)
    total1 = customer[2] - dis1
    total2 = customer[2] - dis2
    total3 = customer[2] - dis3
    if "G" in customer:
        print(f"{customer[0]} has a gold discount statous of 10%, order of {customer[2]} is discounted {dis1:.2f} for a final total of {total1:.2f}")
        print()
    elif "S" in customer:
        print(f"{customer[0]} has a silver discount statous of 5%, order of {customer[2]} is discounted {dis2:.2f} for a final total of {total2:.2f}")
        print()
    elif "B" in customer:
        print(f"{customer[0]} has a bronze discount statous of 2%, order of {customer[2]} is discounted {dis3:.2f} for a final total of {total3:.2f}")
        print()
    return

def main():
    customerRecords = [["Sean Benjamin", "B", 30.22], ["Yanan Mao", "G", 40.22],  ["Charlie Brown", "S", 22.30], ["Snoopy Dog", "G", 69.33], ["Woodstock Bird", "S", 25.00]]
    printLists(customerRecords)

if __name__ == '__main__':
    main()