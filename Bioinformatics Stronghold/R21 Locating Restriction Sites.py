from Bio import SeqIO
record=SeqIO.read("R21.fasta",'fasta')
frw_seq=str(record.seq)
rev_seq=str(record.seq.complement())
for i in range(len(frw_seq)):
    for j in range(len(frw_seq)):
        s=frw_seq[i:j+1]
        m=rev_seq[i:j+1]
        if(len(s)>=4 and len(s)<=12):
            if s==m[::-1]:
                print(i+1,len(s))

