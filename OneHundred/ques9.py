__author__ = 'RongbingMiao'

s = "hello world my name is and practice makes perfect and hello world again"

newS = []



for item in s.split():
    newS.append(item)

print(newS)

print(sorted(set(newS)))