
def checkError(number):
    """
    Function Desciptions:
        The purpose of this function is to check the inputed number and print out statments or generate the Tree
    Parameters:
        number(int): The height of the tree
    Return: 
        None
    """

    #Checks if users height is within the range, if not, it prints out certain message
    if number < 2:
        print("Looks like we've got a baby tree here not quite ready for Christmas cheer.")
    if number > 10:
        print("Whoa, that tree is too big for my cozy living room. Let's find one that fits just right ")
    #If users heigh is within range it generates the Tree
    if number >= 2 and number <= 10:
        generateTree(convertedHeight)


def generateTree(layers):
    """
    Function Desciptions:
        The purpose of this function is to generate and print out tree based on the given height
    Parameters:
        layers(int) : The height of the tree
    Return: 
        None
    """

    #For loop that creates the spaces and the tree
    for i in range(0,layers):
        stars = 2 * i + 1
        spaces = layers - i - 1
        print(' '* spaces, '*' * stars)
    print(' '*(layers - 1), '|')

#Get the user inputs and quits the program if user enters 'q'
while True:
    userHeight = input("Enter desired height for tree [q to quit]: ").lower()
    if userHeight == "q":
        break
    convertedHeight = int(userHeight)
    checkError(convertedHeight)
    