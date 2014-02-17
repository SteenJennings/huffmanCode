__author__ = 'mike'
import operator
from src.tree import Tree

from bitarray import bitarray

class HuffmanTree:
    def __init__(self):
        self.root = None

    def createTree(self, freq):
        # given a list of frequencies sort and generate the tree.

        sorted_freq = sorted(freq.items(), key=operator.itemgetter(1))
        #print(type(sorted_freq))
        #put them in the tree

        #wrap all sorted_freq into tree objects

        print("Sorted List:")
        print(sorted_freq)

        tree_list = []
        for i in sorted_freq:
            tree = Tree(i)
            tree_list.append(tree)

        for i in range(len(tree_list) - 1):
            new_tree = Tree(tree_list[0].root[1] + tree_list[1].root[1])
            new_tree.addNodes(tree_list[0], tree_list[1])
            tree_list.pop(0)
            tree_list.pop(0)
            tree_list.append(new_tree)
            # print(new_tree)

        self.root = tree_list[0]
        print("Printing out Huffman Tree")
        self.root.print_tree(0)


    def gen_codes_rec(self, node, string="", results={}):
        if node.left is None or node.right is None:
            return {node.root[0]: string}
        if node.left is not None:
            results.update(self.gen_codes_rec(node.left, string + "0", results))
        if node.right is not None:
            results.update(self.gen_codes_rec(node.right, string + "1", results))
        return results


    def gen_codes(self):
        print("left=0 right=1")
        return self.gen_codes_rec(self.root)

    def leafNode(self, node):
        if node.left == None and node.right == None:
            return node.root[0]
        return None

    def decode_string(self, coded_string):
        #returns a tuple first value is a string the second is the number of encoding bits it has read
        ctr = 0;
        lastFullLetterCtr = 0;
        decodedString = ""

        tempNode = self.root;

        for i in coded_string:
            ctr += 1
            if i == "0":
                tempNode = tempNode.left
            else:
                tempNode = tempNode.right
            checkNone = self.leafNode(tempNode)
            if checkNone != None:
                tempNode = self.root
                decodedString += (checkNone)
                lastFullLetterCtr = ctr


        return (decodedString, lastFullLetterCtr)
