'''
File Description: Quick helper class I made that implements a basic binary tree.
'''

class Tree:
    def __init__(self, data, tokenType, left, middle, right):
        self.data = data # holds the value of the node
        self.tokenType = tokenType # holds the type of the value
        self.left = left # left subtree/node
        self.middle = middle # middle subtree/node
        self.right = right # right subree/node
