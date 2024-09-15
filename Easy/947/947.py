def sortedSquares(self, nums: list[int]) -> list[int]:
    unsortedSquaredNums = [n*n for n in nums]
    length = len(unsortedSquaredNums)
    i, j, k, temp = 0, 0, 0, 0 # Variables for sorting

    # Selection Sort
    while i < length:
        j = i
        k = i + 1

        while k < length:
            if unsortedSquaredNums[k] < unsortedSquaredNums[j]:
                j = k
            
            k += 1
        
        temp = unsortedSquaredNums[i]
        unsortedSquaredNums[i] = unsortedSquaredNums[j]
        unsortedSquaredNums[j] = temp

        i += 1

    return unsortedSquaredNums # Now sorted

def attempt2(self, nums: list[int]) -> list[int]:
    
    def appender(dest: list, origin: list, index: int) -> None:
        length = len(origin)
        i = index

        while i < length:
            dest.append(origin[i])
            i += 1
    
    positives, negatives, final = [], [], []    # Arrays to be used
    j, k = 0, 0                         # Pointer Variables
    
    # Square and Split Array for merging later
    for i in nums:
        if i > 0:
            positives.append(i*i)
        else:
            negatives.append(i*i)

    positiveLength = len(positives)
    negativeLength = len(negatives)

    negatives.reverse()     # Reverse the list to set up comparisosn

    while j < positiveLength and k < negativeLength:
        if positives[j] < negatives[k]:
            final.append(positives[j])
            j += 1
        else:
            final.append(negatives[k])
            k += 1

    if k != negativeLength:
        appender(final, negatives, k)
    elif j != positiveLength:
        appender(final, positives, j)
    
    return final

def attempt3(self, nums: list[int]) -> list[int]:
    start, end = 0, len(nums) - 1
    result = []

    while start <= end:
        if abs(nums[start]) >= abs(nums[end]):
            result.append(nums[start] * nums[start])
            start += 1
        elif abs(nums[start]) < abs(nums[end]):
            result.append(nums[end] * nums[end])
            end -= 1
    
    result.reverse()

    return result