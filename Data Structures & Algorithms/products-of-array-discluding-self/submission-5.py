class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = nums[0]
        retlist = []
        flag = 0

        for i in range(1, len(nums)):
            if nums[i] == 0:
                flag += 1
                continue
            product = product * nums[i]

        if flag == 1:
            for num in nums:
                if not num==0:
                    retlist.append(0)
                else:
                    retlist.append(product)
            return retlist
        
        if flag > 1:
            return [0]*len(nums)
        
        for num in nums:
            retlist.append(int(product/num))
        return retlist
        
        

        