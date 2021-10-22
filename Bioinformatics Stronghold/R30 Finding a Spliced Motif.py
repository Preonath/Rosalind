from Bio import SeqIO
sequences = []
f = open('R30.fasta', 'r')
for record in SeqIO.parse(f, 'fasta'):
    sequences.append(str(record.seq))
s1 =sequences[0]
s2=sequences[1]

output_list= ""
dna_index = 0
motif_index = 0

# Iterate through the DNA
for i in s1:

    # If current base is equal to the `current` base in the motif
    # By current I mean the latest base we are looking for
    if i == s2[motif_index]:

        motif_index += 1
        # `dna_index + 1` is because question assumes first index is 1
        output_list += str(dna_index + 1) + " "

        # If we are out of motif base then done
        if motif_index == len(s2):][]
            break

    dna_index += 1
print(output_list)