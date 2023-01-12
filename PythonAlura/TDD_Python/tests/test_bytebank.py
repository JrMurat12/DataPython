from codigo.bytebank import Funcionario
import pytest

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000' # Given-Contexto
        esperado = 22
        
        Funcionario_Teste = Funcionario('Teste', entrada, 1111)
        
        resultado = Funcionario_Teste.idade() # When-Ação
        
        assert resultado == esperado # Then-Desfecho