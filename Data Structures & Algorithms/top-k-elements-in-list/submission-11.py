class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Optimal Solution:
        We need to count the number of times ints appear and store them
        We can use the Counter method that will use a hashmap to do that for us
        That looks like:
        [3,4,4,5,5,5]
        {3:1, 4:2, 5:3} k = int, val = freq

        Reverse it so that keys are freq and ints are vals
        {1:3, 2:4, 3:5}
        The key intuition here is that:
            If there was only one integer present,
            That integer could only appear n times
            So no integer can appear more than n times
        So we iterate backwards from n and check if that number exists in our map
        '''
        hmap = Counter(nums)
        freqmap = {}
        for key,val in hmap.items():
            if val not in freqmap:
                freqmap[val] = []
            freqmap[val].append(key)
        
        i = len(nums)
        n = 0
        res = []
        while i > 0 :
            if i in freqmap:
                for num in freqmap[i]:
                    res.append(num)
                n+=len(freqmap[i])
                if n == k:
                    break
            print(f"i:{i}, n:{n}, k:{k}")
            i-=1
        return res

'''
One of the issue I was not able to address is a case such as:
[1,2] where k = 2
The result would be [1,2]
our map would be modified to be a list to reflect both values being present
{1: [1,2]}
and iterating through the list would take O(n) in worst case

Talks about bucket sort:
Acknowledges about using an array that uses indices as count and the values at those indices are list of nums that occurred

'''


        



