# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        curr = head
        count = 0

        while curr:
            curr = curr.next
            count += 1

        index = count - n

        if index == 0:
            return head.next

        curr = head

        for i in range(count - 1):
            if (index - 1) == i:
                curr.next = curr.next.next
                break
            curr = curr.next

        return head