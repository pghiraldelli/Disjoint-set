import random
import time
import sys 

class No(object):
    def __init__(self, valor):
        self.pai = self
        self.valor = valor
        self.rank = 0
        
def criaNos(valores):
    nos = []
    for valor in valores:
        nos.append(No(valor))
    return nos
    
def criaNo(valor, pai):
    no = No(valor)
    no.pai = pai
    raizPai = find(pai)
    raizPai.rank = raizPai.rank + 1
    return no
    
def find(no):
    if no.pai == no:
        return no
    else:
        return find(no.pai)
        
def union(no1, no2):
    raiz1 = find(no1)
    raiz2 = find(no2)
    raiz1.pai = raiz2

def unionByRank(no1, no2):
    raiz1 = find(no1)
    raiz2 = find(no2)
    if raiz1 == raiz2:
        return
    
    if raiz1.rank == raiz2.rank:
        raiz2.pai = raiz1
        raiz1.rank = raiz1.rank + 1
    elif raiz1.rank > raiz2.rank:
        raiz2.pai = raiz1
    elif raiz1.rank < raiz2.rank:
        raiz1.pai = raiz2
    
def findWithPathCompression(no):
     if no.pai != no:
        no.pai = findWithPathCompression(no.pai)
     return no.pai

def unionWithPathCompression(no1, no2):
    raiz1 = findWithPathCompression(no1)
    raiz2 = findWithPathCompression(no2)
    raiz1.pai = raiz2

def unionByRankPathCompression(no1, no2):
    raiz1 = findWithPathCompression(no1)
    raiz2 = findWithPathCompression(no2)
    if raiz1 == raiz2:
        return
    
    if raiz1.rank == raiz2.rank:
        raiz2.pai = raiz1
        raiz1.rank = raiz1.rank + 1
    elif raiz1.rank > raiz2.rank:
        raiz2.pai = raiz1
    elif raiz1.rank < raiz2.rank:
        raiz1.pai = raiz2

def test_unions(nos, reps, union_f):                 
     accum = 0                           
     for i in xrange(reps):              
         a = random.randint(0, len(nos) - 1)
         b = random.randint(0, len(nos) - 1)
         while a == b:
             b = random.randint(0, len(nos) - 1)
         no_a = nos[a]
         no_b = nos[b]
         start = time.time()
         union_f(no_a, no_b)
         end = time.time()
         accum += end - start
     return accum

if __name__ == "__main__":
    sys.setrecursionlimit(100000) 
    print "Total de nos gerados para cada caso: 1000000"
    
    print "----- Criando arestas aleatorias entre os nos gerados com 550000 repeticoes -----"
    nos = criaNos(range(1000000))
    print "Tempo do union: %02f" % test_unions(nos, 550000, union) 
    nos = criaNos(range(1000000))
    print "Tempo do unionByRank: %02f" % test_unions(nos, 550000, unionByRank) 
    nos = criaNos(range(1000000))
    print "Tempo do unionWithPathCompression: %02f" % test_unions(nos, 550000, unionWithPathCompression) 
    nos = criaNos(range(1000000))
    print "Tempo do unionByRankWithPathCompression: %02f" % test_unions(nos, 550000, unionByRankPathCompression)

    print "----- Criando arestas aleatorias entre os nos gerados com 1000000 repeticoes -----"
    print "Tempo do union: infinito"
    nos = criaNos(range(1000000))
    print "Tempo do unionByRank: %02f" % test_unions(nos, 1000000, unionByRank) 
    nos = criaNos(range(1000000))
    print "Tempo do unionWithPathCompression: %02f" % test_unions(nos, 1000000, unionWithPathCompression) 
    nos = criaNos(range(1000000))
    print "Tempo do unionByRankWithPathCompression: %02f" % test_unions(nos, 1000000, unionByRankPathCompression)
    
