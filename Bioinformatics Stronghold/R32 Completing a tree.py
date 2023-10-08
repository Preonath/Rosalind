sequence=[]
f=open("R32.txt","r")
for i in f:
    split_data=[int(j) for j in i.split()]
    sequence.append(split_data)
node=sequence[0][0]
edges=sequence[1:]
min_edges=node-len(edges)-1
print(min_edges)
