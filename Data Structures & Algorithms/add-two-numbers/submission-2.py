# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digit1 = digit2 = 0
        cur1, cur2 = l1, l2
        i = j = 0

        while cur1:
            digit1+= cur1.val * (10**i)
            cur1 = cur1.next
            i+=1
        
        while cur2:
            digit2+= cur2.val * (10**j)
            cur2 = cur2.next
            j+=1
        
        total = digit1 + digit2
        res = None
        cur3 = res
        if total == 0:
            return ListNode()
        while total > 0:
            rem = total % 10
            if not res:
                res = ListNode(rem)
                cur3 = res
            else:
                cur3.next = ListNode(rem)
                cur3 = cur3.next
            total//=10
        return res

