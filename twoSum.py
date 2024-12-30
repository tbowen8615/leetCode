def twoSum(nums, target):

    for i in range (len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print("[",i,", ",j,"]")
                return [i, j]

nums = [2, 7, 11, 15]
target = 9

twoSum(nums, target)

enumerated_nums = enumerate(nums)

def enum_two_sum(enumerated_nums, target):
    hash_map = {}
    for i, num, in enumerated_nums:
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i
        print(hash_map)

enum_two_sum(enumerated_nums, target)