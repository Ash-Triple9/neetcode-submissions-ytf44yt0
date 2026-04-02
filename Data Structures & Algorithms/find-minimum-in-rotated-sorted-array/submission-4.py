class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return min(nums[0], nums[1])
        l=0
        r=len(nums)-1
        while (r-l)!=1:
            m = (r+l)//2
            if nums[l]>nums[m]:
                r = m
            elif nums[m]>nums[r]:
                l = m
            else:
                return nums[l]
        return min(nums[l], nums[r])
            
            

        
        