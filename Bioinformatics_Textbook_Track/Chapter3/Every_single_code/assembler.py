__author__ = 'Rajan Saha Raju'
__date__ = 'June 25 20:02:51 +06 2020'

from sys import stdin
from collections import defaultdict

def build_de_bruijn_graph(seqs, adj):
    for seq in seqs:
        adj[seq[0:-1:]].append(seq[1::])
    return

def get_start_finish_node(adj):
    indeg, outdeg = defaultdict(int), defaultdict(int)
    nodes = set()
    for key, vals in adj.items():
        nodes.add(key)
        nodes.update(vals)  # Add list to set
        outdeg[key] += 1
        for val in vals:
            indeg[val] += 1
    start, finish = None, None
    for node in nodes:
        if indeg[node] + 1 == outdeg[node]:
            start = node
        if indeg[node] == outdeg[node] + 1:
            finish = node
    return (start, finish)

def get_euler_cycle(adj, start):
    path, cycle = [start] , []
    while path:
        u = path[-1]
        if adj[u]:
            v = adj[u].pop()
            path.append(v)
        else:
            cycle.append(path.pop())
    return cycle[::-1]

def get_genome_sequence(paths, start, finish):
    reads = []
    for k in range(len(paths) - 1):
        if paths[k] == finish and paths[k+1] == start:
            reads = paths[0:k+1:] + paths[k+1::]
            break
    reads.pop()
    genome_sequence = ''
    for k in range(len(reads)):
        if k != 0:
            genome_sequence += reads[k][-1]
        else:
            genome_sequence += reads[k]
    return genome_sequence
    
        
def main():
    k = int(input())
    seqs = [line for line in stdin.read().splitlines()]
    adj = defaultdict(list)
    build_de_bruijn_graph(seqs, adj)
    start, finish = get_start_finish_node(adj)
    adj[finish].append(start)
    paths = get_euler_cycle(adj, start)
    genome_seq = get_genome_sequence(paths, start, finish)
    print(genome_seq)

if __name__ == "__main__":
    main()