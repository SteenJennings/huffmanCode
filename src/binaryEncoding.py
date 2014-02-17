import binascii

__author__ = 'Mike Schendel'

def encode(to_encode):
    #get first 8 chars encode as a byte
    if(len(to_encode) % 8 != 0):
       to_encode = to_encode + (8-(len(to_encode) % 8)) * '0'
    print(to_encode)
    bytes = []
    my_range = int(len(to_encode)/8)
    for j in range (my_range):
        encoded_int = 0
        for i in range(7):
            #print((j*8)+i)
            char = to_encode[((j)*8)+i]
            if(char == '1'):
                encoded_int = encoded_int | (1<<(7-i))
        bytes.insert(j, encoded_int)

    #print((bytearray(bytes)))
    print(bytes)
    return (bytes)


def decode(to_decode):
    #go through the list and for each element convert to a binary string
    for i in to_decode:
        #i is the first element in to_decode
        print(bin(i))
    return to_decode



