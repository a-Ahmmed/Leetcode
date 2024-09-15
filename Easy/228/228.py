def summaryRanges(self, nums: list[int]) -> list[str]:
    # Empty List Check
    if not nums:
        return []
    
    # Initialize Variables
    result = []
    start = nums[0]
    end = nums[0]

    def addResults(start, end):
        if start == end:
            result.append(str(start))
        else:
            result.append(f'{start}->{end}')

    i = 1
    while i < len(nums):
        if nums[i] == (nums[i - 1] + 1):
            end = nums[i]
        else:
            addResults(start, end)
            start = nums[i]
            end = nums[i]
        
        i += 1

    addResults(start, end) 

    return result