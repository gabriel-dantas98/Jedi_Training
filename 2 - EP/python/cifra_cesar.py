import sys

alfabetoDefault = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y', 'z']

alfabetoCesar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y', 'z']

def reCrypt(comando, mensagem, rotate, cryptLevel):
    
    if comando == "encrypt":
        for i in range(0,cryptLevel):
            rotateAlpha(rotate)
            mensagem = encrypt(mensagem)
            
        print(mensagem)

    elif comando == "decrypt":
        for j in range(0,cryptLevel):  
            rotateAlpha(rotate)
            mensagem = decrypt(mensagem)
    
        print(mensagem)

def rotateAlpha(rotate):

    countPositivo = 26 - rotate
    for p in range(0,rotate):
        alfabetoCesar[countPositivo] = alfabetoDefault[p]
        countPositivo = countPositivo + 1

    countNegativo = - 26 + rotate
    countReplace = 26 - rotate
    for t in range(0,countReplace):
        alfabetoCesar[t] = alfabetoDefault[countNegativo]
        countNegativo = countNegativo + 1
    
def decrypt(mensagem):
    
    msg = ''
    mensagemFormated = (mensagem.lower())

    for j in range(len(mensagemFormated)):
        if((mensagemFormated[j] in alfabetoDefault) == True):
            k = alfabetoCesar.index(mensagemFormated[j])
            msg += alfabetoDefault[k]

        elif((mensagemFormated[j] in alfabetoDefault) == False):
            msg += mensagemFormated[j]

    return msg

def encrypt(mensagem):
    
    msg = ''
    mensagemFormated = (mensagem.lower())

    for i in range(len(mensagemFormated)):
        if((mensagemFormated[i] in alfabetoDefault) == False):
            msg += mensagemFormated[i]

        elif((mensagemFormated[i] in alfabetoDefault) == True):
            j = alfabetoDefault.index(mensagemFormated[i])
            msg += alfabetoCesar[j]

    return msg

def main():

    comando = sys.argv[1]
    mensagem = sys.argv[2]
    rotate = int(sys.argv[3])
    cryptLevel = int(sys.argv[4])     

    rotateAlpha(rotate)

    if comando == "encrypt" or  comando == "decrypt":
        reCrypt(comando, mensagem, rotate, cryptLevel)
    else:
        print ('Comando invalido!!!')
    
if __name__ == '__main__':
    main()




