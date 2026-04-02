# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        fast = head
        slow = head
        prev = None
        for i in range(n):
            print(i)
            fast = fast.next
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        if not prev: #Fast loop never ran again
            return head.next
        prev.next = slow.next
        return head
