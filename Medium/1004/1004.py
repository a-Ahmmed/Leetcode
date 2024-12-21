def longestOnes(self, nums: list[int], k: int) -> int:
        l, r = 0, 0
        longest = 0

        while r != len(nums):
            if nums[r] == 1:
                r += 1
            else:
                if k > 0:
                    k -= 1
                    r += 1
                else:
                    if nums[l] == 0:
                        k += 1
                    l += 1

            longest = max(r - l, longest)
        
        return longest