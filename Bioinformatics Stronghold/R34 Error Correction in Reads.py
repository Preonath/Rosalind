from Bio import SeqIO
from Bio.Seq import Seq

reads=[]
f=open("R34.fasta","r")
for i in SeqIO.parse(f,'fasta'):
    reads.append(str(i.seq))
right=[]
wrong = []
for i, j in enumerate(reads):
    read = Seq(j)
    rev_read = read.reverse_complement()
    for k in range(i + 1, len(reads)):
        if read == reads[k] or rev_read == reads[k]:
            if read not in right and rev_read not in right:
                right.append(str(read))
                right.append(str(rev_read))

for l in reads:
    if l not in right:
        wrong.append(l)

for incorrect in wrong:
    for correct in right:
        hamming = 0
        for nt1, nt2 in zip(incorrect, correct):
            if nt1 != nt2:
                hamming += 1
                if hamming > 2:
                    break
        if hamming == 1:
            print(incorrect, '->', correct, sep='')


