class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr:
                return 0  # Возвращаем ВЫСОТУ 0 для пустого узла

            left = dfs(curr.left)
            if left == -1: return -1 # "Пробрасываем" ошибку наверх

            right = dfs(curr.right)
            if right == -1: return -1 # "Пробрасываем" ошибку наверх

            # Теперь left и right — это числа (высоты). Можем их сравнивать!
            if abs(left - right) > 1:
                return -1 # Нашли дисбаланс — сигналим об этом
            
            # Если всё ок, возвращаем высоту этого узла родителю
            return 1 + max(left, right)
            
        # Запускаем и проверяем: если не -1, значит всё сбалансировано
        return dfs(root) != -1