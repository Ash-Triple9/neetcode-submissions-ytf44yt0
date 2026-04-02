import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        We are given an unsorted array of integers 
        We are given a value k

        We are asked to return the kth largest element in the array
        The kth largest here means largest in sorted order, not the kth distinct elem

        Trivially, just sort it and find the largest.

        or do a min heap lol
        '''
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        
        i = 0
        retVal = 0
        while i < k:
            retVal= heapq.heappop(heap)
            i+=1
        return -retVal


        