class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            if num not in freq:
                freq[num]=0
            freq[num]+=1

        retList = []

        while k>0:
            topk = -1
            topkKey = -1
            for key,val in freq.items():
                if val>topk:
                    topk=val
                    topkKey = key
            retList.append(topkKey)
            del freq[topkKey]
            k-=1
        return retList

