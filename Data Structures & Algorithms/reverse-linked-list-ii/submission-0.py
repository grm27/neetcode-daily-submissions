# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        
        prev, curr = dummy, head
        
        for _ in range(1, left):
            prev = curr
            curr = curr.next
        
        last, start = prev, curr
        for _ in range(right - left + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        last.next = prev
        start.next = next
        return dummy.next

