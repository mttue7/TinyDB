from tinydb import TinyDB, Query

# Criando o banco de dados
db = TinyDB('tarefas_db.json')

# Função para adicionar uma tarefa
def adicionar_tarefa(tarefa):
    db.insert({'tarefa': tarefa})

# Função para listar todas as tarefas
def listar_tarefas():
    tarefas = db.all()
    for idx, tarefa in enumerate(tarefas, start=1):
        print(f"{idx}. {tarefa['tarefa']}")

# Função para remover uma tarefa
def remover_tarefa(nome_tarefa):
    Tarefa = Query()
    tarefa = db.get(Tarefa.tarefa == nome_tarefa)
    if tarefa:
        db.remove(Tarefa.tarefa == nome_tarefa)
        print(f"Tarefa '{nome_tarefa}' removida com sucesso!")
    else:
        print("Tarefa não encontrada!")

# Função principal
def main():
    while True:
        print("\n=== Lista de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            tarefa = input("Digite a tarefa: ")
            adicionar_tarefa(tarefa)
        elif opcao == '2':
            print("\n--- Tarefas ---")
            listar_tarefas()
        elif opcao == '3':
            nome_tarefa = input("Digite o nome da tarefa a ser removida: ")
            remover_tarefa(nome_tarefa)
        elif opcao == '4':
            break
        else:
            print("Opção inválida! Tente novamente.")

    # Fechando a conexão com o banco de dados
    db.close()

if __name__ == "__main__":
    main()
