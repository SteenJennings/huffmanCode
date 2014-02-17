from src.huffmanTree import HuffmanTree

__author__ = 'mike'


def main():

    freq = {}
    file_name = "text.txt"
    #get the character frequencies
    with open(file_name, 'r') as f:
        parser = f.read(5000)
        while len(parser) > 0:
            for char in parser:
                if not char in freq:
                    freq[char] = 1
                else:
                    freq[char] += 1
            parser = f.read(5000)

    print(freq)

    ht = HuffmanTree()
    ht.createTree(freq)
    codes = ht.gen_codes()
    print(codes)
    encode_file(file_name, codes)
    decode_file("encoding.txt", ht)


def decode_file(file_name, huffman_tree):
    with open("decoding.txt", 'w') as output_file:
        buffer = ""
        with open(file_name, 'r') as f:
            parser = f.read(5000)
            stringToUse = ""
            while len(parser) > 0:
                #TODO need to fix if falls between a encoding
                stringToUse = stringToUse + parser
                stringTuple = huffman_tree.decode_string(stringToUse)
                str = stringTuple[0]
                stringToUse = stringToUse[stringTuple[1]:]

                print(str)
                parser = f.read(5000)



def encode_file(file_name, codes):
    with open("encoding.txt", 'w') as output_file:
        buffer = ""
        with open(file_name, 'r') as f:
            parser = f.read(5000)
            while len(parser) > 0:
                for char in parser:
                    buffer += codes[char]
                parser = f.read(5000)
                output_file.write(buffer)
                buffer = ""


if __name__ == "__main__":
    main()