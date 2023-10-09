def f(s,k):
    s_len=len(s)
    com=[]
    for i in range(s_len-k+1):
        sub=s[i:i+k]
        com.append(sub)
    M=sorted(com)
    co=len(M)
    for j in range(co):
        print(M[j])
k=int(input())
s=input()
f(s,k)

