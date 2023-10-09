import sys
with open("rosalind_ba7b_1.txt", 'r') as file:
 n = int(file.readline())
 j = int(file.readline())
 D = []
 # print(n,j)
 lines = file.readlines()
 # print(lines)
 for line in lines:
     line = line.split()
     # print(line)
     D.append([int(elem) for elem in line])
#print(D)
limb_len = sys.maxsize
for i in range(len(D)):
    for k in range(len(D[i])):
        if (i != j) and (j != k) and (i != k):
            temp = (D[i][j] + D[j][k] - D[i][k])/2
            limb_len = min(limb_len, temp)
print(int(limb_len))
