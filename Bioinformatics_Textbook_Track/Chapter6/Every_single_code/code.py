def rev_compl(st):
    nn = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join(nn[n] for n in reversed(st))

f = open("rosalind_ba6e.txt", "r")
ff=f.readlines()
k_m=ff[0]
p=int(n)
DNA_1=ff[1]
DNA_2=ff[2]
k_mer=int(k_m)

d={}
dd={}

for i in range(len(DNA_1)-k_mer):
    l=[]
    s=DNA_1[i:i+k_mer]
    # print(s)
    ss=DNA_2[i:i+k_mer]
    r=rev_compl(s)
    l.append(s)
    l.append(r)
    d[i]=l
    dd[i]=ss

for k,v in d.items():
    for x,y in dd.items():
        if(v[0]==y or v[1]==y):
            m="({}, {})"
            print(m.format(k,x))
