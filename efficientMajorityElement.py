
def majorityElement(nums):
    candidate = None
    count = 0

    for i in nums:
        if count == 0:
            candidate = i
        count += (1 if candidate == i else -1)
    print(candidate, "is the majority element.")
    return candidate

nums = [4, 4, 5, 6, 1, 1, 1]
majorityElement(nums)