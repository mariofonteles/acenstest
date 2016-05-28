alfabeto = 'abcdefghijklmnopqrstuvwxyz'   
#funcao para encriptar o texto, recebe o valor usado na cifra(n) e o texto original
def encriptar(n, texto):
    resultado = ''      #criando uma string vazia usada para comparar os valores
    for c in texto.lower():  #caso o usuario digite letras em maiusculo, ficam minusculas
        try:
            i = (alfabeto.index(c) + n) % 26 #formula matematica da cifra: E(x) = (x + n) % 26 
            resultado += alfabeto[i]         
        except ValueError:                   #try e except sao usados para possibilitar o uso de espacos.            
            resultado += c                  #quando e detectado um espaco, o valor eh apenas transcrevido como foi escrito originalmente
    return resultado.lower()

def desemcriptar(n, encriptado):  #funcao para desemcriptar pega o valor obtido da funcao anterior
    resultado = ''
    for c in encriptado:
        try:
            i = (alfabeto.index(c) - n) % 26 #a formula para desemcriptacao eh apenas o contrario da formula original
            resultado += alfabeto[i]
        except ValueError:
            resultado += c

    return resultado
    
texto = raw_input ("digite o texto a ser encriptado: ")
n = input("digite um valor de 1 a 26: ")

encriptado = encriptar(n, texto)

print ("a forma encriptada eh: %s" %encriptado)

desemcriptado = desemcriptar(n, encriptado)

print ("e o texto original desemcriptado: %s" %desemcriptado)
