# DO NOT MODIFY THESE 2 LINES
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET += ALPHABET.upper() + ' .,!?'

def encrypt(msg, shift):
    """
    Takes string msg and an integer shift
    returns new string which is an encrypted version
    of the message
    str, int -> str
    print(encrypt('John', 15)) -> 'YDwC'
    print(encrypt(' ', 6)) -> 'b'
    """
    # remove this pass statement and write the body of your function
    newStr = ''
    for i in range(len(msg)):
        for j in range(len(ALPHABET)):
            if msg[i]==ALPHABET[j]:
                index = j
                break
        newStr += ALPHABET[(index + shift) % len(ALPHABET)]
    return newStr
        


def decrypt(encrypted_msg, shift):
    """
    Takes string encrypted_msg and an integer shift
    returns new string which is a decrypted version
    of the message
    str, int -> str
    print(decrypt('eDUHM', 25)) -> Kevin
    print(decrypt('j.GT', -10000)) -> Ivan
    """
    # remove this pass statement and write the body of your function
    newStr = ''
    for i in range(len(encrypted_msg)):
        for j in range(len(ALPHABET)):
            if encrypted_msg[i]==ALPHABET[j]:
                index = j
                break
        newStr += ALPHABET[(index - shift) % len(ALPHABET)]
    return newStr
        

