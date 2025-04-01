def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    # Step 1: Get the size of the matrix (n x n)
    # Since the matrix is square, n is the length of the matrix
    n = len(matrix)

    # Step 2: Transpose the matrix
    # Transposing means swapping elements across the main diagonal
    # We only need to iterate over the upper triangle (i.e., i <= j)
    # to avoid swapping elements twice
    for i in range(n):
        for j in range(i, n):
            # Swap matrix[i][j] with matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 3: Reverse each row of the transposed matrix
    # After transposing, reversing each row completes the 90-degree clockwise rotation
    for i in range(n):
        # Use two pointers to reverse the row in-place
        left, right = 0, n - 1
        while left < right:
            # Swap elements at left and right indices in the current row
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            # Move the pointers inward
            left += 1
            right -= 1

matrix = [[1,2,3],[4,5,6],[7,8,9]]

# Visualize the initial matrix
print("Initial Matrix:")
for row in matrix:
    print(row)

# Call the rotate function to modify the matrix in-place
rotate(matrix)

# Visualize the matrix after rotation
print("\nRotated Matrix (90 degrees clockwise):")
for row in matrix:
    print(row)