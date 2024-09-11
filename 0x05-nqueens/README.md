Steps to Solve:
Input validation:

Ensure that the user provides exactly one argument N, and that N is an integer.
If N is less than 4, print an error message and exit with status 1.
Backtracking algorithm:

Use a recursive function to place queens row by row.
At each step, check if the queen can be placed in a given column without being attacked by another queen in the previous rows.
If it can be placed, move to the next row; otherwise, backtrack.
Board representation:

Use a list of lists to represent the chessboard. Each solution is represented as a list of coordinates where queens are placed.
