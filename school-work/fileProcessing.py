''' 
    COMP 1005/1405 Section A - Assighnment 5 - Problem 2
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
        The purpose of this function is to load recipe data from a CSV file, display 
        the data, extract the secret ingredient information, and display it in a dictionary format.
    Parameters:
        None
    Return:
        None
    """
    recipe_data = loadData()
    displayList(recipe_data)
    secret_ingredient_dict = getSecretIngredient(recipe_data)
    displayDict(secret_ingredient_dict)


def loadData():
    """
    Function Description:
        The purpose of this function is to load recipe data from a CSV file. 
        Each line in the CSV file is read and stored as a list of recipes.
    Parameters:
        None
    Return:
        recipe_data (list): A list of lists, where each inner list represents a recipe with its details.
    """

    while True:
        userCSV = input('Enter file name of the CSV file containing recipes: ')
        try:
            with open(userCSV, 'r') as file:
                line = file.readline()
                recipe_data = []
                while line != "":
                    seperated = line.strip().split(',')
                    recipe_data.append(seperated)
                    line = file.readline()
                recipe_data.pop(0)
                return recipe_data
        except FileNotFoundError:
            print('File Not Found')
            continue


def displayList(listOfList):
    """
    Function Description:
        The purpose of this function is to display the contents of a list of lists, 
        where each inner list represents a recipe. If the list is empty, a message is displayed.
    Parameters:
        listOfList (list): A list of lists containing recipe data.
    Return:
        None
    """
    if listOfList == []:
            print('List is empty')
    for i in listOfList:
        print(i)


def getSecretIngredient(recipe_data):
    """
    Function Description:
        The purpose of this function is to create a dictionary of secret ingredients, 
        each key is a secret ingredient and the value is a list IDs containing that ingredient.
    Parameters:
        recipe_data (list): A list of lists containing recipe details.
    Return:
        secret_ingredient_dict (dict): A dictionary for each secret ingredient to the list of recipe IDs.
    """
    secret_ingredient_dict = {}
    for list in recipe_data:
        idNum = list[0]
        secretIng = list[3]
        if secretIng in secret_ingredient_dict.keys():
            secret_ingredient_dict[secretIng].append(idNum)
        else:
            secret_ingredient_dict[secretIng] = []
            secret_ingredient_dict[secretIng].append(idNum)
    return secret_ingredient_dict


def displayDict(secret_ingredient_dict):
    """
    Function Description:
        The purpose of this function is to display the contents of a dictionary 
        containing secret ingredients and associated recipe IDs. If the dictionary is empty, a message is displayed.
    Parameters:
        secret_ingredient_dict (dict): A dictionary where keys are secret ingredients and values are lists of recipe IDs.
    Return:
        None
    """
    if secret_ingredient_dict == {}:
            print('Dictionary is empty')
    else:
        for i in secret_ingredient_dict:
            print(f'{i}: {secret_ingredient_dict[i]}')
            
main()