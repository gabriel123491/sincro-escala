from funcionario import cadastrar_funcionario, listar_funcionarios, excluir_funcionarios
from escala import cadastrar_escalas, listar_escalas, excluir_escala
from relacionamento import menu_participacoes

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
    print("   7. Relacionar funcionários e escalas 🔗")
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
                print("======================================")
                print("     CADASTRO DE FUNCIONARIOS")
                print("======================================")
                print("")    
                cadastrar_funcionario() 
            case "2":
                print("======================================")
                print("     LISTA DE FUNCIONARIOS")
                print("======================================")
                print("")
                listar_funcionarios()
            case "3":
                print("======================================")
                print("     REMOÇÃO DE FUNCIONARIOS")
                print("======================================")
                print("")
                excluir_funcionarios()
            case "4":
                print("======================================")
                print("     CADASTRO DE ESCALAS")
                print("======================================")
                print("")   
                cadastrar_escalas() 
            case "5":
                print("======================================")
                print("     LISTA DE ESCALAS")
                print("======================================")
                print("")
                listar_escalas() 
            case "6":
                print("======================================")
                print("     REMOÇÃO DE ESCALAS")
                print("======================================")
                print("")
                excluir_escala() 
            case "7":
                print("")
                menu_participacoes()     
            case "0":
                sair()
                break
            case _:  
                print("Opção Inválida!") 
