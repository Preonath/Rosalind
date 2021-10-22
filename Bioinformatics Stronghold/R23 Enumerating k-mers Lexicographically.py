#same problem:itertools_product and R19

import itertools
n=int(input("Number of repeat: "))
s= list((i) for i in input("Enter the string:").strip().split())
per=itertools.product(s,repeat=n)

#
res = []
for i in per:
    if i not in res:
            res.append(i)
for i,s in enumerate(res):
    l=''
    for j in s:
        l+=str(j)
    # print(len(l))
    print(l)