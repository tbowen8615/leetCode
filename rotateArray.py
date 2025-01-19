def rotate(nums, k):

    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]

    print(nums)
    return nums

nums = [1, 2, 3, 4, 5, 6]
rotate(nums, 2)