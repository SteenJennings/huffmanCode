__author__ = 'Mike Schendel'
import operator
from src.tree import Tree

class HuffmanTree:
    def __init__(self):
        self.root = None

    def createTree(self, freq):
        """
        Given a mapping of frequencies this will create the appropiate Huffman Tree
        @param freq: The dictionary mapping of character to number of times they appear in the plain text
        @return:
        """
        # given a list of frequencies sort and generate the tree.

        sorted_freq = sorted(freq.items(), key=operator.itemgetter(1))
        #print(type(sorted_freq))
        #put them in the tree

        #wrap all sorted_freq into tree objects

        print("Sorted List:")
        print(sorted_freq)

        tree_list = []
        #Create a Tree for each single frequency so that they can be added together.
        #This is a recursive pattern
        for i in sorted_freq:
            tree = Tree(i)
            tree_list.append(tree)

        #Pop of the two lowest character frequencies and create a single combined tree.
        # Then put these frequencies back in the begining of the list.
        for i in range(len(tree_list) - 1):
            new_tree = Tree(tree_list[0].root[1] + tree_list[1].root[1])
            new_tree.addNodes(tree_list[0], tree_list[1])
            tree_list.pop(0)
            tree_list.pop(0)

            #if the list of trees is empty I have finished and put the new tree in the list as the final tree
            if len(tree_list) == 0:
                tree_list.append(new_tree)
            else:
                #Go through tree list and add it in sorted order
                #Linear here is fine since on average it will be towards the begining of the list
                # #(Look at analysis of character frequencies)
                for j in range(len(tree_list)):
                    if tree_list[j].root[1] >= new_tree.root[1]:
                        tree_list.insert(j-1, new_tree)
                        break
                    if j == len(tree_list)-1:
                        #at end of list so just append it (Worst case senario)
                        tree_list.append(new_tree)

            #tree_list.append(new_tree)
            # print(new_tree)

        self.root = tree_list[0]
        print("Printing out Huffman Tree")
        self.root.print_tree(0)


    def gen_codes_rec(self, node, string="", results={}):
        """
        Generates the codes and stores them in results so they can easily be retreived when encoding the text
        @param node: the current node
        @param string: the string of 1's and 0's that make up the character code
        @param results: the distionary of all the character to encoding mappings
        @return:
        """
        if node.left is None or node.right is None:
            return {node.root[0]: string}
        if node.left is not None:
            results.update(self.gen_codes_rec(node.left, string + "0", results))
        if node.right is not None:
            results.update(self.gen_codes_rec(node.right, string + "1", results))
        return results


    def gen_codes(self):
        """
        Recursive caller to generate the Huffman Codes for each character
        @return: returns the dictionary mapping of characters to binary code
        """
        print("left=0 right=1")
        return self.gen_codes_rec(self.root)

    def leafNode(self, node):
        if node.left == None and node.right == None:
            return node.root[0]
        return None

    def decode_string(self, coded_string):
        """
        Given a string of 1's and 0's this follows the tree until it hits a leaf which successfully decodes a character
        @param coded_string: The encoded string of 1's and 0's
        @return: A tuple of the full string it decoded and a counter to signal the left over undeoced coded_string
        """
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
