import random


l1 = random.sample(range(0, 100), 100)
print(l1)
new_l = []
add = 0
for number in l1:
    add += number
    new_l.append(add)
print(f" Cumulative sum pairs: {new_l}")

new_l1 = []
for t in range(len(l1)-1):
    r = l1[t] + l1[t + 1]
    new_l1.append(r)
print(f" Sum adjoining pairs: {new_l1}")

new_l2 = []
# s1 = 0
# s2 = 1
la = []
lb = []
for i in range(len(l1)-4):
    a = l1[i] + l1[i + 2] + l1[i + 4]
    b = l1[i + 1] + l1[i + 2] + l1[i + 4]
    la.append(a)
    lb.append(b)
    new_l2.append(list(zip((la, lb))))
# print(new_l2)
