import io

__author__ = 'Mike Schendel'

from src import binaryEncoding
from src.huffmanTree import HuffmanTree

__author__ = 'mike'


def main():

    freq = {}
    file_name = "sample_long.txt"
    #get the character frequencies, by reading the file
    with io.open(file_name, 'r', encoding='utf-8') as f:
        parser = f.read(5000)
        while len(parser) > 0:
            for char in parser:
                if not char in freq:
                    freq[char] = 1
                else:
                    freq[char] += 1
            parser = f.read(5000)

    print(freq)
    #create a new huffman tree
    ht = HuffmanTree()
    ht.createTree(freq)
    #Generates the codes for each letter to represent
    codes = ht.gen_codes()
    print(codes)
    print('Encoding file')
    #Encode the file given the previously calculated codes and write to file
    encode_file(file_name, codes)
    print('Decoding file')
    #Decode and write the file
    decode_file("encoding.txt", ht)

def decode_file(file_name, huffman_tree):
    """
    This decodes an ecoded file and prints it to a file
    @param file_name: the encoded file to read form
    @param huffman_tree: the huffman tree created during encoding
    @return:
    """
    with open("decoding.txt", 'w', encoding='utf-8') as output_file:
        buffer = ""
        with io.open(file_name, 'rb') as f:
            #read 5000 bytes
            parser = binaryEncoding.decode(f.read(5000))
            stringToUse = ""
            while len(parser) > 0:
                stringToUse = stringToUse + parser
                stringTuple = huffman_tree.decode_string(stringToUse)
                str = stringTuple[0]
                stringToUse = stringToUse[stringTuple[1]:]

                print(str)
                output_file.write(str)
                parser = binaryEncoding.decode(f.read(5000))



def encode_file(file_name, codes):
    """
    This encodes a plaintext file and prints the encoding to a file
    @param file_name: The plaintext file
    @param codes: The dictionary of character codes
    @return:
    """
    with io.open("encoding.txt", 'wb') as output_file:
        buffer = ""
        with open(file_name, 'r', encoding='utf-8') as f:
            parser = f.read(5000)
            while len(parser) > 0:
                for char in parser:
                    #The actual encoding of the file
                    buffer += codes[char]
                parser = f.read(5000)
                string_to_write = binaryEncoding.encode(buffer)
                output_file.write(string_to_write)
                buffer = ""


if __name__ == "__main__":
    main()