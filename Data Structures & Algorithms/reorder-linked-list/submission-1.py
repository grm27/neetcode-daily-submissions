# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(-1, head)
        slow, fast = dummy, dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        p = slow.next
        slow.next = None
        prev = None
        while p:
            next = p.next
            p.next = prev
            prev = p 
            p = next
        
        p1 = head
        p2 = prev
        while p1 and p2:
            next1 = p1.next
            next2 = p2.next
            p1.next = p2
            p2.next = next1
            p2 = next2
            p1 = next1
        
        