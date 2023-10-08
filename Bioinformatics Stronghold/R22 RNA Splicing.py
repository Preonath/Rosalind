from Bio import SeqIO
from Bio.Seq import Seq
f=open("R22.txt","r")
sequences=[]
for record in SeqIO.parse(f,"fasta"):
    sequence=""
    for nt in record.seq:
        sequence+=nt
    sequences.append(sequence)

long_seq=sequences[0]
introns=sequences[1:]

for i in range(len(introns)):
    long_seq=long_seq.replace(introns[i],"")
long_seq=Seq(long_seq)
# print(sequences[0])
# print(long_seq)

prot_seq=long_seq.translate(to_stop=True)
print(prot_seq)