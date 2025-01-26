import displayCustomer

def createRecord():
    """ Function Description:
            This function takes in the name, discount type, and total cost enterd by the user and outputs a certian message depeding on thier inputs
        Parameter(s):
            none
        Return [list]: returns a list with the info enterd by user
    """

    customerInfo = []
    name = input("Input customer name: ")
    customerInfo.append(name)
    disType = input("Input discount type (G, S, B): ").upper()
    customerInfo.append(disType)
    cost = float(input("Input total cost: "))
    customerInfo.append(cost)

    return customerInfo

def main():
    numRecords = int(input("How many customer records do you want to insert: "))

    customerLists = []
    for i in range(0, numRecords):
        returned = createRecord()
        customerLists.append(returned)
    displayCustomer.printLists(customerLists)

if __name__ == '__main__':
    main()

