"""
leetcode: https://leetcode.com/problems/implement-trie-prefix-tree/
"""

## trie node
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