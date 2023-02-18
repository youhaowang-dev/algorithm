# Hash Table, String, Design, Trie
# https://leetcode.com/problems/implement-trie-prefix-tree/
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys
# in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

class Node:
    def __init__(self):
        self.is_word = False
        self.letter_to_node = dict()


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.letter_to_node:
                node.letter_to_node[letter] = Node()
            node = node.letter_to_node[letter]

        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.letter_to_node:
                return False
            node = node.letter_to_node[letter]

        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter not in node.letter_to_node:
                return False
            node = node.letter_to_node[letter]

        return True
