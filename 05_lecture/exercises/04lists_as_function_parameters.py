"""
Write a function named double_items(numbers: list), which takes a list of integers as its argument.

The function should return a new list, which contains all values from the original list doubled. T
he function should not change the original list.

An example of the function at work:
    if __name__ == "__main__":
        numbers = [2, 4, 5, 3, 11, -4]
        numbers_doubled = double_items(numbers)
        print("original:", numbers)             # original: [2, 4, 5, 3, 11, -4]
        print("doubled:", numbers_doubled)      # doubled: [4, 8, 10, 6, 22, -8]
"""
# Provide your solution here - run the function from main block below.


"""
Write a function named remove_smallest(numbers: list), which takes a list of integers as its argument.

The function should find and remove the smallest item in the list. You may assume there is a single smallest item in the list.

The function should not have a return value - it should directly modify the list it receives as a parameter.

An example of how the function works:
    if __name__ == "__main__":
        numbers = [2, 4, 6, 1, 3, 5]
        remove_smallest(numbers)
        print(numbers)  # [2, 4, 6, 3, 5]
"""
# Provide your solution here - run the function from main block below.

"""
TIC-TAC-TOE

Tic-Tac-Toe is played on a 3 by 3 grid, by two players who take turns inputting noughts and crosses. 
If either player succeeds in placing three of their own symbols on any row, column or diagonal, they win. 
If neither player manages this, it is a draw.

Write a function named play_turn(game_board: list, x: int, y: int, piece: str), which places the given symbol 
at the given coordinates on the board. The values of the coordinates on the board are between 0 and 2.
The board consists of the following strings:
    
    "": empty square
    "X": player 1 symbol
    "O": player 2 symbol
    
The function should return True if the square was empty and the symbol was successfully placed on the game board. 
The function should return False if the square was occupied, or if the coordinates weren't valid.

An example execution of the function:
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)
"""
# Provide your solution here - run the function from main block below.


"""
TIC-TAC-TOE Advanced
Implement the game logic for a Tic-Tac-Toe game. Implement a loop which continuously asks player 1 and player 2 to place their tics.
Furthermore, write a function which after each successful placement of a tic checks whether the player has won or not. If a player has won,
or the game ends with a draw, stop the game and print the results ("Player 1 has won!", "It's a draw!") and print the final game board.
"""
# Provide your solution here - run the function from main block below.

if __name__ == "__main__":
    print("Run your functions here.")