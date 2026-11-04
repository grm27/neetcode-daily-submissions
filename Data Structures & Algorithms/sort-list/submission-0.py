# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(l1, l2):
            head = p = ListNode()

            while l1 and l2:
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next

            if l1:
                p.next = l1

            if l2:
                p.next = l2

            return head.next

        def mergeSort(head):
            if not head or not head.next:
                return head

            slow, fast = head, head.next
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            next = slow.next
            slow.next = None
            return merge(mergeSort(head), mergeSort(next))

        return mergeSort(head)
