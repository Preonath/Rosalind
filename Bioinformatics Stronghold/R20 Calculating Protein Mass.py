from Bio.Seq import Seq
from Bio.SeqUtils import molecular_weight

f=open('R20.txt','r')
for i in f:
    print(molecular_weight(Seq(i.strip('\n')),monoisotopic=True) - 18.01056)