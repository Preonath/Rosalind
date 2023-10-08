#Problem 10: Consensus and Profile
#Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
#Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

file = open("/home/preonath/Desktop/Rosalind_Dataset/rosalind_cons.txt", "r")
matrix = []
read_all_line= file.read()
read_replace_Rosalind = read_all_line.replace("Rosalind_", "")
read_replace_newline = read_replace_Rosalind.replace("\n", "")
read_after_cutting_digit = ''.join([i for i in read_replace_newline if not i.isdigit()])
matrix = read_after_cutting_digit.split(">")
matrix.remove("")


def consensus(matrix):
    a = []
    c = []
    g = []
    t = []
    for i in range(0, len(matrix[0])):
        count_A = 0
        count_C = 0
        count_G = 0
        count_T = 0
        for j in matrix:
            if (j[i] == "A"):
                count_A+= 1
            elif (j[i] == "C"):
                count_C+= 1
            elif (j[i] == "G"):
                count_G+= 1
            elif (j[i] == "T"):
                count_T+= 1
        a.append(count_A)
        c.append(count_C)
        g.append(count_G)
        t.append(count_T)
    All_String = []
    for i in range(0, len(matrix[0])):
        if (a[i] >= c[i] and a[i] >= g[i] and a[i] >= t[i]):
            All_String.append("A")
        elif (c[i] >= a[i] and c[i] >= g[i] and c[i] >= t[i]):
            All_String.append("C")
        elif (g[i] >= a[i] and g[i] >= c[i] and g[i] >= t[i]):
            All_String.append("G")
        else:
            All_String.append("T")
    New_Profile = ''.join(All_String)
    strA = 'A: ' + ' '.join(map(str,a))
    strC = 'C: ' + ' '.join(map(str,c))
    strG = 'G: ' + ' '.join(map(str,g))
    strT = 'T: ' + ' '.join(map(str,t))

    file = open("result_rosalind_cons.txt","w")
    file.write(New_Profile)
    file.write("\n")
    file.write(strA)
    file.write("\n")
    file.write(strC)
    file.write("\n")
    file.write(strG)
    file.write("\n")
    file.write(strT)
    file.write("\n")
    file.close()
    return New_Profile, strA, strC, strG, strT
print(consensus(matrix))
