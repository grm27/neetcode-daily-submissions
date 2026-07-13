# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        forward = head
        dummy = ListNode(-1, head)

        for _ in range(n):
            forward = forward.next
        
        prev = dummy
        while forward:
            prev = prev.next
            forward = forward.next
        
        prev.next = prev.next.next
        return dummy.next