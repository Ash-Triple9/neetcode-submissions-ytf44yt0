class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Brute force soln:
        Our input works with list of ints and a number k
        Asks us to return the k most frequent elements in the array.

        [1,2,2,3,3,3] where k = 2
        What can a simple solution look like?
        1 occurs once, top 3
        2 occurs twice, top 2
        3 occurs thrice, top 1
        Have to count the occurrence. How?

        Maybe create a set() from the list, which gives only unique numbers
        (1,2,3)
        The use the set to count the occurrence by iterating over the list and save that
            in a list of lists:
            [[1,1], [2,2], [3,3]] -> [a,b] a=frequency, b=int
            Can sort the list and then pick the top k
        '''
        uniqueInts = set(nums)
        resList = []
        for num in uniqueInts:
            count = 0
            for target in nums:
                if target == num:
                    #increase count if found
                    count += 1
            resList.append([count, num])

        resList.sort(reverse=True)
        print(resList)
        res = []
        for i in range(k):
            res.append(resList[i][1])
        return res


