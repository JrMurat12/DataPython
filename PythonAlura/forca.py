import random

def jogar():
    
    imprimirAbertura()
    palavra_secreta = carregandoPalavrasSecretas()      
    letras_acertadas = inicializaLetrasAcertadas(palavra_secreta)
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if(acertou):
        imprime_mensagem_ganhador()
    else:
        imprime_mensagem_perdedor()
 
    
    
    
    
    
    
    
def imprimirAbertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")



def carregandoPalavrasSecretas():
    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()
    
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta



def inicializaLetrasAcertadas(palavraSecreta):
    return ["_" for letra in palavraSecreta]



def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute



def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_ganhador():
    print ("Você ganhou! Parabéns!!!")
    
    
    
def imprime_mensagem_perdedor():
    print ("Você perdeu! Tente novamente!!!")
    
    

if(__name__ == "__main__"):
    jogar()
