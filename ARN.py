class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.color = 1
        self.p = None

    def getKey(self):
        return self.key

    def setKey(self, value):
        self.key = value

    def getFather(self):
        return self.p

    def getColor(self):
        return self.color

    def getChildren(self):
        children = []
        if(self.left != None):
            children.append(self.left)
        if(self.right != None):
            children.append(self.right)
        return children

# Classe che definisce l'albero rosso-nero
# Il colore dei nodi è definito dall'attributo "color" (0=nero, 1=rosso)


class ARN():
    def __init__(self):
        self.Nil = Node(0)
        self.Nil.color = 0
        self.Nil.left = None
        self.Nil.right = None
        self.root = self.Nil

    def setRoot(self, key):
        self.root = Node(key)


# Inserimento


    def RBinsert(self, key):
        z = Node(key)
        z.p = None
        z.key = key
        z.left = self.Nil
        z.right = self.Nil
        z.color = 1

        y = None
        x = self.root

        while (x != self.Nil):
            y = x
            if (z.key < x.key):
                x = x.left
            else:
                x = x.right

        z.p = y
        if (y == None):
            self.root = z
        elif (z.key < y.key):
            y.left = z
        else:
            y.right = z

        if (z.p == None):
            z.color = 0
            return

        if (z.p.p == None):
            return

        self.RBinsertFixup(z)
        
        

    def RBinsertFixup(self, z):
        while (z.p.color == 1):
            if (z.p == z.p.p.right):
                y = z.p.p.left
                if (y.color == 1):
                    y.color = 0
                    z.p.color = 0
                    z.p.p.color = 1
                    z = z.p.p
                else:
                    if (z == z.p.left):
                        z = z.p
                        self.rightRotate(z)
                    z.p.color = 0
                    z.p.p.color = 1
                    self.leftRotate(z.p.p)
            else:
                y = z.p.p.right
                if (y.color == 1):
                    y.color = 0
                    z.p.color = 0
                    z.p.p.color = 1
                    z = z.p.p
                else:
                    if (z == z.p.right):
                        z = z.p
                        self.leftRotate(z)
                    z.p.color = 0
                    z.p.p.color = 1
                    self.rightRotate(z.p.p)
            if z == self.root:
                break
        self.root.color = 0


# Rotazione sinistra


    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.Nil:
            y.left.p = x

        y.p = x.p
        if (x.p == None):
            self.root = y
        elif (x == x.p.left):
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y


# Rotazione destra


    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if (y.right != self.Nil):
            y.right.p = x

        y.p = x.p
        if (x.p == None):
            self.root = y
        elif (x == x.p.right):
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

# Ricerca


    def search(self, key):
        return self.findNode(self.root, key)

    def findNode(self, currentNode, key):
        if(currentNode is None):
            return False
        elif(key == currentNode.key):
            return True
        elif(key < currentNode.key):
            return self.findNode(currentNode.left, key)
        elif(key > currentNode.key):
            return self.findNode(currentNode.right, key)


# Visita


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


