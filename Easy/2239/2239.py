def findClosestNumber(self, nums: list[int]) -> int:
    ans = nums[0]

    for i in nums:
        if abs(i) < abs(ans):
            ans = i
        elif abs(i) == abs(ans):
            if i > ans:
                ans = i

    return ans