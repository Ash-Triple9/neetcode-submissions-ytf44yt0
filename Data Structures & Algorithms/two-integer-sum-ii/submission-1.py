class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1

        while start < end:
            num1 = numbers[start]
            num2 = numbers[end]

            if num1+num2 == target:
                return [start+1, end+1]

            if num1+num2 > target:
                end-=1
                continue
            if num1+num2 < target:
                start+=1
                continue
        