# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reversell(self, head, k):
        cur = head
        prev = None
        tmp = None
        # Have to save head.next to point to the next k nodes
        for i in range(k):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        head.next = tmp
        
        return [head, prev]

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        cur = head
        retNode = ListNode()
        dummy = head
        i = 0
        flag = True # To indicate the first loop
        runningTail = None
        while cur:
            if i == (k-1):
                tmp = cur.next if cur else None
                if flag:
                    [tail, retNode] = self.reversell(dummy, k)
                    print(retNode.val, tail.val)
                    runningTail = tail
                    cur = tmp
                    dummy = tmp
                    flag = False
                else:
                    [tail, front] = self.reversell(dummy, k)
                    runningTail.next = front
                    runningTail = tail
                    print(front.val, tail.val)
                    cur = tmp
                    dummy = tmp
                i = 0
            cur = cur.next if cur else None
            i+=1
            
        return retNode
                

        