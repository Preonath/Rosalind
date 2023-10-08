# https://stackoverflow.com/questions/32991650/get-the-full-substring-matching-the-regex-pattern
# Plz check


import re
from Bio import SeqIO
from Bio.Seq import Seq


record = SeqIO.read('R18.fasta', 'fasta')
pattern = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))')
frw_seq = record.seq
string1=str(frw_seq)
rev_seq = frw_seq.reverse_complement()
string2=str(rev_seq)

seq_list = []

for i in re.findall(pattern,string1):
    prot_seq = Seq(i).translate()
    if prot_seq not in seq_list:
        seq_list.append(prot_seq)
for j in re.findall(pattern, string2):
    rev_prot_seq = Seq(j).translate()
    if rev_prot_seq not in seq_list:
        seq_list.append(rev_prot_seq)

for i, s in enumerate(seq_list):
    print(s)
