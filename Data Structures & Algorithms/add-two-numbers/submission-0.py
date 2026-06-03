# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        res = ListNode()
        carry_over = 0

        curr = res
        while l1 and l2:
            curr.next = ListNode()
            curr = curr.next
            node_sum = l1.val + l2.val + carry_over
            curr.val = node_sum % 10
            carry_over = node_sum // 10
            l1 = l1.next
            l2 = l2.next

        while l1:
            curr.next = ListNode()
            curr = curr.next
            node_sum = l1.val + carry_over
            curr.val = node_sum % 10
            carry_over = node_sum // 10
            l1 = l1.next

        while l2:
            curr.next = ListNode()
            curr = curr.next
            node_sum = l2.val + carry_over
            curr.val = node_sum % 10
            carry_over = node_sum // 10
            l2 = l2.next

        if carry_over:
            curr.next = ListNode()
            curr = curr.next
            curr.val = carry_over

        return res.next
