class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for index,value in enumerate(temperatures):
            while stack and stack[-1][1]<value:
                pair = stack.pop(-1)
                result[pair[0]] = index-pair[0]
            stack.append([index,value])
        return result
        