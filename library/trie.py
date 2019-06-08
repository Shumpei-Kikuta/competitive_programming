import math

class Node:
    def __init__(self, char, parent, children):
        self.char = char
        self.parent = parent
        self.children = children
        
class Trie:
    def __init__(self):
        self.root = Node("*", None, {})

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        i = 0
        while(len(word) > i):
            potential_next = node.children.get(word[i])
            if potential_next is not None:
                node = potential_next
                pass
            else:
                next_node = Node(word[i], node, {})
                node.children[word[i]] = next_node
                node = next_node
            i += 1
        next_node = Node("*", None, {})
        node.children[word[i]] = next_node
        
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        i = 0
        node = self.root
        while(i < len(word)):
            if word[i] in node.children:
                node = node.children[word[i]]
            else:
                return False
            i += 1
        if "*" in node.children:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        i = 0
        node = self.root
        while(i < len(prefix)):
            if prefix[i] in node.children:
                node = node.children[prefix[i]]
            else:
                return False
            i += 1
        return True