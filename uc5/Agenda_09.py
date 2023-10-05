#Criar uma agenda
#1. Adicionar Contato
#2. Listar Contatos
#3. Pesquisar Contato
#4. Sair

# Inicializa a agenda como um dicionário vazio
agenda = {}

# Função para adicionar um contato à agenda
def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    agenda[nome] = telefone
    print(f"Contato {nome} adicionado com sucesso!")

# Função para listar todos os contatos na agenda
def listar_contatos():
    print("Lista de Contatos:")
    for nome, telefone in agenda.items():
        print(f"Nome: {nome}, Telefone: {telefone}")

# Função para pesquisar um contato na agenda
def pesquisar_contato():
    nome = input("Digite o nome do contato que deseja pesquisar: ")
    if nome in agenda:
        print(f"Nome: {nome}, Telefone: {agenda[nome]}")
    else:
        print("Contato não encontrado na agenda.")

# Loop principal do programa
while True:
    print("\n--- Menu ---")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Pesquisar Contato")
    print("4. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        adicionar_contato()
    elif escolha == "2":
        listar_contatos()
    elif escolha == "3":
        pesquisar_contato()
    elif escolha == "4":
        print("Saindo da agenda. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
