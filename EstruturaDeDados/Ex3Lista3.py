import numpy as np

class ProdEscalar:
    def __init__(self, prodA, prodB):
        self.prodA = prodA
        self.prodB = prodB
        print(np.dot(prodA, prodB))
        
vetores = ProdEscalar([[2,1],[0,3]], [[1,1],[3,2]]) #Declare os vetores nos parâmetros da classe

        
