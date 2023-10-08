n,k=map(int,input().split())
fact=1
for i in range(k):
    fact*=(n-i)
par_modulo=fact%1000000
print(par_modulo)