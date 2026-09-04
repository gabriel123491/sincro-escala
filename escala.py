from pathlib import Path

path_bd = Path("sincro-escalas/BD") / "escalas_bd.txt"
escalas = []

def cadastrar_escalas():
    escala = input("digite o nome das escalas!: ")
    with open(path_bd,"a", encoding="utf-8") as arquivo:
        arquivo.write(f"{escalas}\n")
    escalas.append(escalas)
    print(f"O nome cadastrado foi: {escala}")
    print("======================================")
    print("você gostaria de adicionar novas escalas?")
    print("1. Sim ✅")
    print("2. Não ❌")
    seguir_cadastro = input("Escolha uma opção: ")
    print("======================================")
    if seguir_cadastro  == "1":    
        cadastrar_escalas()
    if seguir_cadastro == "2":
        print("cadastro concluido ✅")