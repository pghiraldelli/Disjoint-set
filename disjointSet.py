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

def unionWithPathCompression():
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

if __name__ == "__main__":
    nos = criaNos([1,2,3])
        
    noNovo = criaNo(10,nos[1])
    noNovo2 = criaNo(11, noNovo)
    