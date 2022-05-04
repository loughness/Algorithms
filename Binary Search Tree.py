class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:
    def __init__(self, root):
        # create the first node as the root
        self.root = Node(root)

    def show(self, traversal_type):
        if traversal_type == 'preorder':
            ans = self.preorder(bt.root, '')
            print (ans[:-1])
        elif traversal_type == 'inorder':
            ans = self.inorder(bt.root, '')
            print (ans[:-1])
        else:
            print ('Traversal type is invalid!')

    def preorder(self, start, traversal):
        if start:
            traversal += (str (start.value) + '-')
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str (start.value) + '-')
            traversal = self.inorder(start.right, traversal)
        return traversal
#      4
#    /   \
#   2     6
#  / \   / \
# 1   3 5   7

bt = BinaryTree(4)
bt.root.left = Node(2)
bt.root.left.right = Node(3)
bt.root.left.left = Node(1)
bt.root.right = Node(6)
bt.root.right.left = Node(5)
bt.root.right.right = Node(7)

# print (bt.show('preorder'))
bt.show('preorder')
bt.show('inorder')
bt.show('inorder')