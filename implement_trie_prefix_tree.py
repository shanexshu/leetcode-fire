class Trie:

    def __init__(self, node=""):
        """
        Initialize your data structure here.
        """
        self.node = node
        self.dic = {}
        self.children = []
        self.isEnd = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            self.isEnd = True
            return
        if word[0] not in self.dic:
            newchild = Trie(word[0])
            self.children.append(newchild)
            self.dic[word[0]] = len(self.children)-1
        index = self.dic[word[0]]
        self.children[index].insert(word[1:])
            

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        if not word:
            return self.isEnd
        if word[0] not in self.dic:
            return False
        return self.children[self.dic[word[0]]].search(word[1:])
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not prefix:
            return True
        if prefix[0] not in self.dic:
            return False
        return self.children[self.dic[prefix[0]]].startsWith(prefix[1:])


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)