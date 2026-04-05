# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        # 1. Сдвигаем fast вперед, создавая дистанцию n + 1
        for _ in range(n + 1):
            fast = fast.next

        # 2. Двигаем оба, пока fast не уйдет за пределы списка
        while fast:
            fast = fast.next
            slow = slow.next

        # 3. Удаляем узел: просто перебрасываем ссылку "через одного"
        slow.next = slow.next.next

        return dummy.next