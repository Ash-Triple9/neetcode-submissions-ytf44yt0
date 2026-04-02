import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        '''
        We can use heapq.nlargest(n, list) to find out the kth largest
        integer in our list
        '''
        self.nums = nums
        self.k = k
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        largest = heapq.nlargest(self.k, self.nums)
        return largest[-1]
        
