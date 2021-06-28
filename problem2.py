import random


l1 = random.sample(range(0, 100), 100)
print(l1)
new_l1 = []
c = 0
i = 0
while i <= len(l1)-1:
    c += l1[i]
    new_l1.append(c)
#    print(new_l1)
    i = i + 1
print(new_l1)

new_l2 = []
j = 0
while j <= len(l1):
    t = (l1[j] + l1[j + 1])
    new_l2.append(t)
    j += 1
print(new_l2)
