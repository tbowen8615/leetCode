def shortestToChar(s, c):
    # Helper function to recursively fill the answer array
    def fill_distances(index, c_positions, answer):
        if index == len(s):
            return

        # Find the closest distance to c
        min_distance = float('inf')
        for pos in c_positions:
            distance = abs(index - pos)
            min_distance = min(min_distance, distance)

        answer[index] = min_distance
        fill_distances(index + 1, c_positions, answer)

    # Get all positions of character c in s
    c_positions = [i for i in range(len(s)) if s[i] == c]

    # Initialize answer array
    answer = [0] * len(s)

    # Start recursive filling from index 0
    fill_distances(0, c_positions, answer)

    return answer

s = "loveleetcode"
c = "e"
print(shortestToChar(s, c))

s = "aaab"
c = "b"
print(shortestToChar(s, c))