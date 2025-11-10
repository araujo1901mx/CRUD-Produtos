#CRUD de produtos de uma loja


# Lista global que armazena todos os produtos cadastrados
produtos = []
# Função para criar um novo produto
def criar_produto():
    try:
        # Solicita o nome do produto e formata o texto
        nome = input("Digite o nome do produto: ").strip().title()
        # Solicita o preço e tenta converter para float
        preco = float(input("Digite o preço do produto: "))
    except ValueError:
        # Caso o usuário digite algo que não seja número
        print("Preço inválido. Tente novamente.")
        return
    # Verifica se o preço é negativo
    if preco < 0:
        print("O preço não pode ser negativo. Tente novamente.")
        return
    # Cria o dicionário com as informações do produto
    produto = {"nome": nome, "preco": preco}
    # Adiciona o produto à lista global
    produtos.append(produto)
    print("Produto criado com sucesso!")
# Função para listar todos os produtos cadastrados
def ler_produtos(): 
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        # Usa enumerate() para mostrar o índice de cada produto
        for i, produto in enumerate(produtos):
            print(f"{i + 1}. Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")
# Função para atualizar um produto existente
def atualizar_produto():
    ler_produtos() # Mostra os produtos antes de atualizar
    try:
        # Usuário escolhe o índice do produto (ajustado com -1)
        indice = int(input("Digite o índice do produto a ser atualizado: ")) - 1
    except ValueError:
        print("Índice inválido. Tente novamente.")
        return
    # Verifica se o índice existe na lista
    if 0 <= indice < len(produtos):
        try:
            # Solicita novo nome e novo preço
            novo_nome = input("Digite o novo nome do produto: ").strip().title()
            novo_preco = float(input("Digite o novo preço do produto: "))
        except ValueError:
            print("Preço inválido. Tente novamente.")
            return
        # Atualiza os dados no dicionário  
        produtos[indice]["nome"] = novo_nome
        produtos[indice]["preco"] = novo_preco
        print("Produto atualizado com sucesso!")
    else:
        print("Índice inválido.")
# Função para deletar um produto
def deletar_produto():
    ler_produtos() # Mostra os produtos antes de deletar
    try:
        indice = int(input("Digite o índice do produto a ser deletado: ")) - 1
    except ValueError:
        print("Índice inválido. Tente novamente.")
        return
    if 0 <= indice < len(produtos):
        # Remove o produto pelo índice
        produtos.pop(indice)
        print("Produto deletado com sucesso!")
    else:
        print("Índice inválido.")
# Função principal com o menu de opções
def menu():
    while True:
        print("\nMenu de Produtos")
        print("1. Criar Produto")
        print("2. Ler Produtos")
        print("3. Atualizar Produto")
        print("4. Deletar Produto")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            criar_produto()
        elif escolha == "2":
            ler_produtos()
        elif escolha == "3":
            atualizar_produto()
        elif escolha == "4":
            deletar_produto()
        elif escolha == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
# Ponto de entrada do programa
if __name__ == "__main__":
    menu()

