import math

f= open('R28.txt', 'r')

s = f.readline()
array_1 = [float(x) for x in f.readline().split()]
# print(array_1)


cg = s.count('C') + s.count('G')
at = len(s) - cg

array_2 = []
for x in range(len(array_1)):
    array_2.append(math.log10((array_1[x] / 2) ** cg * (.5 - array_1[x] / 2) ** at))
print(*array_2)

