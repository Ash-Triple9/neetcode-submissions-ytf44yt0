class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i = 0 #Index value 1
        j = len(heights)-1 #Index value 2
        while i < j:
            leftBar = heights[i]
            rightBar = heights[j]
            tmpArea = min(leftBar, rightBar) * (j-i)
            if not tmpArea > area:
                if leftBar < rightBar:
                    i+=1
                else: 
                    j-=1
            else:
                area = tmpArea

        return area

        