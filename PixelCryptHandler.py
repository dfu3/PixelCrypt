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

        randx1 = random.randint(0, 1000000)
        randy1 = random.randint(0, 1000000)

        randx2 = random.randint(0, 1000000)
        randy2 = random.randint(0, 1000000)

        randx3 = random.randint(0, 1000000)
        randy3 = random.randint(0, 1000000)

        keyList = [randx1, randy1, randx2, randy2, randx3, randy3]

        for i in range(0, len(keyList), 2):
            img = img.offset(keyList[i], keyList[i + 1])

        key = [0, 0, 0, 0, 0, 0]
        count = 1

        for i in keyList:
            key[len(keyList) - count] = i
            count += 1


        img.save(fileName, "PNG")


        return key


    def decrypt(self, fileName, keyList):

        img = Image.open(fileName)

        for i in range(0, len(keyList), 2):
            img = img.offset(-(keyList[i + 1]), -(keyList[i]))

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

        for bit in bitList:

            decNum *= 2

            if(bit == "1"):
                decNum += 1

        hexString = ""
        hexString += (hex(decNum)[2:-1])

        decryptMess = binascii.unhexlify(hexString)

        return decryptMess