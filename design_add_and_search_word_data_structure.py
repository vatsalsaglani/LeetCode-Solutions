"""
leetcode: https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""

# trie to add and search word

# trie node

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
    
    def searchWithDot(self, word):

        # dfs to traverse the tree and reach the end of word

        def dfs(current, word):

            if not word:
                return current.is_end_of_word
            
            ch = word[0]

            if ch == '.':
                for node in [current.children[_] for _ in current.children]:
                    if dfs(node, word[1:]): return True
            
            else:

                if ch in current.children:
                    if dfs(current.children[ch], word[1:]): return True
                else:
                    return False
            
        current = self.root
        return dfs(current, word)

## word dictionary

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word):
        self.trie.insert(word)
    
    def search(self, word):
        return self.trie.searchWithDot(word)