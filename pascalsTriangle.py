
def generate(numRows: int) -> list[list[int]]:
    # Step 1: Handle edge case - if numRows is 0, return an empty list
    if numRows == 0:
        return []

    # Step 2: Initialize the result with the first row [1]
    # This is the base case for Pascal's Triangle
    result = [[1]]

    # Step 3: Generate each row from 2 to numRows
    for i in range(1, numRows):
        # Get the previous row to compute the current row
        prev_row = result[-1]
        # Start the new row with 1 (first element is always 1)
        new_row = [1]

        # Compute middle elements: each is the sum of two numbers above it
        # For position j, use prev_row[j-1] + prev_row[j]
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        # End the row with 1 (last element is always 1)
        new_row.append(1)

        # Add the new row to the result
        result.append(new_row)

    # Step 4: Return the complete triangle
    return result

numRows = 5
print(generate(numRows))