class Solution:
    def isPalindrome(self, s: str) -> bool:

        start = 0
        end = len(s)-1

        while start<=end:

            startChar = s[start]
            endChar = s[end]

            # Check if valid char
            if not startChar.isalnum():
                start+=1
                continue
            if not endChar.isalnum():
                end-=1
                continue

            # Compare chars
            if startChar.lower() != endChar.lower():
                return False

            start+=1
            end-=1

        return True
