import string

# charSet = "HvWZc+?YIKLwV.J_7*lDQ}e:(P&xj6GO=5{[b|nkEhmB3C#%1'Mf<2~iR@rAp`/zT4FSd)aoNyg!t,Xq]" + '"u80-s9>U;$^ "'
charSet = string.printable

def encode(inStr, d = " "):
    indexes = []
    for chars in inStr:
        indexes.append(str(charSet.find(chars)))
        boxIndexes = d.join(indexes)
    return(boxIndexes)

def encodeFile(inFile, d = " "):
    with open(inFile) as f:
        data = f.read()
    indexes = []
    for chars in data:
        indexes.append(str(charSet.find(chars)))
        boxIndexes = d.join(indexes)
    with open(inFile, "w") as f:
        f.write(boxIndexes)

def encodeFileLoop(inFile, cap, d = " "):
    print("encoding")
    for i in range(int(cap)):
        encodeFile(inFile, d)

def decode(boxIndexes, d = " "):
    chars = []
    for index in boxIndexes.split(d):
        chars.append(charSet[int(index)])
        boxChars = "".join(chars)
    return(boxChars)

def decodeFile(inFile, d = " "):
    chars = []
    with open(inFile) as f:
        data = f.read()
    for index in data.split(d):
        chars.append(charSet[int(index)])
        boxChars = "".join(chars)
    with open(inFile, "w") as f:
        f.write(boxChars)

def decodeFileLoop(inFile, cap, d = " "):
    print("decoding")
    for i in range(int(cap)):
        decodeFile(inFile, d)