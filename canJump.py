
def canJump(nums):
    farthest = 0

    for i in range(len(nums)):
        if i > farthest:
            print("You cannot reach the end")
            return False

        farthest = max(farthest, i + nums[i])

        if farthest >= len(nums) - 1:
            print("You can reach the end")
            return True

    print("You can reach the end")
    return True

nums = [2,3,1,1,4]
canJump(nums)