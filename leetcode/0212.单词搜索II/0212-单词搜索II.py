class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        a = self.data
        for c in word:
            if c not in a:a[c] = {}
            a = a[c]
        a['#'] = word
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not any(board):return []
        m = len(board)
        n = len(board[0])
        tree = Trie()
        for word in words:
            tree.insert(word)
        ans =[]
        def dfs(i,j,treesne):            
            cur = board[i][j] 
            if '#' in treesne:
                ans.append(treesne['#'])
                treesne.pop('#') #»•÷ÿ
            board[i][j]='$'
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=x<m and 0<=y<n and board[x][y]!='$' and  board[x][y] in treesne:
                    dfs(x,y,treesne[board[x][y]])
            board[i][j] =cur #ªÿÀ›
        for i in range(len(board)):
            for j in range(len(board[0])):
                if  board[i][j] in tree.data:
                    dfs(i,j,tree.data[board[i][j]])
        return ans