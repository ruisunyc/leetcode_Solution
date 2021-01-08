class Tries:
    def __init__(self):
        self.tree = {}
    def insert(self,word):
        a = self.tree
        for c in word:
            if c not in a:
                a[c] = {}
            a = a[c]
        a['#'] = True
    def start(self,pre):
        a = self.tree
        for i,c in enumerate(pre):
            if c not in a:break
            a = a[c]
            if '#' in a:return pre[:i+1]
        return pre
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trees = Tries()
        for word in dictionary:
            trees.insert(word)
        return ' '.join(trees.start(sen) for sen in  sentence.split(' '))
        # return ' '.join(map(trees.start,sentence.split(' ')))
       
