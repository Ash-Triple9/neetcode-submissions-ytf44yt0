import heapq
import math 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        Working with a list of lists where the data is coordinates
        Also given an integer k
        Have to return the k closest points to the origin (0,0)
        The way to calculate distance is by using the Euclidean distance algorithm
        (sqrt((x1 - x2)^2 + (y1 - y2)^2))

        k will always be > 0
        coordinates can be from -100 to 100, which won't matter in terms of finding distance

        Slight note: the euclidean distance formula can be simplified to 
        (sqrt((x1)^2 + (y1)^2)) since we are using (0,0) as our second set of coords

        What we can do as a basic approach is essentially iterate through the list while we have k results,
        and keep track of the minimum one, after every loop we remove the minimum set out of the list and redo it until we have k closest.
        That would be O(n*k) time with O(1) space

        Another approach is to create a hashmap with distance as keys and coords as values.
        The distances are then put through a min heap structure using heap
        We then pull k distances from the heap, and match the value to the hashmap to obtain the coords.
        This should be O(n) time with O(n) space
        '''

        hashmap = {}
        distance_heap = []

        for coord in points:
            x = coord[0]
            y = coord[1]
            distance = math.sqrt(x**2 + y**2)
            if distance not in hashmap:
                hashmap[distance] = []
            hashmap[distance].append([x,y])
            heapq.heappush(distance_heap, distance)
        
        i = 0
        res = []
        while i < k:
            distance = heapq.heappop(distance_heap)
            res.append(hashmap[distance].pop())
            i+=1
        return res

