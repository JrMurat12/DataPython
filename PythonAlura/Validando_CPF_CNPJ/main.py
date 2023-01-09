from Cpf_Cnpj import Documento

############ CPF #############
# from Cpf import Cpf
# cpf_um = Cpf("15316264754")
# print(cpf_um)
exemplo_cpf = "49713812018"
documento1 = Documento.cria_documento(exemplo_cpf)

############ CNPJ ############
exemplo_cnpj = "54573854000196"
documento = Documento.cria_documento(exemplo_cnpj)

print(documento)
print(documento1)


############ Telefone ##########


