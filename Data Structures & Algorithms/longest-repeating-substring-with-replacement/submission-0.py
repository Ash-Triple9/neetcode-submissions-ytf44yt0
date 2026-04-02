class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        chars = dict()
        topf = 0
        res = 0

        for r in range(len(s)):
            chars[s[r]] = 1+ chars.get(s[r],0)
            topf = max(topf, chars[s[r]])
            window = r-l+1
            if window-topf<=k:
                res = window
            else:
                chars[s[l]]-=1
                l+=1
        return res


        