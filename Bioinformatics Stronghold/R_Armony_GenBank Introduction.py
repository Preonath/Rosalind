from Bio import Entrez

f=open('gbk.txt')
genus, start_date, end_date = [line.strip() for line in f.readlines()]

Entrez.email = 'preonath2838@.github.com'
handle = Entrez.esearch(db='nucleotide', term=genus+'[ORGN]', mindate=start_date, maxdate=end_date, datetype='pdat')
record = Entrez.read(handle)

print(record['Count'])
_
