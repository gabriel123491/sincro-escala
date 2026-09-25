import json
from pathlib import Path

path_bd = Path(__file__).parent / "BD" / "funcionario_bd.json"
funcionarios = []

def _carregar_funcionarios():
    if not path_bd.exists():
        return []
    
    with open(path_bd,"r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

    
def cadastrar_funcionario():
    funcionarios = _carregar_funcionarios()
    
    print("====================================")
    print("       CADASTRAR FUNCIONARIOS       ")
    print("====================================")
    print("")
    listar_funcionarios()
    print("")
    print("====================================")

    nome = input("digite o nome: ")
    proximo_id = max((f["id"] for f in funcionarios), default=0) + 1
    funcionarios.append({"id": proximo_id, "nome":nome})
    with open(path_bd,"w", encoding="utf-8") as arquivo:
        json.dump(funcionarios, arquivo, ensure_ascii=False, indent= 4)
    print(f"O nome cadastrado foi: {nome}")
    print("======================================")
    print("você gostaria de adicionar um novo funcionário?")
    print("1. Sim ✅")
    print("2. Não ❌")
    seguir_cadastro = input("Escolha uma opção: ")
    print("======================================")
    if seguir_cadastro  == "1":    
        cadastrar_funcionario()
    if seguir_cadastro == "2":
        print("cadastro concluido ✅")
        
def listar_funcionarios():
    funcionarios = _carregar_funcionarios()
    for f in funcionarios:
        print(f"id: {f['id']} - nome: {f['nome']}")
            
def excluir_funcionarios():
    listar_funcionarios()
    funcionário = input("Qual funcionário você deseja deletar: ")
    
    with open(path_bd,"w", encoding="utf-8") as arquivo:
        for linha in funcionarios:
            print(linha)
            print(funcionário)
            if linha == funcionário:
                funcionarios.remove(linha)
                linha = ""
            arquivo.write(linha)
