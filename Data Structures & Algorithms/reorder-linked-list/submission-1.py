# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev, curr = None, second
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        first, second = head, prev
        while second:
            tmp1 = first.next    # сохраняем следующий у first
            tmp2 = second.next   # сохраняем следующий у second
            first.next = second  # вставляем second после first
            second.next = tmp1   # second указывает на старый first.next
            first = tmp1         # двигаем first
            second = tmp2 