def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        unique = set()
        longest = 0

        while r != len(s):
            if s[r] not in unique:
                unique.add(s[r])
                r += 1
            else:
                unique.remove(s[l])
                l += 1

            longest = max(r - l, longest)

        return longest