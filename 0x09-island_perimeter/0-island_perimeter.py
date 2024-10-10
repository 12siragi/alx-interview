#!/usr/bin/python3
"""
This module contains the function island_perimeter that calculates
the perimeter of an island represented in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of an island described in a grid.
    
    Args:
        grid (list of list of int): The grid representing the island and water.
        
    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides
                perimeter += 4

                # Subtract sides for adjacent land cells
                if i > 0 and grid[i - 1][j] == 1:  # Check cell above
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # Check cell below
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Check cell to the left
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:  # Check cell to the right
                    perimeter -= 1

    return perimeter

