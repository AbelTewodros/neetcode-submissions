class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        original = image[sr][sc]
        def dfs(sr,sc, color):
            if (sr,sc) in visited or sr >= len(image) or sc >= len(image[0]) or sr < 0 or sc < 0:
                return

            elif image[sr][sc] == original:
                visited.add((sr,sc))
                image[sr][sc] = color
                dfs(sr+1,sc,color)
                dfs(sr,sc+1,color)
                dfs(sr-1,sc,color)
                dfs(sr,sc-1,color)
        dfs(sr,sc, color)
        return image
