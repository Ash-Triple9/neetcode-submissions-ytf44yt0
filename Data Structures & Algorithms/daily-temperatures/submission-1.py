class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Brute force soln:
        Given an array of ints, arr[i] represent the temp on the ith day.
        Have to calculate the number of days after i before a warmer day appears.

        [30,38,30,36,35,40,28]

        So for 30, the next day itself is warmer. So res[i] -> 1
        For 38, the next warmer day is 40, 4 days after. So res[i] -> 4

        A solution would be to do a double for loop:
        For each number, iterate through the rest of the loop to see when the next higher number appears.
            When we find such a number, store the indices passed.
            If no such number is found, set it to 0
        '''
        res = []
        for i in range(len(temperatures)):
            flag = False
            for j in range(i+1, len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    res.append(j-i)
                    flag = True
                    break
            if not flag:
                res.append(0)
        return res

                
        