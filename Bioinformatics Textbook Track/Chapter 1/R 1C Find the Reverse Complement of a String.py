def string(s):
    rna=""
    rev=s[::-1]
    for i in rev:
        if(i=="A"):
            rna+="T"
        elif (i == "T"):
            rna += "A"
        elif (i == "C"):
            rna += "G"
        if (i == "G"):
            rna += "C"
    return(rna)
s=input()
print(string(s))
