from codigo.bytebank import Funcionario
import pytest

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000' # Given-Contexto
        esperado = 22
        
        Funcionario_Teste = Funcionario('Teste', entrada, 1111)
        
        resultado = Funcionario_Teste.idade() # When-Ação
        
        assert resultado == esperado # Then-Desfecho
    
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = 'Lucas Carvalho ' #Given
        esperado = 'Carvalho'
        
        Funcionario_Teste = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome()
        
        assert resultado == esperado