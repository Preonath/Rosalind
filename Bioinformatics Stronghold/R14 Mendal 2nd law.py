# Slide of probability:   https://www.slideshare.net/BrijeshKumar230/laws-of-probability-75500744
# Law of this problem probability: https://medium.com/dev-genius/active-learning-bioinformatics-2-0-87c94f36e4ad

import math
k =int(input())      # where k is the number of generations

N =int(input()) #    N is the least number of the population with genotype Aa Bb we are looking for

P = 2**k   #final population P,For a population of P = k²

probability = 0
for i in range(N, P + 1):
    prob = (math.factorial(P) /
            (math.factorial(i) * math.factorial(P - i))) * (0.25**i) * (0.75**(
                P - i))
    probability += prob
print(probability)