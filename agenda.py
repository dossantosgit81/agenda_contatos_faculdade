from ntpath import join


contatos = {}

msg_contato_inexistente = "Verfique se o nome que você digitou realmente existe."

inserir_ja_foi_executado = 0;

nome_contato = ""
contatos[nome_contato] = {}
contatos[nome_contato]['telefone'] = ""
contatos[nome_contato]['email'] = ""
contatos[nome_contato]["twitter"] = ""
contatos[nome_contato]['instagram'] = ""

def inserir():
    nome_contato = str(input("Insira o nome do contato: ")).capitalize() 
    contatos[nome_contato] = {}
    contatos[nome_contato]['telefone'] = str(input("Insira o telefone: "))
    contatos[nome_contato]['email'] = str(input("Insira o email: "))
    contatos[nome_contato]['twitter'] = str(input("Insira o login do twitter: "))
    contatos[nome_contato]['instagram'] = str(input("Insira o login instagram: "))
    print("Contato inserido com sucesso!")

def remover():
    try:
        del contatos[str(input("Insira o nome do contato que deseja remover: " )).capitalize()]
        print("Contato removido com sucesso!!!")
    except:
        print(msg_contato_inexistente)

def consultar():
    try:
        print(contatos[str(input("Insira o nome do contato que deseja encontrar: " )).capitalize()])
    except:
        print(msg_contato_inexistente)

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

def inserir_contatos():
    try:
        qtd_usuarios = int(str(input("Quantos usuários deseja inserir? " )))
        contador = 0;
        while qtd_usuarios > contador:
            inserir()
            contador+=1

    except:
        print("Não é possivel converter o(s) carctere(s) que você digitou para número. ")


def em_branco_ou_vazio(s):
    return s.isspace() or s != ''  


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
                        

def exibir(listas):
    index = 0
    print("Nro | "+ "Nome | "+ "Telefone | " + "E-mail | " "Twitter | " "Instagram | ")
    for lista in listas: 
        index+=1
        indexText = str(index)
        exibir_lista = ' | '.join(lista)
        print(indexText +' | '+ exibir_lista)
          

                            



    #usesublist
inserir_contatos()
listar_contatos()

