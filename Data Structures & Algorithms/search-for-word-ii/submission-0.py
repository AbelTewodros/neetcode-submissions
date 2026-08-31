class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False
    
    def addWord(self,word):
        curr=self
        for w in word:
            if w not in curr.children:
                curr.children[w]=TrieNode()
            curr=curr.children[w]
        curr.end=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for w in words:
            root.addWord(w)
        ROW,COL= len(board),len(board[0])
        visited,res=set(),set()
        
        def dfs(r,c,node,word):
            if r<0 or c<0 or r>=ROW or c>=COL or (r,c) in visited or board[r][c] not in node.children:
                return 
            visited.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.end:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visited.remove((r,c))
        
        for i in range(ROW):
            for j in range(COL):
                dfs(i,j,root,"")
        return list(res)