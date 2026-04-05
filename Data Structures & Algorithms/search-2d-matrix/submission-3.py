class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:
            m_idx = (left + right) // 2
            row = m_idx // cols
            col = m_idx % cols

            guess = matrix[row][col]

            if guess == target:
                return True
            if guess > target:
                right = m_idx - 1
            else:
                left = m_idx + 1

        return False
