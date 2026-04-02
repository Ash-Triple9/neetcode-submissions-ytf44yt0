class Solution:
    def trap(self, height: List[int]) -> int:
        result = []
        currPrefix = 0
        for i in range(len(height)):
            if i > 0:
                currPrefix = max(height[i-1], currPrefix)
                result.append(currPrefix)
            else:
                result.append(currPrefix)

        currSuffix = 0
        for j in range(len(height)-1, 0, -1):
            if j < len(height)-1:
                currSuffix = max(currSuffix, height[j+1])
                result[j] = min(result[j], currSuffix) - height[j]

            else:
                result[j] = min(result[j],currSuffix) - height[j]

        total = 0
        for num in result:
            if num > 0:
                total+= num
        
        return total

        
        