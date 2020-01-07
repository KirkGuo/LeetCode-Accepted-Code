class Node():
    def __init__(self):
        self.ch = None
        self.stop = False
        self.nexts = []
        self.ch2idx = {}


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = Node()     

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        def insert_ch(node, word):
            if not word:
                node.stop = True
                return
            if word[0] in node.ch2idx:
                insert_ch(node.nexts[node.ch2idx[word[0]]], word[1:])
            else:
                n = Node()
                n.ch = word[0]
                node.ch2idx[n.ch] = len(node.nexts)
                node.nexts.append(n)
                if len(word)==1:
                    n.stop = True
                insert_ch(n, word[1:])
        
        insert_ch(self.data, word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        def search_ch(node, word):
            if not word:
                return node.stop
            if word[0] in node.ch2idx:
                return search_ch(node.nexts[node.ch2idx[word[0]]], word[1:])
            return False
        
        return search_ch(self.data, word)
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        def startWith_ch(node, word):
            if not word:
                return True
            if word[0] in node.ch2idx:
                return startWith_ch(node.nexts[node.ch2idx[word[0]]], word[1:])
            return False
        
        return startWith_ch(self.data, prefix)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
