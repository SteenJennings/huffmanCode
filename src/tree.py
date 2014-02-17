__author__ = 'mike'


class Tree:
    def __init__(self, root):
        #root is a tuple of char, freq
        self.root = root
        self.left = None
        self.right = None


    def __str__(self):
        return str(self.root)


    def print_tree(self, tabs):
        if self.left is not None:
            self.left.print_tree(tabs+1)
        print("\t"*tabs + str(self.root))
        if self.right is not None:
            self.right.print_tree(tabs+1)


    def addNodes(self, tree1, tree2):
        #frequency of two nodes added
        self.root = (tree1.root[0] + tree2.root[0], tree1.root[1] + tree2.root[1])
        self.left = tree1
        self.right = tree2
        #while temp != None:
