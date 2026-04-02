class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largestArea = 0
        for i in range(len(heights)):
            largestArea = max(largestArea, heights[i])
            curHeight = heights[i]
            l=i
            r=i
            while l>0:
                if curHeight>heights[max(l-1,0)]:
                    break
                l-=1
            while r<len(heights):
                if curHeight>heights[min(r+1, len(heights)-1)]:
                    break
                r+=1
            print(i,r,l)
            if r == len(heights):
                r-=1
            area = heights[i]*((r-l)+1)
            largestArea = max(largestArea, area)
        return largestArea
            


        