class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0: return 0
        r = 0
        l = 0
        chars = set()
        count = 0
        while r<len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l+=1
            chars.add(s[r])
            r+=1
            count = max(count, r-l)
        return count

        