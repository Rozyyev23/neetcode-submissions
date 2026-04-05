class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board)):
                val = board[i][j]

                if val == '.':
                    continue

                box_index = (i // 3) * 3 + (j // 3)

                if val in row[i] or val in col[j] or val in box[box_index]:
                    return False
                row[i].add(val)
                col[j].add(val)
                box[box_index].add(val)
        return True

