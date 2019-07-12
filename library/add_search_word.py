import math

class Node:
    def __init__(self, char, parent, children):
        self.char = char
        self.parent = parent
        self.children = children
        
class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node("*", None, {})
        
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
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
        node.children["*"] = next_node

    def search_helper(self, word, node, i) -> bool:
        if (i == len(word)):
            if "*" in node.children:
                return True
            else:
                return False
        else:
            if word[i] == ".":
                boolean = False
                for child in node.children:
                    boolean = boolean | self.search_helper(word, node.children[child], i + 1)
                return boolean
            elif word[i] in node.children:
                node = node.children[word[i]]
                return self.search_helper(word, node, i + 1)
            else:
                return False


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        return self.search_helper(word, node, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)