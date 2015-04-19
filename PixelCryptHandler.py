__author__ = 'dfu3'

import Image, binascii, math
from Crypto.Random import random

class PixelCrypt:

    def encrypt(self, plainText, fileName):

        picSize = round(math.sqrt( len(plainText) * 8 )) + 1

        hexString = binascii.hexlify(plainText)

        encryptMess = str(bin(int(hexString, 16)))
        encryptMess = encryptMess[2:]

        img = Image.new("RGB", (int(picSize), int(picSize)), "WHITE")

        i = 0
        for x in xrange((int(picSize))):
            for y in xrange((int(picSize))):

                if( i >= len(encryptMess) ):
                    break

                if( encryptMess[i] == "0" ):
                    img.putpixel((x, y), 0)

                i +=1

        randx = random.randint(0, 10000)
        randy = random.randint(0, 10000)

        offSetKey = [randx, randy]

        new_img = img.offset(randx, randy)

        new_img.save(fileName, "PNG")

        return offSetKey


    def decrypt(self, fileName, key):

        img = Image.open(fileName)

        xOff = key[0]
        yOff = key[1]

        new_img = img.offset(-xOff, -yOff)

        size = img.size
        bitList = ""

        for x in xrange(size[0]):
            for y in xrange(size[1]):

                pixVal = new_img.getpixel((x, y))

                if(pixVal[0] == 0):
                    bitList += "0"

                else:
                    bitList += "1"


        i = len(bitList) -1

        while(bitList[i] == "1"):
            i -= 1
        bitList = bitList[:i + 1]

        decNum = 0

        for bit in bitList:

            decNum *= 2

            if(bit == "1"):
                decNum += 1

        hexString = ""
        hexString += (hex(decNum)[2:-1])

        decryptMess = binascii.unhexlify(hexString)

        return decryptMess