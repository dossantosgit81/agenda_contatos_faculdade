contatos = {}

msg_contato_inexistente = "Verfique se o nome que você digitou realmente existe."

def inserir():
    nome_contato = str(input("Insira o nome do contato aqui: ")).capitalize() 
    contatos[nome_contato] = {}
    contatos[nome_contato]['telefone'] = str(input("Insira o telefone aqui: "))
    contatos[nome_contato]['email'] = str(input("Insira o email aqui: "))
    contatos[nome_contato]['midias_sociais'] = [{'twitter': str(input("Insira seu twitter aqui:  "))}]
    contatos[nome_contato]['midias_sociais'].append({'instagram': str(input("Insira seu instagram aqui:  "))})
    print("Contato inserido com sucesso!")

def remover():
    try:
        del contatos[str(input("Insira o nome do contato que deseja remover." )).capitalize()]
        print("Contato removido com sucesso!!!")
    except:
        print(msg_contato_inexistente)

def consultar():
    try:
        print(contatos[str(input("Insira o nome do contato que deseja encontrar." )).capitalize()])
    except:
        print(msg_contato_inexistente)

def atualizar():
   # try:
        
        nome_contato_atualizar = str(input("Insira o nome do contato que deseja remover." )).capitalize()
        contatos[nome_contato_atualizar] = contatos[nome_contato_atualizar]
       # contatos[]
    #:

    
inserir()
consultar()
print(contatos)

