from bytebank import Funcionario

# jefferson = Funcionario('Jefferson Murat', '11/02/2001', 1000)

# print(jefferson.idade())

def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
    print(f'Teste = {funcionario_teste.idade()}')
    
teste_idade()