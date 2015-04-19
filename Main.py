__author__ = 'dfu3'

import Image, binascii, math
width = 640
hieght = 640

message = "This is a message to test my program's encryption"

#--------------------------------------------ENCRYPTING--------
picSize = round(math.sqrt( len(message) * 8 )) + 1
encryptMess = str(bin(int(binascii.hexlify(message), 16)))
encryptMess = encryptMess[2:]
print("original: " + message)

img = Image.new("RGB", (int(picSize), int(picSize)), "WHITE")

i = 0
for x in xrange((int(picSize))):
    for y in xrange((int(picSize))):

        if( i >= len(encryptMess) ):
            break

        if( encryptMess[i] == "0" ):
            img.putpixel((x, y), 0)

        i +=1

img.save("myImage.png", "PNG")
#---------------------------------------------<

#--------------------------------------------DECRYPTING--------
size = img.size
bitList = ""

for x in xrange(size[0]):
    for y in xrange(size[1]):

        pixVal = img.getpixel((x, y))

        if(pixVal[0] == 0):
            bitList += "0"

        else:
            bitList += "1"


i = len(bitList) -1

while(bitList[i] == "1"):
    i -= 1
bitList = bitList[:i + 1]

decNum = 0
firstCheck = True

hexString = ""
hexCount = 0

for bit in bitList:

    decNum *= 2

    if(bit == "1"):
        decNum += 1

hexString += (hex(decNum)[2:-1])

decryptWord = binascii.unhexlify(hexString)

print("after decryption: " + decryptWord)
#---------------------------------------------<