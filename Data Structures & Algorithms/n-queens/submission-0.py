class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        subset=[]
        off_diag1=set()
        off_diag2=set()
        off_col=set()
        def dfs(row):
            if row>=n:
                if len(subset)==n:
                    res.append(subset.copy())
                return
            
            for col in range(n):
                diag1=row+col
                diag2=row-col
                if diag1 in off_diag1 or diag2 in off_diag2 or col in off_col:
                    continue
                off_diag1.add(diag1)
                off_diag2.add(diag2)
                off_col.add(col)
                str=''
                while len(str)<col:
                    str+='.'
                str+='Q'
                while len(str)<n:
                    str+='.'
                subset.append(str)
                dfs(row+1)
                subset.pop()
                off_diag1.remove(diag1)
                off_diag2.remove(diag2)
                off_col.remove(col)
        dfs(0)
        return res


            
