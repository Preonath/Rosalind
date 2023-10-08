dna=input()
s=input()
dna_l=len(dna)
s_l=len(s)
ans=[]
for i in range(dna_l-s_l+1):
    sub=dna[i:i+s_l]
    if(sub==s):
        ans.append(i)
print(*ans)