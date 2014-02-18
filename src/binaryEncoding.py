

__author__ = 'Mike Schendel'

def encode(to_encode):
    #get first 8 chars encode as a byte
    if(len(to_encode) % 8 != 0):
       to_encode = to_encode + (8-(len(to_encode) % 8)) * '0'
    #print(to_encode)
    bytes = []
    my_range = int(len(to_encode)/8)
    for j in range (my_range):
        encoded_int = 0
        for i in range(0,8):
            #print((j*8)+i)
            char = to_encode[((j)*8)+i]
            if(char == '1'):
                encoded_int = encoded_int | (1<<(7-i))
        bytes.insert(j, (chr(encoded_int)))
        #print(bin(encoded_int))

    return ''.join(bytes)


def decode(to_decode):
    #go through the list and for each element convert to a binary string
    decoded_str = ''
    for i in to_decode:
        #i is the first element in to_decode
        int_to_decode = ord(i)
        truncatedBin = ("{0:b}".format(int_to_decode))
        str = ((8-len(truncatedBin)) * '0') + truncatedBin
        #print(str)
        decoded_str = decoded_str + str


    return decoded_str

