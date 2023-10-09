def ComputeDistancesBetweenLeaves(n, T):
    # D
    # Recursively compute the distances between two nodes
    def D(i, j, path=[]):
        if i == j:  return 0
        d = float('inf')
        for node, weight in T[i]:
            if node == j:
                return weight
            if node in path:
                continue
            test = weight + D(node, j, path + [node])
            if test < d:
                d = test
        return d
    for i in range(n):
        for j in range(n):
            return [D(i,j)]
    # return [[D(i, j) for j in range(n)] for i in range(n)]

if __name__ == '__main__':
    from helpers import create_weighted_adjacency_list
    n, T = create_weighted_adjacency_list()
    for ds in ComputeDistancesBetweenLeaves(n, T):
        print(' '.join(str(d) for d in ds))