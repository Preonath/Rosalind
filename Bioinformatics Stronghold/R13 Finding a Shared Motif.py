from Bio import SeqIO
l = []
f = open('R13.txt', 'r')
for record in SeqIO.parse(f,'fasta'):
    s = []
    seq = ''
    for nt in record.seq:
        seq += nt
    l.append(seq)
srt_seq = sorted(l, key=len)
first_seq = srt_seq[0]
others_seq = srt_seq[1:]
motif = ''
for i in range(len(first_seq)):
    for j in range(i, len(first_seq)):
        m = first_seq[i:j + 1]
        flag = False
        for k in others_seq:
            if m in k:
                flag = True
            else:
                flag = False
                break
        if flag and len(m) > len(motif):
            motif = m
print(motif)
