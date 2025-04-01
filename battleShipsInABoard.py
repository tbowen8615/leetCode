
def countBattleships(board):
    """
    :type board: List[List[str]]
    :rtype: int
    """
    # Handle the base case: if the board is empty or has no columns, return 0
    # This prevents index errors and ensures correct output for invalid inputs
    if not board or not board[0]:
        return 0

    # Initialize the count of battleships to 0
    # This is the only extra memory used, ensuring O(1) space complexity
    count = 0

    # Get the dimensions of the board
    # rows is the number of rows (m), cols is the number of columns (n)
    rows = len(board)
    cols = len(board[0])

    # Iterate through each cell in the board in a single pass
    # i represents the row index, j represents the column index
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell contains an 'X', indicating part of a battleship
            if board[i][j] == 'X':
                # To count this 'X' as the start of a battleship, ensure:
                # 1. There is no 'X' above (i.e., not part of a vertical battleship)
                # 2. There is no 'X' to the left (i.e., not part of a horizontal battleship)
                # Use i > 0 and j > 0 to avoid index out of bounds when checking above/left
                if (i > 0 and board[i - 1][j] == 'X') or (j > 0 and board[i][j - 1] == 'X'):
                    # If there is an 'X' above or to the left, this is not the start of a battleship
                    # Skip this cell as it's part of an already counted battleship
                    continue
                # If the above conditions are not met, this is the start of a new battleship
                # Increment the count
                count += 1

    # Return the total number of battleships found
    return count

board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
print(countBattleships(board))

board = [["."]]
print(countBattleships(board))