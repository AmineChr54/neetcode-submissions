class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = WordDictionary()
            cur = cur.children[c]
        cur.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index, cur):
            if index == len(word):
                return cur.is_end

            c = word[index]

            if c == '.':
                for child in cur.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if c not in cur.children:
                    return False
                return dfs(index + 1, cur.children[c])

        return dfs(0, self)
