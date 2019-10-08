__author__ = 'Phil'

encrypted = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
decrypted = ""

for letter in encrypted:
    if(letter == " " or letter == "." or letter == "'" or letter == "(" or letter == ")"):
        decrypted = decrypted + letter
    else:
        if(ord(letter) == 121):
            decrypted = decrypted + "a"
        elif(ord(letter) == 122):
             decrypted = decrypted + "b"
        else:
            decrypted = decrypted + chr(ord(letter) + 2)


print(decrypted)

#for the url: map -> ocr
