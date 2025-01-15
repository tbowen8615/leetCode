
def removeDuplicates(nums):
    k = 0
    unique = set()

    for i in range(len(nums)):
        if nums[i] not in unique:
            unique.add(nums[i])
            nums[k] = nums[i]
            k += 1
    print(nums)
    return k

nums = [1,1,2]
removeDuplicates(nums)