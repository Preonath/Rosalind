from itertools import product, permutations
n=int(input())
list_1 =[]
for i in range(1, n+1):
	list_1.append([-1*i,i])
# print(list_1)

list_2=map(list,list(product(*list_1)))
list_3=[]
for i in list_2:
	list_3+=map(list,list(permutations(i)))
print(len(list_3))
for i in list_3:
	print(*i)