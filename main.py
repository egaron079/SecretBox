import sbx
import os

a = True

clear = "cls"

while a:
    os.system(clear)
    i = input("encode, encodeFile, encodeFileLoop, decode, decodeFile, or decodeFileLoop:\n\n")

    if i == "encode":
        os.system(clear)
        b = input("what do you want to encode:\n\n")
        print("\nresult:\n\n" + str(sbx.encode(b)))
        input()
    elif i == "encodeFile":
        os.system(clear)
        b = input("what file do you want to encode:\n\n")
        sbx.encodeFile(b)
        print("\n" + b + " encoded")
        input()
    elif i == "encodeFileLoop":
        os.system(clear)
        b = input("what file do you want to loop encode:\n\n")
        os.system(clear)
        c = input("how many times do you want to encode the file:\n\n")
        os.system(clear)
        sbx.encodeFileLoop(b, c)
        os.system(clear)
        print(b + " loop encoded")
    elif i == "decode":
        os.system(clear)
        b = input("what do you want to decode:\n\n")
        print("\nresult:\n\n" + str(sbx.decode(b)))
        input()
    elif i == "decodeFile":
        os.system(clear)
        b = input("what file do you want to decode:\n\n")
        os.system(clear)
        sbx.decodeFile(b)
        print("\n" + b + " decoded")
        input()
    elif i == "decodeFileLoop":
        os.system(clear)
        b = input("what file do you want to loop decode:\n\n")
        os.system(clear)
        c = input("how many times do you want to decode the file:\n\n")
        os.system(clear)
        sbx.decodeFileLoop(b, c)
        os.system(clear)
        print(b + " loop decoded")
    else:print("invalid command")