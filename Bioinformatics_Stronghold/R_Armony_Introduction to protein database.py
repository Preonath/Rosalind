from Bio import ExPASy
from Bio import SwissProt



f=open('Rprotein.txt')

id= f.read()
protein_info= ExPASy.get_sprot_raw(id)
new_file= SwissProt.read(protein_info)

l = []

for i in new_file.cross_references:
    if i[0] == 'GO' and i[2][0]=='P':
        m=i[2].strip('P:') # use strip to remove 'P:'
        l.append(m)

for n in l:
    print(n)
