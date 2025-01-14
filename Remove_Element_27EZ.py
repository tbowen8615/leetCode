"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following:
1) Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
2) Return k
"""


def removeElement(nums, val):
    k = 0 # Index to place the next non-val element

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    print(nums, k)
    return k

nums = [3,2,2,3]
val = 3
removeElement(nums, val)