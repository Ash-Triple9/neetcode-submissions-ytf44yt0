# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def merge(self, l1, l2):
        cur = dummy = ListNode()
        while l1 and l2:
            if l1.val< l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        if l1:
            while l1:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
        else:
            while l2:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        return dummy.next
                


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        for i in range(1, len(lists)):
            l1 = lists[i-1]
            l2 = lists[i]
            lists[i] = self.merge(l1, l2)
        return lists[-1] if lists else ListNode().next
        