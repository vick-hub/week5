import os
import sys


def main():
    sent = input("Enter a sentence: ").split(" ")
    s = []
    s2 = dict()
    for i in sent:
        s.append(i)
    # print(s)
    s1 = list(enumerate(s))
    # print(s1)
    for i in s1:
        if i is not s2:
            s2[i] = 1
        else:
            s2[i] = s2[i] + s2[i + 1]
    for i, j in s2:
        print(i, '->', j)
        return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
