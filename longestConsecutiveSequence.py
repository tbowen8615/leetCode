
def longestConsecutive(nums):

    if not nums:
        return 0

    unique_set = set(nums)
    longest_streak = 0

    for num in unique_set:
        # Only start a sequence if num is the start of the sequence
        if (num - 1) not in unique_set:
            current_num = num
            current_streak = 1

            # Count the length of the sequence
            while (current_num + 1) in unique_set:
                current_num += 1
                current_streak += 1

            # Update the longest streak
            longest_streak = max(longest_streak, current_streak)
    print(longest_streak, "is the longest streak.")
    return longest_streak

nums = [100, 4, 200, 1, 3, 2]
longestConsecutive(nums)