# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        Def a two pointer situation.
        Does one pointer have to be at the start and the other at the end?
            That wont work because references dont go backwards
        Need to create a new listnode that points to the beginning
        [0,1,2,3] [4,5,6]
        So the division needs to be n//2
        We could initially run through the list to get a value for n
        Then we run it again, but set one pointer at n//2 while the other is at 0
            Forgot that we also have to reverse the second half
        Then, using the new listnode, we attach one after the other
        '''
        n = 0
        cur = head
        while cur:
            n+=1
            cur = cur.next
        halfpoint = n//2
        p1 = head
        p2 = head
        for i in range(halfpoint):
            if i == halfpoint-1:
                tmp = p2.next
                p2.next = None
                p2 = tmp
            else:
                p2 = p2.next
        
        cur = p2
        prev = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        p2 = prev


        i = 0 
        prev = None
        while (p1 and p2) and i<n:
            if i%2 == 0:
                tmp1 = p1.next
                tmp2 = p2.next
                prev = p2
                p1.next = p2
                p2.next = tmp1

                p1 = tmp1
                p2 = tmp2
                i+=1
            else:
                i+=1
        if p2:
            prev.next = p2
        print(prev.val)



        
        