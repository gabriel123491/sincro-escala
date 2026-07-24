# 💻 Guia de Desenvolvimento: Sistema de Escalas via Terminal (CLI)

Este documento é o mapa de desenvolvimento para o nosso sistema de gerenciamento de escalas. Ele funciona como um guia de passos (backlog) projetado especificamente para programadores iniciantes praticarem lógica de programação pura no terminal.

---

## 📌 Fase 1: Menu Interativo e Estrutura de Dados
*O objetivo desta fase é criar a navegação do programa e aprender a guardar dados na memória.*

### 🔁 Menu Principal em Loop
* Criar um loop (`while`) que mantém o programa rodando até que o usuário digite a opção de sair.
* Exibir opções de texto numeradas na tela usando comandos de saída (Ex: `print`/`console.log`).
  * *Exemplo de Menu:*
    ```text
    --- GERENCIADOR DE ESCALAS ---
    1. Cadastrar Funcionário
    2. Alocar Funcionário em um Turno
    3. Visualizar Escala Completa
    0. Sair do Programa
    ------------------------------
    Escolha uma opção: 
    ```

### 👥 Armazenamento na Memória
* Criar estruturas de dados (Listas, Vetores ou Dicionários) para guardar os nomes dos funcionários.
* Criar uma estrutura para associar o Nome do Funcionário ao Dia e ao Turno (Ex: Manhã, Tarde, Noite).

---

## 📌 Fase 2: Lógica de Alocação e Visualização
*Aqui o foco é fazer as funções do menu funcionarem e exibir os dados de forma limpa.*

### ✍️ Fluxo de Cadastro e Alocação
* **Opção 1**: Ler o nome digitado pelo usuário e salvá-lo na lista de funcionários.
* **Opção 2**: Listar os funcionários cadastrados, pedir para o usuário escolher um, digitar o dia da semana e escolher o turno.

### 📅 Visualização de Dados (Relatório)
* **Opção 3**: Usar estruturas de repetição (`for` ou `foreach`) para percorrer os dados guardados e exibi-los linha por linha no terminal.
  * *Exemplo de Saída:*
    ```text
    --- ESCALA DA SEMANA ---
    Segunda-feira | Manhã | Funcionário: Carlos
    Segunda-feira | Tarde | Funcionário: Mariana
    Terça-feira   | Noite | Funcionário: Roberto
    ------------------------
    ```

---

## 📌 Fase 3: Validações e Regras (Evitando Bugs)
*Treino intensivo de estruturas condicionais (`if` / `else`) para proteger o sistema.*

### ❌ Validação de Choque de Horários
* Criar uma verificação que impeça que o mesmo funcionário seja escalado no **mesmo dia e no mesmo turno** duas vezes.

### 🛡️ Proteção contra Entradas Inválidas
* Garantir que o sistema não trave se o usuário digitar uma opção que não existe no menu.
* Exibir mensagens de alerta amigáveis no terminal (Ex: `"Erro: Funcionário não encontrado!"` ou `"Opção inválida!"`).

---

## 📌 Fase 4: Persistência de Dados Básica (Opcional/Avançado)
*Para os dados não sumirem toda vez que o terminal for fechado.*

### 💾 Salvar e Carregar Arquivo de Texto (`.txt`)
* Criar uma função que pega as listas de dados e as escreve linha por linha em um arquivo de texto comum na mesma pasta do projeto.
* Fazer o programa tentar ler esse arquivo de texto assim que for iniciado, preenchendo as listas automaticamente antes de exibir o menu.

---

## 🛠️ Dicas para o Desenvolvimento
1. **Faça uma coisa por vez**: Não tente programar a validação (Fase 3) antes de conseguir fazer o menu e o cadastro simples funcionarem (Fase 1).
2. **Use comandos de saída para testar**: Abuse do `print`/`console.log` no meio do código para ver o que está acontecendo com as suas variáveis enquanto testa o sistema.
3. **Mantenha o código limpo**: Divida cada funcionalidade (cadastrar, listar, validar) em funções separadas para o código não virar um bloco gigante e confuso.
