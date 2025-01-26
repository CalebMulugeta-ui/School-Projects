""" Complete your "Project Details".  If there is an arrow to the right of the line number then click the arrow
to expand the comment.
********************************************************
COMP 1005/1405 Section [A] - Assignment [3]

Project Details:
    Name: Caleb Mulugeta
    Student #: 101352144
    Date Created: November 4, 2024

External Libraries Used (if appliable)
import random
********************************************************
"""
""" Pseudocode 
        Prompt user input for total rounds of the game
        Initialize the total game score
        for each round:
            Validate the user input for board size and number of ships
            Handle invalid entries 
            Set the board and ships.
            for each shot in the round:
                Request the user to input the assumed ship coordinates
                Display the Hit message (Hit or Miss)
                Display the full board with updated attempts results 
            Show the final state of the board
            Display the user final score of this round
        Display the user final score of the game
"""

""" Import the libraries if appliable

""" 
""" Define global variables if appliable

"""

# Suggest to start by understanding the code in the main function.
# Then proceed with the coding.

import random


def addShip(board, numShips):
    """ Function Description:
            Randomly places the specified number of ships ('S') on the board.
        Parameter(s): 
            board : The list of lists representing the game board
            numShips [int]: The number of ships that user wants on the board
        Return: None   
    """
    for i in range(0, numShips):
        randomPos = random.randint(0,len(board))
        rndm = random.randint(0, len(board)-1)
        board[rndm].insert(randomPos, "S")
        board[rndm].remove("~")
    return board

def checkSetUpError(size, numShips):
    """ Function Description:
            Validates user input for the size of the board and the number of ships.
        Parameter(s): 
            size [int]: The size of the board
            numShips [int]: The number of ships
        Return [Boolean]: Return True if an error is found or False if there is no error.
    """
    maxShips = (size*size)-2

    if ((numShips > maxShips) or (numShips < 1) or size < 2 or size > 5 ):
       return True

    elif ((numShips < maxShips) or (numShips > 1) or (size > 2 or size < 5)):
        return False

def checkFireError(board, row, col):
    """ Function Description:
            Validates user input for the coordinates to shot a ship
        Parameter(s):
            board : The list of lists representing the game board
            row [int]: The row coordinate entered by the user.
            col [int]: The col coordinate entered by the user. 
        Return [Boolean]: Return True if an error is found or False if there is no error.   
    """
    
    if ((row < 0) or (col < 0) or (row > (len(board))-1) or (col > (len(board))-1) or (board[row][col] == 'X') or (board[row][col] == 'O')):
        return True #Error   

    if (row >= 0) and (col >= 0) and (row <= (len(board))-1) and (col <= (len(board)-1)): 
        return False #No Error  
        

def createBoard(size):
    """ Function Description:
            Creates a size-by-size game board initialized with '~'
        Parameter(s):
            size [int]: The size of the board which will be used to create a board of size x size
                        Example: size 2 will create [ ['~', '~'], ['~', '~']]
        Return: board which is a list of lists  
    """
    
    board = []
    for rows in range(size):
        newList = []
        for columns in range(size):
            newList.append("~")
        board.append(newList)
    return board

def displayBoard(board, round=True):
    """ Function Description:
            Displays the current state of the board.  If round is True then print out the current
            state of the board without showing the ships 'S'.  Else round is False then print out the
            current state of the board showing hits 'X', misses 'O', ships that have not been hit 'S'
            and everything else '~'.
        Parameter(s):
            board : The list of lists representing the game board.
            round [Boolean] : True if you are print the board after each shot and False to display
            the end of a round version.  Default value of True.
        
        Return: None  
    """
    if round == True: #During game
        for i in range(0, len(board)):
            for e in range(0, len(board)):
                if board[i][e]=="S": #checks if position is equal to S on the board
                    print('~', end="") #when the postion is equal to S on the board, it prints ~ in its place
                else:
                    print(board[i][e], end="")
            print()
     #End game(Prints everything)
    if round == False:
        for i in range(0, len(board)):
            for e in range(0,len(board)):
                print(board[i][e], end="")
            print()
    return


def fireShot(board, row, col):
    """ Function Description:
            Marks a shot on the board.
        Parameter(s):
            board : The list of lists representing the game board
            row [int]: The row coordinate entered by the user.
            col [int]: The col coordinate entered by the user. 
        Return[Boolean]: Return True if a ship was hit and False if the shot missed a ship.     
    """  


    if board[row][col] == "S":
        board[row].insert(col + 1,'X')
        board[row].remove('S')
        return True
    
    if board[row][col]== "~":
        board[row].insert(col + 1,'O')
        board[row].remove('~')
        return False
    
    return board
def playRound(board, numShips):
    """ Function Description:
            Main logic for playing one round 
            
            Pseudocode:
            Keep track of number of shots for the round
            Keep track of the score (number of hits) for the round
            Loop until user fires all their shots
                Ask user to enter coordinates for their shot.  Input two numbers separated by a space.
                Validate the shot coordinates using checkFireError function
                Fire a shot using the fireShot function
                Output if the shot is a hit or a miss
                display the board after the shot has been taken displayBoard(board)
            Output "End of round X"
            display the board at the end of the round displayBoard(board, False)
    
        Parameter(s):
            board : The list of lists representing the game board
            numShips [int]: The number of ships
        Return [int]: The number of hits (ships that were hit) for the round.   
    """ 
    counter = 0
    shotPerRound = 0
    hitsPerRound = 0
    shot = numShips
    while shot > 0:
        shotPerRound += 1
        shot -= 1
        #Get user coordinates, split the given numbers
        rowCol = input("Enter row and column to take a shot (e.g., 2 3): ")
        split = rowCol.split(' ')
        userRow = int(split[0])
        userCol = int(split[1])
        flag=checkFireError(board, userRow, userCol) 
        if flag == True:
            shot += 1
            print("You need to enter your coordinates again")
            continue         
        
        counter += 1
        checkShot = fireShot(board, userRow, userCol)
        if checkShot == True:
            hitsPerRound += 1
            print(f"Shot {counter} is a Hit!")
        if checkShot == False:
            print(f"Shot {counter} is a Miss!")
        displayBoard(board)
    print("End of Round: ")
    displayBoard(board, False)

    return hitsPerRound

totalScore = 0
def main():    
    """ Function Description:
            Play the game in a designated number of rounds and present the final score to the user.
            You can not change the code in the main function.  If student changes the main function code
            then they will lose 25 marks.
        Parameter(s): No parameters
        Return: None  
    """
    currentRound = 0
    numRounds = int(input("Enter the number of rounds of Battleship you want to play: "))
    flag = True
    while currentRound < numRounds:
        while flag:
            size = int(input("Enter the size of the board: "))
            numShips = int(input("Enter the number of ships: "))
            flag = checkSetUpError(size, numShips)
            if (flag == False):
                break
            else:
                print("You will need to enter the size of the board and number of ships again.")
            
        board = createBoard(size)
        addShip(board, numShips)
        print(f"\nRound {currentRound + 1}:\n")
        hits = playRound(board, numShips)
        global totalScore
        totalScore += hits
        currentRound += 1
    print(f"\nFinal Score after {numRounds} round(s) is {totalScore} out {numShips * numRounds}.")
    return

if __name__ == '__main__':
    main()