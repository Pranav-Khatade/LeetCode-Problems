class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lil = []
        n=0
        for char in s:
            if char not in lil:
                lil.append(char)
            else:
                while char in lil:
                    lil.pop(0)
                lil.append(char)
            n = max(n,len(lil))
        return n