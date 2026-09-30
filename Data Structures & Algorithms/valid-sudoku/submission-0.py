class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[(i + 1) for i in range(9)] for j in range(9)]
        columns = [[(i + 1) for i in range(9)] for j in range(9)]
        squares = [[(i + 1) for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                square = i//3 * 3 + j//3
                if val == ".": continue
                val = int(val)
                if not (val in rows[i] and val in columns[j] and val in squares[square]):
                    return False
                rows[i].remove(val)
                columns[j].remove(val)
                squares[square].remove(val)
        return True