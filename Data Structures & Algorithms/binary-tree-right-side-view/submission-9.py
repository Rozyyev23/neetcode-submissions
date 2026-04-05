# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
    
        result = []
        queue = deque([root])
    
        while queue:
            level_size = len(queue)
        
            for i in range(level_size):
                node = queue.popleft()
            
            # Если это последний узел на текущем уровне — 
            # значит, это именно то, что мы увидим справа!
                if i == level_size - 1:
                    result.append(node.val)
            
            # Продолжаем стандартный BFS: добавляем детей
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return result