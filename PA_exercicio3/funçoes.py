import json
import os


def criar_contato(nome: str, agenda: dict) -> dict:
    while True:
        num = input("Digite o número do seu novo contato:\n")

        if len(num) < 8:
            print("O número precisa ter no mínimo 8 dígitos. Tente novamente.")
            continue

        num_ok = any(c.isdigit() for c in num)
        simbolo_ok = any(c in '$&!?_#' for c in num)
        letra_ok = any(c.isalpha() for c in num)

        print('-------------------------------------------------------')
        print(f'Presença de números:  {num_ok} (desejado: True)')
        print(f'Presença de símbolos: {simbolo_ok} (desejado: False)')
        print(f'Presença de letras:   {letra_ok} (desejado: False)')
        print('-------------------------------------------------------')

        if num_ok and not simbolo_ok and not letra_ok:
            agenda[nome] = num
            print("Contato criado com sucesso!")
            break
        else:
            print("Número inválido. Deve conter apenas dígitos numéricos e ter ao menos 8 dígitos.")

    return agenda


def remover_contato(nome: str, agenda: dict) -> dict:
    if nome in agenda:
        del agenda[nome]
        print(f"Contato '{nome}' removido com sucesso.")
    else:
        print("Esse contato não existe na sua agenda.")
    return agenda


def pesquisar_contato(nome: str, agenda: dict) -> None:
    if nome in agenda:
        print(f'Nome: {nome}\nNúmero: {agenda[nome]}')
    else:
        print('Esse contato não existe.')


def exibir_contatos(agenda: dict) -> None:
    if agenda:
        print("=== Lista de Contatos ===")
        for nome, numero in agenda.items():
            print(f'Nome: {nome} - Número: {numero}')
    else:
        print("Agenda vazia.")

def editar_contato(nome: str, agenda: dict) -> dict:
    if nome not in agenda:
        print("Esse contato não existe.")
        return agenda

    print(f"Contato atual - Nome: {nome}, Número: {agenda[nome]}")
    novo_nome = input("Digite o novo nome (ou pressione Enter para manter o mesmo): ").strip()
    novo_numero = input("Digite o novo número (ou pressione Enter para manter o mesmo): ").strip()

    if novo_nome:
        agenda[novo_nome] = agenda.pop(nome)
        nome = novo_nome  # Atualiza nome para edição de número se necessário

    if novo_numero:
        agenda[nome] = novo_numero

    print("Contato atualizado com sucesso.")
    return agenda


def salvar_agenda(agenda: dict) -> None:
    with open('agenda.txt', 'w', encoding='utf-8') as f:
        json.dump(agenda, f, ensure_ascii=False, indent=4)
    print("Agenda salva com sucesso!")


def carregar_agenda() -> dict:
    if os.path.exists('agenda.txt'):
        with open('agenda.txt', 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}


if __name__ == "__main__":
    agenda = carregar_agenda()
    criar_contato("Maria", agenda)
    exibir_contatos(agenda)
    salvar_agenda(agenda)
