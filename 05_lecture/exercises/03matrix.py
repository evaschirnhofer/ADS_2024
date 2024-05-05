"""
Write a function named count_matching_elements(my_matrix: list, element: int), which takes a two-dimensional array of integers
and a single integer value as its arguments. The function then counts how many elements within the matrix match the argument value.

An example of how the function should work:

    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1)) # prints 3
"""
# Provide your solution here

"""
GO - Game
In a game of Go two players take turns to place black and white stones on a game board. 
The winner is the player who manages to encircle a bigger area on the board with their own game pieces.

Write a function named who_won(game_board: list), which takes a two-dimensional array as its argument. 
The array consists of integer values, which represent the following situations:

    0: empty square
    1: player 1 game piece
    2: player 2 game piece
    
The scoring rules of Go can be quite complex, but in this exercise it is enough to compare the number of pieces each player 
has on the game board. Also, the size of the game board is not limited.

The function should return the value 1 if player 1 won, and the value 2 if player 2 won. 
If both players have the same number of pieces on the board, the function should return the value 0.
"""
# Provide your solution here


"""
Check Row in Sudoku

Write a function named row_correct(sudoku: list, row_no: int), which takes a two-dimensional array representing a sudoku grid,
and an integer referring to a single row, as its arguments. Rows are indexed from 0.

The function should return True or False, depending on whether the row is filled in correctly, that is, 
whether it contains each of the numbers 1 to 9 at most once.
"""
sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]