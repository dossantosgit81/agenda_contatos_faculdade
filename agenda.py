from ntpath import join

#Salvo todos os contatos aqui
contatos = {}

#Mensagem de erro para informar o usário de que aquele dado não existe
msg_contato_inexistente = "Verfique se o nome que você digitou realmente existe."

#Iniciando variaveis necessárias para inserir no dicionario ao salvar ou atualizar ou remover e demais operações solicitadas
nome_contato = ""
contatos[nome_contato] = {}
contatos[nome_contato]['telefone'] = ""
contatos[nome_contato]['email'] = ""
contatos[nome_contato]["twitter"] = ""
contatos[nome_contato]['instagram'] = ""

#Inserção de dados no dicionario contatos
def inserir():
    nome_contato = str(input("Insira o nome do contato: ")).capitalize() 
    contatos[nome_contato] = {}
    contatos[nome_contato]['telefone'] = str(input("Insira o telefone: "))
    contatos[nome_contato]['email'] = str(input("Insira o email: "))
    contatos[nome_contato]['twitter'] = str(input("Insira o login do twitter: "))
    contatos[nome_contato]['instagram'] = str(input("Insira o login instagram: "))
    print("Contato inserido com sucesso!")

#Remoção de um dado do contato
def remover():
    try:
        del contatos[str(input("Insira o nome do contato que deseja remover: " )).capitalize()]
        print("Contato removido com sucesso!!!")
    except:
        print(msg_contato_inexistente)

#Consulta de um contato
def consultar():
    try:
        print(contatos[str(input("Insira o nome do contato que deseja encontrar: " )).capitalize()])
    except:
        print(msg_contato_inexistente)

#Atualização de um contato
def atualizar(): 
        nome_contato_antigo = str(input("Insira o nome do contato que deseja atualizar. " )).capitalize()
        nome_contato_novo = str(input("Insira o novo nome." )).capitalize()

        if nome_contato_novo == "" and nome_contato_antigo != "":
            nome_contato_novo = nome_contato_antigo
        
        try:
            contatos[nome_contato_novo] = contatos.pop(nome_contato_antigo)
            contatos[nome_contato_novo]['telefone'] = str(input("Insira o novo telefone: "))
            contatos[nome_contato_novo]['email'] = str(input("Insira o novo email: "))
            contatos[nome_contato_novo]['twitter'] = str(input("Insira o login do twitter: "))
            contatos[nome_contato_novo]['instagram'] = str(input("Insira o login instagram: "))
        except:
            print("Nome inexistente")

#Inserção de vários contatos
def inserir_contatos():
    try:
        qtd_usuarios = int(str(input("Quantos usuários deseja inserir? " )))
        contador = 0;
        while qtd_usuarios > contador:
            inserir()
            contador+=1

    except:
        print("Não é possivel converter o(s) carctere(s) que você digitou para número. ")

#Funcao para verficar se uma string é vazia ou possui espaços
def em_branco_ou_vazio(s):
    return s.isspace() or s != ''  

#Função auxiliar para exibir os dados de contatos em formato string
def exibir(listas):
    index = 0
    print("Nro | "+ "Nome | "+ "Telefone | " + "E-mail | " + "Twitter | " + "Instagram ")
    for lista in listas: 
        index+=1
        indexText = str(index)
        exibir_lista = ' | '.join(lista)
        print(indexText +' | '+ exibir_lista)

#Lista contatos
def listar_contatos():
    lista_estrtura_exibicao = []
    lista_exibicao = []
    for key, value in contatos.items():
        if  em_branco_ou_vazio(key):
            lista_estrtura_exibicao.append(str(key)) 
        for newKey, newValue in value.items():
                if em_branco_ou_vazio(newValue): 
                    lista_estrtura_exibicao.append(newValue)
                    if(newKey == 'instagram'):
                        lista_exibicao.append(lista_estrtura_exibicao)
                        lista_estrtura_exibicao = []
    exibir(lista_exibicao)

#Inserção de dados com virgula
def inserir_dados_com_virgula():
    print("A ordem é: Nome, telefone, email, Twitter, Instagram. Se você não digitar os dados corretos nessa ordem, uma conta de instagram será salva em um conta de twitter por exemplo.")
    entrada = str(input("Insira os dados que serão salvos. " )).capitalize()

    entrada_array = entrada.split(",")
    if len(entrada_array) == 5:
        nome_contato = entrada_array[0]
        contatos[nome_contato] = {}
        contatos[nome_contato]['telefone'] = entrada_array[1]
        contatos[nome_contato]['email'] = entrada_array[2]
        contatos[nome_contato]['twitter'] = entrada_array[3]
        contatos[nome_contato]['instagram'] = entrada_array[4]
        print("Contato inserido com sucesso!")

   
#Escolha do usário                        
def escolha():
	print(" ")

	print(" ")
	print("1 - Adicionar contato")
	print("2 - Remover um contato")
	print("3 - Alterar contato")
	print("4 - Buscar por um contato")
	print("5 - Listar contatos")
	print("6 - Adicionar contatos")
	print("7 - Salvar contatos seprados por vírgula")
	print("8 - Sair")

    
	acao = int(str(input("Ação: ")))

	return acao

acao = 1
#Execução de acordo com escolha
while acao in (1, 2, 3, 4, 5, 6, 7):
	acao = escolha()
	if acao == 1:
		inserir()
	elif acao == 2:
		remover()
	elif acao == 3:
		atualizar()
	elif acao == 4:
		consultar()
	elif acao == 5:
		listar_contatos()
	elif acao == 6:
		inserir_contatos()
	elif acao == 7:
		inserir_dados_com_virgula()
	else:
		exit("Até logo!!!")


