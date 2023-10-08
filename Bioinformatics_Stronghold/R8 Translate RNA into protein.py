from Bio.Seq import Seq
s=input()
messenger_rna =Seq(s)
protein=messenger_rna.translate()
print(protein)