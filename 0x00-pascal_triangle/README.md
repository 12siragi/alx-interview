# Pascal's Triangle

This project contains a Python function to generate Pascal's Triangle, a mathematical construct that displays binomial coefficients in a triangular array.

## Description

Pascal's Triangle is a triangular array of binomial coefficients. The function `pascal_triangle(n)` generates the first `n` rows of Pascal's Triangle and returns them as a list of lists.

## Function

### `pascal_triangle(n)`

Returns a list of lists of integers representing Pascal's Triangle with `n` rows.

**Parameters:**
- `n` (int): The number of rows to generate. Must be a non-negative integer.

**Returns:**
- List of lists of integers: Pascal's Triangle with `n` rows. Returns an empty list if `n <= 0`.

### Example

```python
>>> from pascal_triangle import pascal_triangle
>>> pascal_triangle(5)
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]

