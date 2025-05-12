from funçoes import *

def exibir_menu():
    print("\n======= MENU DA AGENDA =======")
    print("1. Criar contato")
    print("2. Remover contato")
    print("3. Pesquisar contato")
    print("4. Exibir todos os contatos")
    print("5. Editar contato")
    print("6. Salvar e sair")
    print("==============================")
    return input("Escolha uma opção (1-6): ")


def main():
    agenda = carregar_agenda()
    print("Agenda carregada com sucesso!")

    while True:
        opcao = exibir_menu()

        match opcao:
            case "1":
                nome = input("Digite o nome do contato: ").strip()
                if nome in agenda:
                    print("Esse nome já existe na agenda. Use outro.")
                else:
                    agenda = criar_contato(nome, agenda)

            case "2":
                nome = input("Digite o nome do contato a ser removido: ").strip()
                agenda = remover_contato(nome, agenda)

            case "3":
                nome = input("Digite o nome do contato a ser pesquisado: ").strip()
                pesquisar_contato(nome, agenda)

            case "4":
                exibir_contatos(agenda)

            case "5":
                nome = input("Digite o nome do contato a ser editado: ").strip()
                agenda = editar_contato(nome, agenda)

            case "6":
                salvar_agenda(agenda)
                print("Saindo do programa...")
                break

            case _:
                print("Opção inválida. Por favor, escolha entre 1 e 6.")


if __name__ == "__main__":
    main()