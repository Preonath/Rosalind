from Bio import SeqIO

prefixes = []
suffixes = []
handle = open('samplefile.fasta', 'r')

for record in SeqIO.parse(handle, 'fasta'):
    count1 = 0
    count2 = 0
    prefix = [record.id]
    suffix = [record.id]

    pre = ''
    suf = ''
    for nt in record.seq:
        if count1 < 3:
            pre += nt
            count1 += 1
    prefix.append(pre)

    for tn in reversed(record.seq):
        if count2 < 3:
            suf += tn
            count2 += 1
    suffix.append(''.join(reversed(suf)))
    prefixes.append(prefix)
    suffixes.append(suffix)
    # print(prefix)
    # print(suffix)
handle.close()

for i,k in enumerate(suffixes):
    currentsf = suffixes[i][1]

    currentid = suffixes[i][0]
    # print(i,k)
    # print("suf")
    # print(currentid)
    for j, l in enumerate(prefixes):
        # print(j,l)
        if currentsf == prefixes[j][1] and currentid != prefixes[j][0]:
            print(currentid, prefixes[j][0])