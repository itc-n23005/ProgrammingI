# P203を正しい形に直しています
import os
import sys

max = 2
print(sys.getdefaultencoding())
print(os.path.basename(os.getcwd()))
for i in range(3):
    print(i, end=" ")
    if max > i:
        print(max)
    else:
        print("#")
