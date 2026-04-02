class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        Given an array called tasks where the contents of it are uppercase chars
        Given an int n

        Tasks can be completed in any order
        Each cycle = one task done
        Identical tasks must have a cycle interval of n 

        So for instance:
        x x y y with n=2, this means any identical tasks must have an interval of 2 other tasks
        it can also go idle to fulfill that requirement
        
        '''

        count = Counter(tasks) # To get the frequency of the tasks present
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time+=1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
        