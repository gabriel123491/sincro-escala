funcionarios = []
sair_do_sistema = False

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
    funcionario = input("digite o nome do funcionario: ")
    funcionarios.append(funcionario)
    print(f"o nome cadastrado foi: {funcionario}")
    print("====================================")
    print("Você gostaria de adicionar um novo funcionário?")
    print("   1. Sim ✅")
    print("   2. Não ❌")
    seguir_cadastro = input("Escolha uma opção: ")
    print("====================================")
    if seguir_cadastro == "1":
        cadastrar_funcionario() 
    if seguir_cadastro == "2":
        print("Cadastre concluído! ✅")              
def listar_funcionario():
    print("listando_funcionario")
    
def sair():
    print("Saindo do sistema digestão de escala👋")
    
    
#=====================================================
 
while not sair_do_sistema:
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
