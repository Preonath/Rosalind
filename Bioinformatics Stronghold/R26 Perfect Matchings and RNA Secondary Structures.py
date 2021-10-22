# https://dodona.ugent.be/nl/exercises/425265453/



from Bio import SeqIO
from math import factorial

handle=open("R26.fasta","r")
sequence_list=''
for i in SeqIO.parse(handle,"fasta"):

    # print(i)
    sequence_list=i.seq

AU=0
GC=0
for j in sequence_list:
    if(j=='A'):
        AU+=1
    elif(j=='G'):
        GC+=1
print(AU,GC)
perfect_match=factorial(AU)*factorial(GC)

print(perfect_match)