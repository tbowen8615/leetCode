def three_sum(nums):
    nums.sort() # sort the array
    result = []

    for i in range(len(nums) - 2):
        # skip duplicate elements for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # initialize two pointers
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                # found a triple
                result.append([nums[i], nums[left], nums[right]])

                # skip duplicates for the second and third numbers
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move pointers inward
                left += 1
                right -= 1

            elif current_sum < 0:
                # increase the sum
                left += 1
            else:
                right -= 1

    print(result)
    return result

nums = [-1, 0, 1, 2, -1, -4]
three_sum(nums)