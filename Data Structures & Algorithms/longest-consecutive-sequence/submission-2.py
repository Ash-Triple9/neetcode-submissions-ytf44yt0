class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = {}
        for num in nums:
            hashSet[num] = num-1
        
        longestSequence = 0
        for num in nums:
            if not num-1 in hashSet:
                tempSequence = 0
                while num in hashSet:
                    num = num+1
                    tempSequence += 1
                longestSequence  = max(tempSequence, longestSequence)
        return longestSequence          