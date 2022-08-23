contatos = {}

msg_contato_inexistente = "Verfique se o nome que você digitou realmente existe."

def inserir():
    nome_contato = str(input("Insira o nome do contato: ")).capitalize() 
    contatos[nome_contato] = {}
    contatos[nome_contato]['telefone'] = str(input("Insira o telefone: "))
    contatos[nome_contato]['email'] = str(input("Insira o email: "))
    contatos[nome_contato]['midias_sociais'] = [{'twitter': str(input("Insira o login do twitter: "))}]
    contatos[nome_contato]['midias_sociais'].append({'instagram': str(input("Insira o login instagram: "))})
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
        
        contatos[nome_contato_novo] = contatos.pop(nome_contato_antigo)
        contatos[nome_contato_novo]['telefone'] = str(input("Insira o novo telefone: "))
        contatos[nome_contato_novo]['email'] = str(input("Insira o novo email: "))
        contatos[nome_contato_novo]['midias_sociais'] = [{'twitter': str(input("Insira o novo login do twitter: "))}]
        contatos[nome_contato_novo]['midias_sociais'].append({'instagram': str(input("Insira o novo login instagram: "))})

def inserir_contatos():
    try:
        qtd_usuarios = int(str(input("Quantos usuários deseja inserir? " )))
        contador = 0;
        while qtd_usuarios > contador:
            inserir()
            contador+=1

    except:
        print("Não é possivel converter o(s) carctere(s) que você digitou para número. ")
   

    
inserir()
consultar()
atualizar()
print(contatos)

