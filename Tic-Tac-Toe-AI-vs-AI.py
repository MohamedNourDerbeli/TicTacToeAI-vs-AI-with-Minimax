import random
# Define the main function for playing tic-tac-toe
def tic_tac_toe(grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]):
# Function to print the tic-tac-toe grid
    def printgrid(grid):
        # Prints the grid with vertical and horizontal lines
        print(grid[0] + '|' + grid[1] + '|' + grid[2])
        print('-+-+-')
        print(grid[3] + '|' + grid[4] + '|' + grid[5])
        print('-+-+-')
        print(grid[6] + '|' + grid[7] + '|' + grid[8])
        print("\n")

# Function to check if a space on the grid is free
    def spaceIsFree(position):
        if grid[position] == ' ':
            return True
        else:
            return False

# Function to insert a letter (X or O) at a specific position
    def insertLetter(letter, position):
        # Checks if the position is available and inserts the letter
    # Then, it checks if the game is a draw or if someone has won
        if spaceIsFree(position):
            grid[position] = letter
            printgrid(grid)
            if (checkDraw()):
                print("Draw!")
                exit()
            if checkForWin():
                if letter == 'X':
                    print("Alex wins!")
                    exit()
                else:
                    print("Sam wins!")
                    exit()

            return

    # Function to check if a player has won the game
    def checkForWin():
        # Checks for all possible win conditions on the grid
        # Returns True if any of these conditions are met, indicating a win
        # Otherwise, it returns False
        if (grid[0] == grid[1] and grid[0] == grid[2] and grid[0] != ' '):
            return True
        elif (grid[3] == grid[4] and grid[3] == grid[5] and grid[3] != ' '):
            return True
        elif (grid[6] == grid[7] and grid[6] == grid[8] and grid[6] != ' '):
            return True
        elif (grid[0] == grid[3] and grid[0] == grid[6] and grid[0] != ' '):
            return True
        elif (grid[1] == grid[4] and grid[1] == grid[7] and grid[1] != ' '):
            return True
        elif (grid[2] == grid[5] and grid[2] == grid[8] and grid[2] != ' '):
            return True
        elif (grid[0] == grid[4] and grid[0] == grid[8] and grid[0] != ' '):
            return True
        elif (grid[6] == grid[4] and grid[6] == grid[2] and grid[6] != ' '):
            return True
        else:
            return False

    # Function to determine which player (Alex or Sam) has won
    def checkWhichMarkWon(mark):
        # Similar to checkForWin, this function checks if a specific player's mark has won
        # Returns True if that player has won, otherwise, it returns False
        if grid[0] == grid[1] and grid[0] == grid[2] and grid[0] == mark:
            return True
        elif (grid[3] == grid[4] and grid[3] == grid[5] and grid[3] == mark):
            return True
        elif (grid[6] == grid[7] and grid[6] == grid[8] and grid[6] == mark):
            return True
        elif (grid[0] == grid[3] and grid[0] == grid[6] and grid[0] == mark):
            return True
        elif (grid[1] == grid[4] and grid[1] == grid[7] and grid[1] == mark):
            return True
        elif (grid[2] == grid[5] and grid[2] == grid[8] and grid[2] == mark):
            return True
        elif (grid[0] == grid[4] and grid[0] == grid[8] and grid[0] == mark):
            return True
        elif (grid[6] == grid[4] and grid[6] == grid[2] and grid[6] == mark):
            return True
        else:
            return False

    # Function to check if the game is a draw
    def checkDraw():
        for key, value in enumerate(grid):
            if (grid[key] == ' '):
                return False
        return True

    # Function for the AI player's move (Sam in this case)
    def SamMove():
        # Implements the minimax algorithm to find the best move for Sam
        # The algorithm tries all possible moves and scores them, then chooses the best move
        # It then inserts Sam's letter at the chosen position
        bestScore = -800
        bestMove = 0
        for key, value in enumerate(grid):
            if (grid[key] == ' '):
                grid[key] = Sam
                score = minimax2(grid, 0, False)
                grid[key] = ' '
                if (score > bestScore):
                    bestScore = score
                    bestMove = key

        insertLetter(Sam, bestMove)
        return

    # Function for the other player's (Alex) move
    def AlexMove():
    # Similar to SamMove, this function determines the best move for Alex    
        bestScore = -800
        bestMove = 0
        for key, value in enumerate(grid):
            if (grid[key] == ' '):
                grid[key] = Alex
                score = minimax(grid, 0, False)
                grid[key] = ' '
                if (score > bestScore):
                    bestScore = score
                    bestMove = key

        insertLetter(Alex, bestMove)
        return
# The minimax2 and minimax functions are used for the AI's decision-making
    # They evaluate the possible moves and return scores to determine the best move
    def minimax2(grid, depth, isMaximizing):
        if (checkWhichMarkWon(Sam)):
            return 1
        elif (checkWhichMarkWon(Alex)):
            return -1
        elif (checkDraw()):
            return 0

        if (isMaximizing):
            bestScore = -800
            for key, value in enumerate(grid):
                if (grid[key] == ' '):
                    grid[key] = Sam
                    score = minimax2(grid, depth + 1, False)
                    grid[key] = ' '
                    if (score > bestScore):
                        bestScore = score
            return bestScore

        else:
            bestScore = 800
            for key, value in enumerate(grid):
                if (grid[key] == ' '):
                    grid[key] = Alex
                    score = minimax2(grid, depth + 1, True)
                    grid[key] = ' '
                    if (score < bestScore):
                        bestScore = score
            return bestScore

    def minimax(grid, depth, isMaximizing):
        if (checkWhichMarkWon(Alex)):
            return 1
        elif (checkWhichMarkWon(Sam)):
            return -1
        elif (checkDraw()):
            return 0

        if (isMaximizing):
            bestScore = -800
            for key, value in enumerate(grid):
                if (grid[key] == ' '):
                    grid[key] = Alex
                    score = minimax(grid, depth + 1, False)
                    grid[key] = ' '
                    if (score > bestScore):
                        bestScore = score
            return bestScore

        else:
            bestScore = 800
            for key, value in enumerate(grid):
                if (grid[key] == ' '):
                    grid[key] = Sam
                    score = minimax(grid, depth + 1, True)
                    grid[key] = ' '
                    if (score < bestScore):
                        bestScore = score
            return bestScore

    Sam = 'O'
    Alex = 'X'

    # Randomly decide which player goes first
    starting_player = random.choice([Sam, Alex])

    # Start the game with the player who goes first
    if starting_player == Sam:
        SamMove()
    else:
        AlexMove()

    # Continue the game until there is a winner or a draw
    while not checkForWin():
        SamMove()
        AlexMove()

# Create an initial empty grid and start the game
grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
tic_tac_toe(grid)
