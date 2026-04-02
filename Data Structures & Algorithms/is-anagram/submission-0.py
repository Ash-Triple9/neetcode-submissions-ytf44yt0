class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = dict()
        for char in s:
            if char not in freq:
                freq[char] = 0
            freq[char]+=1
        for char in t:
            if char not in freq:
                return False
            freq[char] -= 1
        
        for k,v in freq.items():
            if v != 0:
                return False
        return True
        