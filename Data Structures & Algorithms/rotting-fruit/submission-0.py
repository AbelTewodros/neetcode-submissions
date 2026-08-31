class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS,COLS=len(grid),len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]


        fresh_fruit=0
        time=0
        q=deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    fresh_fruit+=1
                if grid[i][j]==2:
                    q.append((i,j))
                    
        
        
        while fresh_fruit>0 and q:
            for _ in range(len(q)):
                r,c=q.popleft()
                for nr,nc in directions:
                    row,col=nr+r,nc+c
                    if (0<=row<ROWS and 0<=col<COLS and grid[row][col]==1):
                        grid[row][col]=2
                        fresh_fruit-=1
                        q.append((row,col))
            time+=1
        return time if fresh_fruit==0 else -1

