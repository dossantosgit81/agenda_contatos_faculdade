db = []

contato = {'nome': '', 'telefone': '', 'email': '', 'midias_sociais': []}

def inserir():
    contato['nome'] = str(input("Insira seu nome aqui: ")) 
    contato['telefone'] = str(input("Insira telefone aqui: "))
    contato['email'] = str(input("Insira seu email aqui: "))
    contato['midias_sociais'].append({'twitter': str(input("Insira seu twitter aqui:  "))}) 
    contato['midias_sociais'].append({'instagram': str(input("Insira seu instagram aqui:  "))})
    db.append(contato)

inserir()
print(db)