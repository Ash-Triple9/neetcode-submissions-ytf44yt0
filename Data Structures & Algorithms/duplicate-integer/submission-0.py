class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dir = dict()
        for num in nums:
            if num not in dir:
                dir[num] = 0
            dir[num]+=1
            if dir[num]>1:
                return True
        return False
        