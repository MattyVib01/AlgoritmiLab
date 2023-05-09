import random
import math
import matplotlib.pyplot as plt
from ABR import ABR
from ARN import ARN
from timeit import default_timer as timer

N=2000
tree=ABR()
brtree=ARN()
tree2=ABR()
brtree2=ARN()
A=list(range(N))
B=list(range(N))
random.shuffle(A)
last=A[N-1]
for i in A:
    tree.insert(i)
for l in A:
    brtree.RBinsert(l)
for j in B:
    tree2.insert(j)
for k in B:
    brtree2.RBinsert(k)

    
    
#Cerca l'ultimo elemento se l'albero è costruito random
start=timer()
tree.search(last)
end=timer()
print(str(end-start)+" secondi")
start=timer()
brtree.search(last)
end=timer()
print(str(end-start)+" secondi")


#Cerca l'ultimo elemento se l'albero è ordinato
start=timer()
tree2.search(N-1)
end=timer()
print(str(end-start)+" secondi")
start=timer()
brtree2.search(N-1)
end=timer()
print(str(end-start)+" secondi")


