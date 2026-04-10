class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Optimal solution:
        What was the shortcoming of the brute force?
            Double for loop increases time complexity.
        How to avoid that?
            Here, ordering matters. Indices play a part. 
            And we are looking for the next higher temp always.
        (30,0), (38,1), (30,2), (36,3), (35,4), (40,5), (28,6)
        Indices will tell us the days passed.
        Stack implementation can be done:
        Append to stack if current temp is lower than stack[-1],
            Pop while stack[-1] <= current temp:
                with every pop, insert the difference in indices at the result array, which will have a determined size

        '''
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if not stack or temperatures[i]<=stack[-1][0]:
                stack.append((temperatures[i],i))
            else:
                while stack:
                    if stack[-1][0]>=temperatures[i]:
                        break
                    prev = stack.pop()
                    res[prev[1]] = i - prev[1]
                stack.append((temperatures[i],i))
        return res
            
            

                
        