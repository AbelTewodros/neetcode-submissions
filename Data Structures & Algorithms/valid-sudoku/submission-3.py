class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       Row = defaultdict(set)
       Col = defaultdict(set)
       Box = defaultdict(set)

       for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in Row[i] or board[i][j] in Col[j] or board[i][j] in Box[(i//3,j//3)]:
                    return False
                Row[i].add(board[i][j])
                Col[j].add(board[i][j])
                Box[(i//3,j//3)].add(board[i][j])
       return True
           