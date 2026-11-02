# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        le_than, gre_than = ListNode(), ListNode()
        p1, p2 = le_than, gre_than

        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next

        p1.next = gre_than.next
        p2.next = None

        return le_than.next
