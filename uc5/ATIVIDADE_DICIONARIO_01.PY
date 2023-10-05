#atividade 01

#01. Acessar as informações de contato de uma pessoa específica a partir do dicionário "contatos". Por exemplo, imprimir o telefone e o email de "Alice".
contatos = {
    'Bob': {'telefone': '987-654-3210', 'email': 'bob@email.com'},
    'Alice': {'telefone': '123-456-7890', 'email': 'alice@email.com'}
}

# Nome da pessoa que você deseja acessar
nome_da_pessoa = 'Alice'

# Verifique se o nome da pessoa está no dicionário
if nome_da_pessoa in contatos:
    # Acessando as informações de contato da pessoa
    pessoa_info = contatos[nome_da_pessoa]
    telefone = pessoa_info['telefone']
    email = pessoa_info['email']

    # Imprimindo as informações de contato da pessoa
    print(f'Informações de contato de {nome_da_pessoa}: Telefone - {telefone}, Email - {email}')
else:
    print(f'{nome_da_pessoa} não foi encontrado nos contatos.')


#02. Adicionar novas pessoas e suas informações de contato ao dicionário "contatos".

# Adicionando as informações de contato de Pedro
contatos['Pedro'] = {'telefone': '111-222-3333', 'email': 'pedro@email.com'}

# Adicionando as informações de contato de João
contatos['João'] = {'telefone': '444-555-6666', 'email': 'joao@email.com'}

#03. Modificar as informações de contato de uma pessoa existente no dicionário "contatos". Por exemplo, atualizar o email de "Bob".

contatos['Bob']['email'] = 'novo_email_bob@email.com'

#04. Excluir um contato específico do dicionário "contatos". Por exemplo, remover o contato de "Alice".

del contatos['Alice']

#05. Desafio (+1 pt): listar todos os nomes de pessoas no dicionário "contatos" em ordem alfabética.#

contatos = {
    'Bob': {'telefone': '987-654-3210', 'email': 'bob@email.com'},
    'Alice': {'telefone': '123-456-7890', 'email': 'alice@email.com'},
    
   
'Pedro': {'telefone': '111-222-3333', 'email': 'pedro@email.com'},
    'João': {'telefone': '444-555-6666', 'email': 'joao@email.com'}
}

# Imprimindo os nomes em ordem alfabética diretamente
for nome in sorted(contatos.keys()):
    
   
print(nome)

``
Nnomes_em_ordem_alfabetica,sorted()diretamente nãofor,





