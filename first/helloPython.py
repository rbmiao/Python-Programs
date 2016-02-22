__author__ = 'RongbingMiao'

import random
import sys
import os

testFile = open("test.txt", "wb")
print(testFile.mode)
print(testFile.name)


testFile.write(bytes("Wrtistteset to daniel\n", "utf8"))
testFile.close()

mFile = open("test.txt", "r+")

testNew = mFile.read()

print(testNew)

mFile.close()

os.remove("test.txt")
