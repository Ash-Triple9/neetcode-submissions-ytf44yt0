import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        Choosing the two heaviest stones, meaning we can use the heap struct
            to find the heaviest two element
        If the two heaviest stones are of same weight, then they are destroyed. 
        If one is less than the other, then the smaller stone is destroyed and 
            the difference in the weights is the new weight of the heavier stone. 
        Do the simulation until the heap structure is empty or 1, return the weight
            of the last stone or 0 if it becomes 0.
        '''

        # heapify the list, but use a max heap instead of min heap
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        # while maxHeap length >= 1,
        while len(maxHeap)>1:
            # take the two largest stones
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)
            # compare their weights
            # if x==y, then continue
            if not x==y:
                if x<y:
                    y -= x
                    heapq.heappush(maxHeap, -y)
                else:
                    x -= y
                    heapq.heappush(maxHeap, -x)

            # if x-y, then y = y-x and gets pushed back to heap and x is discarded

        # if length of maxHeap == 1 then return maxHeap[0], else return 0
        if maxHeap:
            return -heapq.heappop(maxHeap)
        else: return 0

        