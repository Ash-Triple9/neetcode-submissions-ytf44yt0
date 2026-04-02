class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = float("infinity")
        left = 0
        right = 0

        have = 0
        need = 0

        countT, countS = dict(), dict()
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
            have+=1
        
        l=0
        for r in range(len(s)):
            char = s[r]
            countS[char]= 1 + countS.get(char, 0)
            if char in countT and countT[char] >= countS[char]:
                need+=1
                if have == need:
                    while have==need:
                        countS[s[l]]-=1
                        if s[l] in countT and countS[s[l]]<countT[s[l]]:
                            need-=1
                            if (r-l)+1 < window:
                                left = l
                                right = r
                                window = r-l+1
                        l+=1
        
        if window == float("infinity"):
            return ""
        else:
            return s[left:right+1]
        
                        
                    


                        
                

        