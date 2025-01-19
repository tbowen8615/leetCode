
def majorityElement(nums):
    threshold = len(nums) / 2
    unique = set(nums)
    for i in unique:
        count = 0
        for j in nums:
            if j == i:
                count += 1
        if count > threshold:
            print(i, "is the majority element.")
            return i

nums = [4, 4, 4, 4, 5, 6]
majorityElement(nums)