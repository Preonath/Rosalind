def hamming_dist(string1, string2):
    return sum([x != y for x, y in zip(string1, string2)])


if __name__ == "__main__":
    f=open("R1G.txt","r")
    input_lines = f.read().splitlines()
    dna1 = input_lines[0]
    dna2 = input_lines[1]
    print(hamming_dist(dna1,dna2))