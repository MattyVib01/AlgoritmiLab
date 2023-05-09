import random
import matplotlib.pyplot as plt
from ABR import ABR
from ARN import ARN
from timeit import default_timer as timer
    
def main():
    
    N=20000
    j=1
    print("\n")
    tree=ABR()
    brtree=ARN()
    tree2=ABR()
    brtree2=ARN()
    x=list()
    y=list()
    
    
#Inserisco N valori pseudocasuali
    print("Inserimento di N valori pseudocasuali")
    A=list(range(N))
    random.shuffle(A)
    print("Albero binario di ricerca")
    start=timer()
    for i in A:
        tree.insert(A[i])
        x.append(j)
        y.append(timer())
        j=j+1
    end=timer()
    print(str(end-start)+" secondi")
    plt.plot(x,y)
    plt.xlabel("valori inseriti")
    plt.ylabel("tempo impiegato")
    plt.show()
    
    j=0
    x.clear()
    y.clear()
    
    print("Albero rosso-nero")
    start=timer()
    for i in A:
        brtree.RBinsert(A[i])
        x.append(j)
        y.append(timer())
        j=j+1
    end=timer()
    print(str(end-start)+" secondi")
    plt.plot(x,y,c="red")
    plt.xlabel("valori inseriti")
    plt.ylabel("tempo impiegato")
    plt.show()
    print("\n")

    x.clear()
    y.clear()
    
#Inserisco N valori in ordine crescente
    print("Inserimento di N valori in ordine crescente (caso peggiore)")
    start=timer()
    print("Albero binario di ricerca")
    for i in range(N):
        tree2.insert(i)
        x.append(i)
        y.append(timer())    
    end=timer()
    print(str(end-start)+" secondi")
    plt.plot(x,y)
    plt.xlabel("valori inseriti")
    plt.ylabel("tempo impiegato")
    plt.show()
    
    x.clear()
    y.clear()
    
    
    start=timer()
    print("Albero rosso nero")
    for i in range(N):
        brtree2.RBinsert(i)
        x.append(i)
        y.append(timer())
    end=timer()
    print(str(end-start)+" secondi")
    plt.plot(x,y,c="red")
    plt.xlabel("valori inseriti")
    plt.ylabel("tempo impiegato")
    plt.show()
    
        
if __name__=="__main__":
    main()