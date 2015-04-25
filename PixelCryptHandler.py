__author__ = 'dfu3'

import Image, binascii, math
import django.utils.crypto
from Crypto.Random import random

class PixelCrypt:

    def encrypt(self, plainText, fileName):

        picSize = round(math.sqrt( len(plainText) * 8 )) + 1

        hexString = binascii.hexlify(plainText)

        encryptMess = str(bin(int(hexString, 16)))
        encryptMess = encryptMess[2:]

        cipherKey = ""
        finalCrypt = ""

        foundBadSym = True

        while( foundBadSym == True ):

            preKey = django.utils.crypto.get_random_string(len(plainText), allowed_chars='abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()')
            hexString2 = binascii.hexlify(preKey)

            cipherKey = str(bin(int(hexString2, 16)))
            cipherKey = cipherKey[2:]

            numCrypt = int(encryptMess, 2) ^ int(cipherKey, 2)
            finalCrypt = '{0:b}'.format(numCrypt)

            binVal = (int(finalCrypt, 2) ^ int(cipherKey, 2))

            hexString = ""
            hexString += (hex(binVal)[2:-1])
            decryptMess = binascii.unhexlify(hexString)

            symbols = plainText

            foundBadSym = False

            for elem in decryptMess:
                if(elem not in symbols):
                    foundBadSym = True

        finalCrypt += "0"

        img = Image.new("RGB", (int(picSize), int(picSize)), "WHITE")

        i = 0
        for x in xrange((int(picSize))):
            for y in xrange((int(picSize))):

                if( i >= len(finalCrypt) ):
                    break

                if( finalCrypt[i] == "0" ):
                    img.putpixel((x, y),0)

                i +=1

        img.save(fileName, "PNG")

        return cipherKey


    def decrypt(self, fileName, key):

        img = Image.open(fileName)
        size = img.size

        bitList = ""

        for x in xrange(size[0]):
            for y in xrange(size[1]):

                pixVal = img.getpixel((x, y))

                if(pixVal[0] == 0):
                    bitList += "0"

                else:
                    bitList += "1"

        i = len(bitList) - 1

        while(bitList[i] == "1"):
            i -= 1
        bitList = bitList[:i]

        binVal = int(bitList, 2) ^ int(key, 2)

        hexString = ""
        hexString += (hex(binVal)[2:-1])

        decryptMess = binascii.unhexlify(hexString)

        return decryptMess