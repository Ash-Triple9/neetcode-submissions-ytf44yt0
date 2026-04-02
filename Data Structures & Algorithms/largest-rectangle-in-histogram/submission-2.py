class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                prevIndex, prevHeight = stack.pop(-1)
                maxArea = max(maxArea, prevHeight*(i-prevIndex))
                start = prevIndex
            stack.append([start, height])
        
        for i, height in stack:
            maxArea = max(maxArea, height * (len(heights)-i))
        return maxArea
                    

        