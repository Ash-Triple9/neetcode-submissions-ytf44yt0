class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Optimal soln:
        An array which was originally in sorted ascending order has now
            been rotated between 1 and n times. 
        We are given a target, and have to return the index of the target within the array,
            or -1 if it is not present.
        
        The O(n) solution is easy enough to do,
            Iterate through the list and check if number is present or not.
        Trying the O(log n) solution:
            This means a binary approach.
            e.g.
                [3,4,5,6,1,2], target = 1
                mid point is 5
                low is 3
                high is 2
                
                5 is not our target, target value is smaller than 5
                normally that means split left,
                 but our low end has a value of 3, higher than target value.
                 so we know that target is not on left, so go to right
                
                [6,1,2], midpoint is our target.

                [6,0,1,2,3,4,5] target = 4
                mid = 2, low = 6, high = 5
                we know the sequence restarts on the left side because mid < high

                have to keep in mind which side the sequence restarts, the low, mid and high vals and the target
        '''
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

        