db = []

midias_sociais = []
contatos = {'nome': '', 'telefone': '', 'email': '', 'contas': []}

def inserir():
    contatos['nome'] = str(input("Insira seu nome aqui: ")) 
    contatos['telefone'] = str(input("Insira telefone aqui: "))
    contatos['email'] = str(input("Insira seu email aqui: "))
    contatos['contas'].append({'twitter': str(input("Insira seu twitter aqui:  "))}) 
    contatos['contas'].append({'instagram': str(input("Insira seu instagram aqui:  "))})
    db.append(contatos)

inserir()
print(db)