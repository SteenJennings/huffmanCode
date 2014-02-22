

__author__ = 'Mike Schendel'

def encode(to_encode):
    """
    This encodes the string of 1's and 0's that represent a huffman coding into UTF-8 character set
    @param to_encode: This is a string of 1's and 0's that need to be encoded
    @return: a UTF-8 string representing the string parameter
    """
    #get first 8 chars encode as a byte
    if(len(to_encode) % 8 != 0):
       to_encode = to_encode + (8-(len(to_encode) % 8)) * '0'
    myBytes = []
    my_range = int(len(to_encode)/8)
    for j in range (my_range):
        encoded_int = 0
        for i in range(0,8):
            #print((j*8)+i)
            char = to_encode[((j)*8)+i]
            if char == '1':
                encoded_int |= 1 << (7 - i)
        myBytes.insert(j, encoded_int)
        #print(bin(encoded_int))
    #return ''.join(myBytes)
    return bytearray(myBytes)


def decode(to_decode):
    """
    This takes the UTF-8 character encoding and decodes it into a string of 1's and 0's
    @param to_decode: The list to decode
    @return: A string of 1's and 0's
    """
    #go through the list and for each element convert to a binary string
    decoded_str = ''
    for i in to_decode:
        #i is the first element in to_decode
        int_to_decode = int(i)
        truncatedBin = ("{0:b}".format(int_to_decode))
        str = ((8-len(truncatedBin)) * '0') + truncatedBin
        #print(str)
        decoded_str = decoded_str + str


    return decoded_str

