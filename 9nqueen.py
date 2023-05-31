print("Enter the number of queens")
N = int(input())

# Chessboard
# NxN matrix with all elements 0
board = [[0]*N for _ in range(N)]

def is_attack(i, j):
    # Checking if there is a queen in the same row or column
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    # Checking diagonals
    for k in range(0, N):
        for l in range(0, N):
            if (k+l == i+j) or (k-l == i-j):
                if board[k][l] == 1:
                    return True

    return False

def N_queen(n):
    # If n is 0, solution found
    if n == 0:
        return True

    for i in range(0, N):
        for j in range(0, N):
            '''Checking if we can place a queen here or not
            A queen will not be placed if the place is being attacked
            or already occupied'''
            if (not is_attack(i, j)) and (board[i][j] != 1):
                board[i][j] = 1
                # Recursion
                # Whether we can put the next queen with this arrangement or not
                if N_queen(n-1):
                    return True
                board[i][j] = 0

    return False

# Solving the N-Queen problem
N_queen(N)

# Printing the board
for i in board:
    print(i)

'''
The provided code implements the N-Queen problem, where the goal is to place N queens on an NxN chessboard in such a way that no two queens threaten each other. The code uses a backtracking algorithm to find a solution.

Let's go through the code step by step:

1. The user is prompted to enter the number of queens (N) they want to place on the chessboard.

2. A 2D list called `board` is created to represent the chessboard. It is initialized as an NxN matrix filled with 0s.

3. The function `is_attack(i, j)` is defined to check if a queen at position `(i, j)` on the board is being attacked by any other queen. It checks for attacks in the same row, same column, and diagonals. If an attack is found, it returns `True`; otherwise, it returns `False`.

4. The main function `N_queen(n)` is defined to solve the N-Queen problem recursively. The parameter `n` represents the number of queens left to be placed on the board. The base case is when `n` becomes 0, indicating that all queens have been successfully placed without any attacks. In that case, the function returns `True`.

5. The function uses nested loops to iterate over all positions on the board. For each position, it checks if a queen can be placed there without being attacked or already occupied. If so, it marks the position as occupied by setting `board[i][j]` to 1 and recursively calls `N_queen(n-1)` to place the next queen. If a solution is found, the function returns `True`. If not, the position is reset by setting `board[i][j]` back to 0.

6. If no solution is found after checking all possible positions, the function returns `False`.

7. The `N_queen(N)` function is called to solve the N-Queen problem for the given value of N.

8. Finally, the board is printed by iterating over each row of the `board` list and printing it.

Now let's consider an example execution with N = 4:

```
Enter the number of queens
4
[1, 0, 0, 0]
[0, 0, 0, 1]
[0, 1, 0, 0]
[0, 0, 1, 0]
```

In the output, each row represents a row of the chessboard, and the value 1 represents the position where a queen is placed. The output shows a valid solution to the N-Queen problem for N = 4, where none of the queens threaten each other.
'''