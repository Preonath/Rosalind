import math
import itertools
n=int(input())
per=itertools.permutations(list(range(1, n + 1)))
fact=math.factorial(n)
print(fact)
for i,s in enumerate(list(per)):
   # to remove the braket according to output
   l=''
   for j in s:
      l+=str(j) + ' '
   print(l)