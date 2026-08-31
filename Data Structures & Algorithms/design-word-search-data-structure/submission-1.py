class TrieNode:
    
    def __init__(self):
        self.children={}
        self.end=False


class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for w in word:
            if w not in curr.children:
                curr.children[w]=TrieNode()
            curr=curr.children[w]
        curr.end=True

    def search(self, word: str) -> bool:
        curr=self.root
        def dfs(curr,i):
            if i==len(word):
                return curr.end
            if word[i]=='.':
                saved=curr
                for key in saved.children.keys():
                    return dfs(curr.children[key],i+1)
            if word[i] not in curr.children:
                return False
            return dfs(curr.children[word[i]],i+1)
          
        return dfs(curr,0)
        
