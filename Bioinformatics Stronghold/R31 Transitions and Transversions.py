from Bio import SeqIO
sequences = []
f = open('R31.fasta', 'r')
for record in SeqIO.parse(f, 'fasta'):
    sequences.append(str(record.seq))
s1 = sequences[0]
s2 = sequences[1]

transition = 0
transversion = 0
AG = ['A', 'G']
CT = ['C', 'T']
for i, j in zip(s1, s2):
    if i != j:
        if i in AG and j in AG:
            transition += 1
        elif i in CT and j in CT:
            transition += 1
        else:
            transversion += 1
print('%0.11f' % (transition / transversion))
