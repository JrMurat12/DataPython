import requests
from Telefones_Br import Telefones_Br
from Cpf_Cnpj import Documento
from Datas_Br import Datas_Br
from Endereco_Br import Endereco_Br


############ CPF #############
exemplo_cpf = "49713812018"
documento1 = Documento.cria_documento(exemplo_cpf)
print(documento1)


############ CNPJ ############
exemplo_cnpj = "54573854000196"
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)


############ Telefone ##########
telefone =  "552126481234"
telefone_objeto = Telefones_Br(telefone)
print(telefone_objeto)


############ Data ###############
cadastro = Datas_Br()
print(cadastro)
print(cadastro.tempo_cadastro())


############ CEP #################
cep = "01001000"
objeto_cep = Endereco_Br(cep)
logradouro, bairro, cidade, cep, uf = objeto_cep.acessa_via_cep()
print(logradouro, bairro, cidade, cep, uf)


