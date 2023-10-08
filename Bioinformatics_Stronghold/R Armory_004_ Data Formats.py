from Bio import Entrez
from Bio import SeqIO

f=open('rosalind_frmt.txt')
IDs =f.read().strip().split()

Entrez.email = 'preonath2838@.github.com'
handle = Entrez.efetch(db='nucleotide', id=IDs, rettype='fasta')
records = list(SeqIO.parse(handle, 'fasta'))



[min_index] = [i for i in range(len(records)) if len(records[i]) == min([len(record.seq) for record in records])]

handle2 = Entrez.efetch(db='nucleotide', id=IDs, rettype='fasta')
minFASTA = handle2.read().strip().split('\n\n')[min_index]

print(minFASTA)
