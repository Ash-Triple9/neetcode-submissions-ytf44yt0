class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        retList = [[] for i in range(len(nums)+1)]

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)


        for key,val in freq.items():
            retList[val].append(key)

        res = []
        for i in range(len(retList)-1, 0, -1):
            for n in retList[i]:
                res.append(n)
                if len(res) == k:
                    return res

