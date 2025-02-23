def search(nums, target):
    # Initialize left and right pointers for binary search
    left = 0
    right = len(nums) - 1

    # Continue while search range is valid
    while left <= right:
        # Calculate middle index
        mid = (left + right) // 2

        # If target is found, return its index
        if nums[mid] == target:
            print(mid)
            return mid
        # If target is less than middle element, search left half
        elif nums[mid] > target:
            right = mid - 1
        # If target is greater than middle element, search right half
        else:
            left = mid + 1

    # Target not found, return -1
    print("target not found")
    return -1

nums = [-1, 0, 3, 5, 9, 12]
target = 9

search(nums, target)