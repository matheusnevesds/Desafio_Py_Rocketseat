# Função para adicionar contato
def adicionar_contato():
    print("\nAdicionar Contato\n")
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o e-mail do contato: ")
    favorito = input("É um contato favorito? (S/N): ").upper()

    # Verifique se o usuário digitou "S" para favorito
    if favorito == "S":
        favorito = True
    else:
        favorito = False

    # Crie um dicionário com os dados do contato
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": favorito
    }

    # Adicione o contato à lista de contatos
    contatos.append(contato)
    print("\nContato adicionado com sucesso!\n")


# Função para visulizar contatos
def visualizar_contatos():
    print(f"\nLista de Contatos:\n" ) 
    for contato in contatos:
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"E-mail: {contato['email']}")
        print(f"Favorito: {'Sim' if contato['favorito'] else 'Não'}")
        print("-" * 20)
        print()


# Função para editar contato
def editar_contato():
    nome_contato = input("\nDigite o nome do contato que deseja editar: ")

    for contato in contatos:
        if contato['nome'] == nome_contato:
            print(f"Editando contato: {contato['nome']}")
            contato['telefone'] = input("\nDigite o novo telefone: ")
            contato['email'] = input("Digite o novo e-mail: ")
            print("\nContato atualizado com sucesso!")
            return

    print(f"\nContato '{nome_contato}' não encontrado.\n")


# Função para marcar contato como favorito
def marcar_favorito():
    nome_contato = input("\nDigite o nome do contato: ")

    for contato in contatos:
        if contato['nome'] == nome_contato:
            contato['favorito'] = not contato['favorito']
            print(f"Contato '{contato['nome']}' marcado como favorito!\n" if contato['favorito'] else "\nContato desmarcado como favorito.\n")
            return

    print(f"\nContato '{nome_contato}' não encontrado.\n")


# Função para exibir apenas os contatos favoritos
def contatos_favoritos():
    print("\nContatos Favoritos:\n")
    for contato in contatos:
        if contato['favorito']:
            print(f"Nome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"E-mail: {contato['email']}")
            print("-" * 20)
            print()

# Função para apagar contato
def apagar_contato():
    nome_contato = input("\nDigite o nome do contato que deseja apagar: ")

    for contato in contatos:
        if contato['nome'] == nome_contato:
            contatos.remove(contato)
            print(f"\nContato '{nome_contato}' apagado com sucesso!\n")
            return

    print(f"\nContato '{nome_contato}' não encontrado.\n")


# Cria uma lista vazia para armazenar os contatos
contatos = []

# Loop para exibir o menu de opções
while True:
    print("\nAgenda de Contatos\n1")
    print("1. Adicionar Contato")
    print("2. Visualizar Contatos")
    print("3. Editar Contato")
    print("4. Marcar/Desmarcar como Favorito")
    print("5. Ver Contatos Favoritos")
    print("6. Apagar Contato")
    print("0. Sair")
    print('')
    opcao = input('Escolha uma opção: ')

    # Condicionais para selecionar opção
    if opcao == '1':
        adicionar_contato()

    elif opcao == '2':
        visualizar_contatos()

    elif opcao == '3':
        editar_contato()

    elif opcao == '4':
        marcar_favorito()

    elif opcao == '5':
        contatos_favoritos()
    elif opcao == '6':
        apagar_contato()

    elif opcao == '0':
        break

    
    

