def sum(a, b, c):
    return a + b + c

def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    
    # Print the current board state
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ") 

def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    for win in wins:
        # Check if X has won the match
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X Won the match")
            return 1
        
        # Check if O has won the match
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("O Won the match")
            return 0
    
    # No winner yet
    return -1
    
if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X and 0 for O
    
    print("Welcome to Tic Tac Toe")
    
    while True:
        printBoard(xState, zState)  # Print the current board state
        
        if turn == 1:
            print("X's Chance")
            value = int(input("Please enter a value: "))
            xState[value] = 1  # Mark the selected position with 'X'
        else:
            print("O's Chance")
            value = int(input("Please enter a value: "))
            zState[value] = 1  # Mark the selected position with 'O'
        
        cwin = checkWin(xState, zState)  # Check if there is a winner
        
        if cwin != -1:
            print("Match over")
            break
        
        turn = 1 - turn  # Switch the turn between X and O


'''
Certainly! Here's a detailed explanation of the provided code:

1. The `sum` function takes three inputs `a`, `b`, and `c` and returns their sum.

2. The `printBoard` function takes two inputs `xState` and `zState`, which represent the current state of the board for X and O players. It prints the current board state using the values from `xState` and `zState`.

3. The `checkWin` function takes two inputs `xState` and `zState`, representing the board state for X and O players. It checks for a winning condition by examining all possible winning combinations (`wins`). If X or O has won, it prints the corresponding message and returns the respective value. If there is no winner, it returns -1.

4. The `if __name__ == "__main__":` block ensures that the following code is only executed when the script is run directly, not when it is imported as a module.

5. The variables `xState` and `zState` are initialized as lists representing the initial state of the board for X and O players.

6. The variable `turn` is initialized as 1, representing the turn of X player. The value 0 would represent the turn of O player.

7. The message "Welcome to Tic Tac Toe" is printed to indicate the start of the game.

8. The main game loop begins with the `while True:` statement.

9. Inside the loop, `printBoard(xState, zState)` is called to display the current board state.

10. Depending on the value of `turn`, either "X's Chance" or "O's Chance" is printed to prompt the respective player for their move.

11. The player's input is read as an integer value and stored in the variable `value`.

12. If it is X's turn (`turn == 1`), `xState[value]` is set to 1 to mark the selected position as occupied by X. Otherwise, if it is O's turn (`turn == 0`), `zState[value]` is set to 1 to mark the selected position as occupied by O.

13. The `checkWin(xState, zState)` function is called to check if there is a winner. If a winner is found (`cwin != -1`), the corresponding message is printed, and the game loop is terminated with a `break` statement.

14. After each move, the turn is switched between X and O by setting `turn = 1 - turn`. If it was X's turn, it becomes O's turn, and vice versa.

15. The game continues until there is a winner or the game ends in a tie.

Overall, the code implements a simple command-line version of the Tic Tac Toe game, allowing players to take turns, mark their moves on the board, and checks for a winner after each move.
'''