class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        global INF
        INF=2147483647
        ROW,COL=len(grid),len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        
        def BFS(r,c):
            que=deque([(r,c)])
            visit=[[False]*COL for _ in range(ROW)]
            visit[r][c]=True
            steps=0

            while que:
                for _ in range(len(que)):
                    row,col=que.popleft()
                    if grid[row][col]==0:
                        return steps
                    
                    for cr,cc in directions:
                        nr,nc=row+cr,col+cc
                        if (0<=nr<ROW and 0<=nc<COL and not visit[nr][nc] and grid[nr][nc]!=-1):
                            visit[nr][nc]=True
                            que.append((nr,nc))
                steps+=1
            return INF
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==INF:
                    grid[i][j]=BFS(i,j)


