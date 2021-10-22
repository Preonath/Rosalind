#Problem 6: Counting Point Mutations
#Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#Return: The Hamming distance dH(s,t).

def mut(sequence1,sequence2):
 mutation=0
 for i,j in zip(sequence1,sequence2):
  if i!=j:
    mutation+= 1
 print(mutation)

def dif(sequence1,sequence2):
 print([i+1 for i in range(len(sequence1)) if sequence1[i] != sequence2[i]])

sequence1 =input()
sequence2 =input()
dif(sequence1,sequence2)
mut(sequence1,sequence2)