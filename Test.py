__author__ = 'dfu3'
import PixelCryptHandler
import time



handler = PixelCryptHandler.PixelCrypt()


file = open("largeDataSet.txt", "r")

cont = file.read()

startTime = time.time()

key = handler.encrypt(cont, "test.png")
print('{}{}'.format("write time elapsed: ", (time.time() - startTime) ))

startTime = time.time()

decryptedText = handler.decrypt("test.png", key)
print('{}{}'.format("read time elapsed: ", (time.time() - startTime) ))

print(decryptedText)

