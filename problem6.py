import os
import sys


def main():
    sent = input("Enter a sentence: ").split(" ")
    s = []
    s2 = dict()
    for i in sent:
        s.append(i)
    # print(s)
    s1 = enumerate(s)
#     print(s1)
    for i in s1:
        if i is not s2:
            s2[i] = 1
        else:
            s2[i] = s2[i] + 1
    for k, v in s2:
        print(k, '->', v)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
