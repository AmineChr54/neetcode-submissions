class PrefixTree:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def insert(self, word: str) -> None:
        cur = self
        for i, c in enumerate(word):
            if c not in cur.children:
                cur.children[c] = PrefixTree()
            cur = cur.children[c]
        cur.is_end_of_word = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return cur.is_end_of_word
            

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return True
        