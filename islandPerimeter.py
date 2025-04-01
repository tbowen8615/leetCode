
def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # Initialize variables: rows and cols for grid dimensions
    rows = len(grid)
    cols = len(grid[0])

    # Initialize perimeter to 0; this will store the total perimeter
    perimeter = 0

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Base case: If the cell is water (0), skip it as it doesn't contribute to the perimeter
            if grid[i][j] == 0:
                continue

            # For a land cell (1), start with a perimeter contribution of 4 (all sides exposed)
            cell_perimeter = 4

            # Check the four adjacent cells (up, down, left, right) to find shared edges
            # If an adjacent cell is also land, subtract 1 from the perimeter for the shared side

            # Check up (i-1, j)
            if i > 0 and grid[i - 1][j] == 1:
                cell_perimeter -= 1

            # Check down (i+1, j)
            if i < rows - 1 and grid[i + 1][j] == 1:
                cell_perimeter -= 1

            # Check left (i, j-1)
            if j > 0 and grid[i][j - 1] == 1:
                cell_perimeter -= 1

            # Check right (i, j+1)
            if j < cols - 1 and grid[i][j + 1] == 1:
                cell_perimeter -= 1

            # Add this cell's contribution to the total perimeter
            perimeter += cell_perimeter

    # Return the total perimeter of the island
    return perimeter

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(islandPerimeter(grid))

grid = [[1]]
print(islandPerimeter(grid))

grid = [[1,0]]
print(islandPerimeter(grid))