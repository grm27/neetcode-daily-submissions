# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head

        while p.next:
            next = p.next
            gcd = self.gcd(p.val, p.next.val)
            p.next = ListNode(gcd, p.next)
            p = next
        
        return head







    def gcd(self, a, b):
        if a < b:
            a, b = b, a
        
        while b > 0:
            r = a % b
            a = b
            b = r
        
        return a
        