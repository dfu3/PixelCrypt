__author__ = 'dfu3'
import PixelCryptHandler

handler = PixelCryptHandler.PixelCrypt()


file = open("largeDataSet.txt", "r")

cont = file.read()

key = handler.encrypt(cont, "finalTest")

decryptedText = handler.decrypt("finalTest", key)

print(decryptedText)