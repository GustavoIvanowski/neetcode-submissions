class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # improve data structure
        rows = {}
        columns = {}
        squares = {}
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                square = i//3 * 3 + j//3
                if val == ".": continue
                if i not in rows: rows[i] = set()
                if j not in columns: columns[j] = set()
                if square not in squares: squares[square] = set()
                if (val in rows[i] or val in columns[j] or val in squares[square]):
                    return False
                rows[i].add(val)
                columns[j].add(val)
                squares[square].add(val)
        return True