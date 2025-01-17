
def removeDuplicates(nums):
    if len(nums) <= 2:
        print(nums)
        return len(nums)

    write_pointer = 2

    for i in range(2, len(nums)):
        if nums[i] != nums[write_pointer - 2]:
            nums[write_pointer] = nums[i]
            write_pointer += 1

    print(nums)
    return write_pointer

nums = [1, 1, 1, 2, 2, 3]
removeDuplicates(nums)