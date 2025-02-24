def minSubArrayLen(target, nums):
    # 1. Initialize pointers and variables for sliding window
    start = 0
    current_sum = 0
    min_length = float('inf')

    # 2. Iterate through nums using end pointer to expand window
    for end in range(len(nums)):
        # Add current element to running sum
        current_sum += nums[end]

        # 3. Shrink window while sum is >= target to minimize length
        while current_sum >= target:
            # Update minimum length if current window is shorter
            min_length = min(min_length, end - start + 1)
            # Subtract element at start and move start pointer
            current_sum -= nums[start]
            start += 1

    # 4. Return 0 if no valid subarray found, otherwise return minimum length
    return min_length if min_length != float('inf') else 0

nums = [2, 3, 1, 2, 4, 3]
target = 7
print(minSubArrayLen(target, nums))