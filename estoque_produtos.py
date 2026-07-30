def adicionar_produto(estoque):
    nome = input("Nome do produto: ")
    
    if nome in estoque:
        print("Erro: Produto já cadastrado!")
        return
    
    quantidade = int(input("Quantidade: "))
    preco = float (input("Preço: R$ "))
    
    estoque[nome] = {
        "Quantidade": quantidade,
        "Preço": preco
    }
    
    print("Produto adicionado com sucesso! \n")
    
    
def listar_produtos(estoque):
    if not estoque:
        print("Estoque vazio! \n")
        return
    
    print("\n Lista de Produtos")
    
    for nome, dados in sorted(estoque.items(), key=lambda item: item[0].lower()):
        print(f"{nome}: {dados['Quantidade']} disponível(is) por R$ {dados['Preço']:.2f}")
        
    print()
    
def remover_produto(estoque):
    nome = input("Nome do produto remover: ")
    
    if nome in estoque:
        del estoque[nome]
        print("Produto removido com sucesso! \n")
        
    else:
        print("Erro: Produto não encontrado! \n")
        
        
def atualizar_quantidade(estoque):
    nome = input("Nome do produto: ")
    
    if nome in estoque:
        nova_quantidade = int(input("Nova quantidade: "))
        estoque[nome]["Quantidade"] = nova_quantidade
        print("Quantidade atualizada com sucesso! \n")
    else:
        print("Erro: Produto não encontrado! \n")
        
    for nome, dados in sorted(estoque.items(), key=lambda item: item[0].lower()):
        print(f"{nome}: {dados['Quantidade']} disponível(is) por R$ {dados['Preço']:.2f}")
    
def menu ():
    estoque = {}
    
    while True:
        
        print("Menu")
        print("1 - Adicionar Produto")
        print("2 - Listar Produtos")
        print("3 - Remover Produto")
        print("4 - Atualizar Quantidade de Produto")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_produto(estoque)
            
        elif opcao == "2":
            listar_produtos(estoque)
            
        elif opcao == "3":
            remover_produto(estoque)
            
        elif opcao == "4":
            atualizar_quantidade(estoque)
            
        elif opcao == "5":
            print("Encerrando...")
            break
        
        else:
            print("Opção inválida. Tente novamente! \n")
            
menu()
                