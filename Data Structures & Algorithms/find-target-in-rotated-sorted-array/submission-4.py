class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        l = 0
        r = len(nums)-1
        while (r-l)!=1:
            m = (l+r)//2

            if nums[m]==target:
                return m

            # Find which side is the sorted side
            if nums[l] < nums[m]:
                # Left side is sorted
                # Check if target lies in this region
                if nums[l]<=target<=nums[m]:
                    # If so, reduce this region
                    r = m
                else:
                    l = m
            
            else:
                # Right side is sorted
                if nums[m]<=target<=nums[r]:
                    l=m
                else:
                    r = m
        if nums[r]==target:
            return r
        elif nums[l]==target:
            return l
        return -1
        