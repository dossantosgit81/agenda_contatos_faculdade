# encoding=utf8
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
# ***VÁRIAVEIS**
      # x = 1
      # y = 2

# ***ESTRUTURAS CONDICIONAIS***
      # if x == y:
      #   print("Números iguais")

      # elif x < y:
      #   print("x é maior que y.")

      # else:
      #    print("y é maior que x.")

# ***ESTRUTURA DE REPETIÇÃO WHILE***
      # x=1;
      # while x < 10:
      #   print(x)
      # x = x+1

# ***ESTRUTURA DE REPETIÇÃO FOR***
      # lista1 = [1, 2, 3, 4, 5]
      # lista1 = [1, 2, 3, 4, 5.9]
      # lista1 = [1, 2, 3, 4, 0.55, "Hello"]

      # for i in lista1:
      #   print(i)

# ***FUNÇÃO RANGE***
      # #Imprima os números de 10 a 20(Não incluso) de 2 em 2 em dez
      # for i in range(10, 20, 2):
      #   print(i)

      # #Imprima os números de 0 a 10(Não incluso)
      # for i in range(10):
      #   print(i)

      # #Imprima os números de 10 a 20(Não incluso)
      # for i in range(10, 20):
      #   print(i)

# ***STRINGS***
      # a = "Diego"
      # b = "Maradona"

      # concatenar = a + " " + b + "\n"
      # print(concatenar)
      # print(len(concatenar))
      # print(concatenar[2])
      # print(concatenar[0:4])

      # print(concatenar.lower())
      # print(concatenar.upper())

      # # Remove caracteres especiais
      # print(concatenar.strip())

      # minha_lista=concatenar.split(" ");
      # print(minha_lista)

      # #Trás o index da palavra
      # busca = concatenar.find("Maradona")
      # print(busca)

      # # Trás toda palavra a partir da da letra/palavra buscada
      # busca = concatenar.find("r")
      # print(concatenar[busca:])

      # print(concatenar.replace(" ", " Rainha "))

# ***FUNÇÔES***
      # def soma(x, y):
      #       return x+y

      # def multiplicacao(x, y):
      #       return x*y

      # s = soma(2, 3)
      # m = multiplicacao(3, 4)

      # print(soma(s, m))

# ***Arquivos***
      # #read() <- Ler arquivo
      # #readline() <- Lê uma linha
      # #readlines() <- Lê o arquivo e o armazena em um alista

      # arquivo = open("arquivo.txt")
      # #linhas = arquivo.readlines()

      # #print(linhas)

      # texto_completo = arquivo.read()
      # print(texto_completo)

      # # for linha in linhas:
      # #       print(linha)

      # w = open("arquivo2.txt", "a")

      # w.write("Esse é o meu arquivo")
      # w.close()

      #listas

      # minha_lista = ["abacaxi", "melancia", "abacate"]

      # print(minha_lista)

      # for item in minha_lista:
      #       print(item)

      # tamanho = len(minha_lista)
      # print(tamanho)

      # minha_lista.append("Limão");

      # print(minha_lista)

      # if "abacaxi" in minha_lista:
      #       print("7 está na lista")

      # #del minha_lista[2:]
      # #del minha_lista[0:]
      # del minha_lista[:]

      # minha_lista = []


      # print(minha_lista)

      # minha_lista = [5, 9, 5, 6, 1, 2, 4, 7, 8]
      # minha_lista.sort(reverse=True)
      # lista = sorted(minha_lista)
      # print(minha_lista)

#***DICIONARIOS***
meu_dicionario = {"A":"AMEIXA", "B":"BOLA"}
print(meu_dicionario["A"])

# for chave in meu_dicionario:
#       print(chave+"-"+meu_dicionario[chave])

for i in meu_dicionario.items():
      print(i)

for i in meu_dicionario.values():
      print(i)

for i in meu_dicionario.keys():
      print(i)


try:
      print(2/0)
except:
      print("Não é permitida")

x = [1,2,3,4]
y= [i**2 for i in x]
z= [i**2 for i in x if i%2==1]
print(y)
print (z)

for i, nome in enumerate(x):
      print(i, nome)

def dobro(x):
      return x*2

valor = [1, 2, 3, 4, 5]
lista2 = ["Abacate", "Bola", "Cachorro", "Dinheiro", "Elefante"]
for numero, nome in zip(valor, lista2):
      print(numero, nome)

# valor_dobrado = map(dobro, valor)

# valor_dobrado = list(valor_dobrado)
# print(valor_dobrado)