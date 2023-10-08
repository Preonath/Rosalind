#https://dodona.ugent.be/en/exercises/756526814/#submission-card
from Bio import SeqIO
f = open("R33.txt", "r")
s = f.readline()
mat = [x for x in f.readline().split()]

c = {'':1, 'A':0, 'C':0, 'G':0, 'U':0, 'AA':0, 'AC':0, 'AG':0, 'AU':1, 'CA':0, 'CC':0, 'CG':1, 'CU':0, 'GA':0, 'GC':1, 'GG':0, 'GU':0, 'UA':1, 'UC':0, 'UG':0, 'UU':0}

def catalan(mat):
    if (mat not in c):
        if mat.count('C') != mat.count('G') or mat.count('A') != mat.count('U'):
            c[mat] = 0
        else:
            c[mat] = sum([catalan(mat[1:i]) * c[mat[0]+mat[i]] * catalan(mat[i+1:]) for i in range(1, len(mat), 2)])
    return c[mat]
print(catalan(mat[0]) % 1000000)