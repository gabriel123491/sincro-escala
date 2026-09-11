from funcionario import cadastrar_funcionario, listar_funcionarios, excluir_funcionarios
from escala import cadastrar_escalas, listar_escalas, excluir_escala


sair_do_sistema = False

def apresenta_menu():
    print("====================================")
    print("     SISTEMA DIGESTÃO DE ESCALA     ")
    print("====================================")
    print("")
    print("   1. Cadastrar funcionário 🙎")
    print("   2. Listar funcionário 🙎🙎")
    print("   3. Excluir funcionário 🗑️​")
    print("   4. Cadastrar Escalas📃")
    print("   5. Listar Escalas📃📃")
    print("   6. Excluir escala🗑️")
    print("   0. Sair ❌")
    print("")
    opcao_menu = input("Escolha uma opção: ")
    print("")
    return opcao_menu

   
def sair():
    print("Saindo do sistema digestão de escala👋")
    
    
#=====================================================
 
while not sair_do_sistema:
    opcao_menu = apresenta_menu()

    match opcao_menu:
            case "1":
                cadastrar_funcionario() 
            case "2":
                listar_funcionarios()
            case "3":
                excluir_funcionarios()
            case "4":
                cadastrar_escalas() 
            case "5":
                listar_escalas() 
            case "6":
                excluir_escala()      
            case "0":
                sair()
                break
            case _:  
                print("Opção Inválida!") 
