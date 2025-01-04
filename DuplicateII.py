# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such
# that nums[i] == nums[j] and abs(i - j) <= k

def containsNearbyDuplicate(nums, k):
    num_map = {}
    for i, num in enumerate(nums):
        if num in num_map:
            if abs(i - num_map[num]) <= k:
                print("True")
                return True
    print("False")
    return False

nums = [1, 0, 1, 1]
containsNearbyDuplicate(nums, 1)