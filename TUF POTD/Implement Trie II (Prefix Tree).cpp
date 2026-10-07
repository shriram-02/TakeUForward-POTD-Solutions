class Trie:

    def __init__(self):
        self.children = {}
        self.end = 0
        self.prefix = 0

    def insert(self, word):
        node = self

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()

            node = node.children[ch]
            node.prefix += 1

        node.end += 1

    def countWordsEqualTo(self, word):
        node = self

        for ch in word:
            if ch not in node.children:
                return 0

            node = node.children[ch]

        return node.end

    def countWordsStartingWith(self, prefix):
        node = self

        for ch in prefix:
            if ch not in node.children:
                return 0

            node = node.children[ch]

        return node.prefix

    def erase(self, word):
        node = self

        for ch in word:
            node = node.children[ch]
            node.prefix -= 1

        node.end -= 1