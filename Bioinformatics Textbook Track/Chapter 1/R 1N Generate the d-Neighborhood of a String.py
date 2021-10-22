import itertools

def hamming_dist(string1, string2):
    return sum([x != y for x, y in zip(string1, string2)])

def nei(pattern,k,d):
 L = ['A', 'C', 'G', 'T']
 perms = itertools.product(L, repeat = k)
 ans = []
 for perm in perms:
    perm_string = ''.join(perm)
    h = hamming_dist(perm_string,pattern)
    if(h<=d):
      ans.append(perm_string)
 ans = set(ans)
 print(('\n').join(ans))

pattern = input()
k = len(pattern)
d = int(input())
nei(pattern,k,d)

