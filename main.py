def apresenta_menu():
    print("====================================")
    print("     SISTEMA DIGESTÃO DE ESCALA     ")
    print("====================================")
    print("")
    print("   1. Cadastrar funcionário 🙎")
    print("   2. Listar funcionário 🙎🙎")
    print("   0. Sair ❌")
    print("")
    opcao_menu = input("Escolha uma opção: ")
    return opcao_menu
    
    

def cadastrar_funcionario():
    funcionarios = input("digite o nome do funcionario: ")
    print(f"o nome cadastrado foi: {funcionarios}")
    
def listar_funcionario():
    print("listando_funcionario")
    
def sair():
    print("Saindo do sistema digestão de escala👋")
    
    
#=====================================================
    
opcao_menu = apresenta_menu()


match opcao_menu:
        case "1":
            cadastrar_funcionario() 
        case "2":
            listar_funcionario() 
        case "0":
            sair()
        case _:  
            print("Opção Inválida!")
