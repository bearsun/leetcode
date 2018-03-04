class Solution:
    def checksub(self, sub):
        cur = set()
        for e in sub:
            if e == '.':
                continue
            if int(e) in cur:
                return False
            else:
                cur.add(int(e))
        return True
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check row
        for row in board:
            if not self.checksub(row):
                return False
        
        # check col
        for col in zip(*board):
            if not self.checksub(col):
                return False
        
        # check square
        for irow in (0, 3, 6):
            for icol in (0, 3, 6):
                square = [board[x][y] for x in range(irow, irow + 3) for y in range(icol, icol + 3)]
                if not self.checksub(square):
                    return False
        return True