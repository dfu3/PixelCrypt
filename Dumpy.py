__author__ = 'dfu3'
from Crypto.Random import random


randx1 = random.randint(0, 1000000)
randy1 = random.randint(0, 1000000)

randx2 = random.randint(0, 1000000)
randy2 = random.randint(0, 1000000)

randx3 = random.randint(0, 1000000)
randy3 = random.randint(0, 1000000)

keyList = [randx1, randy1, randx2, randy2, randx3, randy3]

for i in range(1, len(keyList), 2):
    print(i)

for i in keyList:
    print(i)

keyList = keyList.reverse()

# for i in keyList:
#     print(i)
