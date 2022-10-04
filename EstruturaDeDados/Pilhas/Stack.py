from Node import Node
# Nó simples a ser utilizado na pilha

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __repr__(self):
        return "[" + str(self.top) + "]"

    def push(self, item):
        # Insere um item na pilha
        node = Node(item) # Criou o nó
        node.next = self.top # Apontou para o próximo
        self.top = node # Adiciona o nome criado no top da pilha
        self.size = self.size + 1

    def pop(self):
        assert self.top

        self.top = self.top.next
        #if self.size > 0:
            #node = self.top
            #self.top = self.top.next
        self.size = self.size - 1
            #return node.data
        #raise IndexError("The Stack is Empty!")

    def peek(self):
        if self.size > 0:
            self.top.data
        raise IndexError("The Stack is Empty!")

    def __len__(self):
        return self.size

# Cria uma pilha vazia.
pilha = Stack()
print("Pilha vazia: ", pilha)

# Insere elementos na pilha.
for i in range(5):
    pilha.push(i)
    print("Insere o valor {0} no topo da pilha: {1}".format(i, pilha))

# Remove elementos na pilha.
while pilha.top != None:
    print("Removendo elemento que está no topo da pilha: ", pilha)
    pilha.pop()


