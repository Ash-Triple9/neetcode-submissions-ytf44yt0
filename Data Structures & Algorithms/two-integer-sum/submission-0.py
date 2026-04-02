class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dir = {}
        for i in range(len(nums)):
            remainder = target-nums[i]
            if remainder not in dir:
                dir[nums[i]] = i
            else:
                return sorted([i, dir[remainder]])