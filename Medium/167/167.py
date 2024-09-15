def twoSum(self, numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1

    temp = numbers[left] + numbers[right]
    while temp != target:
        if temp > target:
            right -= 1
        else:
            left += 1
        
        temp = numbers[left] + numbers[right]

    return [left + 1,right + 1]