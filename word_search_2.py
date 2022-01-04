"""
leetcode: https://leetcode.com/problems/word-search-ii/
"""

# trie to search


class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode("*")

    def insert(self, word):

        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode(letter)
            current = current.children[letter]

        current.is_end_of_word = True

    def search(self, word):

        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]

        return current.is_end_of_word

    def startsWith(self, prefix):

        if prefix == "": return True
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False

            current = current.children[letter]

        return True


## word search


def findWords(board, words):

    wordTrie = Trie()

    for word in words:
        wordTrie.insert(word)

    M = len(board)
    N = len(board[0])

    strings = []

    def dfs(row, col, path):

        if row < 0 or col < 0 or row >= M or col >= M or board[row][col] == 0:
            ## stop
            return

        string_lst = path + [board[row][col]]
        string = "".join(string_lst)

        if not wordTrie.startsWith(string):
            # stop
            return
        elif wordTrie.search(string) and not string in strings:
            strings.append(string)

        placeholder = board[row][col]
        board[row][col] = 0
        dfs(row + 1, col, string_lst)
        dfs(row - 1, col, string_lst)
        dfs(row, col + 1, string_lst)
        dfs(row, col - 1, string_lst)
        board[row][col] = placeholder

    for row in range(M):
        for col in range(N):
            dfs(row,col, [])
    
    return strings