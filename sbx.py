import random

def encodeStr(inStr, seed = random.randint(10, 64)):
    bits = []
    for chars in inStr:
        boxChrs = ord(chars) * seed
        bits.append(chr(boxChrs))
    bits.append(str(seed))
    return("".join(bits))

def decodeStr(inStr):
    seed = inStr[-2:]
    code = inStr[:-2]
    bits = []
    for chars in code:
        boxChrs = ord(chars) / int(seed)
        bits.append(chr(int(boxChrs)))
    return("".join(bits))
