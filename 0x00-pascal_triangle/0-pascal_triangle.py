def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n rows.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        prev_row = triangle[i - 1]
        for j in range(len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j + 1])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle