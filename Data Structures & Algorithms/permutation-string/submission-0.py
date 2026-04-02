class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1freq = dict()
        for char in s1:
            s1freq[char] = 1 + s1freq.get(char,0)
        
        s2freq = dict()
        for i in range(len(s1)):
            s2freq[s2[i]] = 1 + s2freq.get(s2[i],0)

        l = 0
        r = len(s1)-1

        while r < len(s2):
            if s1freq == s2freq:
                return True
            else:
                s2freq[s2[l]]-=1
                if s2freq[s2[l]] == 0:
                    del s2freq[s2[l]]
                r+=1
                l+=1
                if r==len(s2):
                    continue
                s2freq[s2[r]] = 1 + s2freq.get(s2[r],0)
        return False

            

            

            


        