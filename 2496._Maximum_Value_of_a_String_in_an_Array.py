class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max = 0
        for i in strs:
            try:
                if int(i) > max:
                    max = int(i)
            except ValueError:
                if len(i) > max:
                    max = len(i)
        
        return max