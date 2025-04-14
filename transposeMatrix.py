def traverse(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j])

    return True


matrix = [[1,2,3],[4,5,6],[7,8,9]]
traverse(matrix)