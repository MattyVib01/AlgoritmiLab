#Classe che definisce il nodo
class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.p=None
        
    def getKey(self):
        return self.key
    
    def setKey(self,value):
        self.key=value
        
    def getFather(self):
        return self.p
        
    def getChildren(self):
        children=[]
        if(self.left!=None):
            children.append(self.left)
        if(self.right!=None):
            children.append(self.right)
        return children
    
    
    
#Classe che definisce l'albero binario di ricerca
class ABR:
    def __init__(self):
        self.Nil = Node(0)
        self.Nil.left = None
        self.Nil.right = None
        self.root = self.Nil
        
    
    def setRoot(self,key):
        self.root=Node(key)
    
        
#Inserimento
    def insert(self, key):
        z=Node(key)
        z.p=None
        z.key=key
        y=None
        x=self.root 
        while(x is not None):
            y=x
            if(z.key<x.key):
                x=x.left 
            else:
                x=x.right 
        z.p=y
        if(y is None):
            self.root=z
        elif(z.key<y.key):
            y.left=z
        else:
            y.right=z
            
            
              
#Ricerca
    def search(self, key):           
        return self.findNode(self.root, key)
        
    def findNode(self, currentNode, key):
        if(currentNode is None):
            return False
        elif(key==currentNode.key):
            return True
        elif(key<currentNode.key):
            return self.findNode(currentNode.left, key)
        elif(key>currentNode.key):
            return self.findNode(currentNode.right, key)
        
#Visita
    def inorder(self):
        def inorder(v):
            if(v is None):
                return 
            if(v.left is not None):
                inorder(v.left)
            print(v.key)
            if(v.right is not None):
                inorder(v.right)
        inorder(self.root)
        


    
        
            
        
            
        
    
            
        
        
                
            
            
                
                 
                 
             
    
    
            
        
        
    
        
        
        
        
        
