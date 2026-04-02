class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        res = []

        for i in range(len(nums)):
            res.append(pre)
            pre = pre*nums[i]

        for j in range(len(nums)-1, -1, -1):
            res[j] = res[j]*post
            post = post*nums[j]
        return res

        
        

        