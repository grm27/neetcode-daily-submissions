# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next

            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        p1 = prev
        p2 = slow if not fast else slow.next

        while p1:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True
