"""
1. Escreva um programa para criar e gerenciar uma agenda telefônica, utilizando listas e dicionários. 
O código deve permitir ao usuário as seguintes opções:

- Criar um contato;
- Remover um contato;
- Editar um contato;
- Pesquisar um contato;
- Exibir todos os contatos.

As funcionalidades acima devem ser exibidas como um menu de opções para o usuário.

Cada contato deve apresentar, no mínimo, um nome e um número de telefone.
"""

agenda = {}

print("----------------------------------------------------------------\n"
          "                         AGENDA TELEFONICA\n"
          "\n"
          "                              FUNÇOES                         \n"
          "- Criar um contato\n"
          "- Remover um contato\n"
          "- Editar um contato\n"
          "- Pesquisar um contato\n"
          "- Exibir todos os contatos\n"
          "----------------------------------------------------------------\n")

while True:
    
      # Mostrar açoes possiveis (cada açao vai ser referente a um numero)
      action = int(input("Digite o numero referente ao comando que vc deseja iniciar"
            "1 - Criar um contato\n"
            "2 - Remover um contato\n"
            "3 - Editar um contato\n"
            "4 - Pesquisar um contato\n"
            "5 - Exibir todos os contatos\n"
            "Escolha o comando:  "))

      if action == 1:
            # Criar contato
            nome = input("Digite o nome do seu novo contato?:\n").lower() 
            if nome == 'sair' :
                  break

            num_ok = False
            simbolo_ok = False
            letra_ok = False

            while num_ok == False or simbolo_ok == True or letra_ok == True:

                  num_ok = False
                  simbolo_ok = False
                  letra_ok = False

                  num = input("Digite o numero do seu novo contato:\n")

                  if len(num) >= 8 :
                        caracteres_ok = True
                        for num in '0123456789':
                              if num.find(num) != -1:
                                    num_ok = True
                              break
                        for simbolo in '$&!?_#':
                              if num.find(simbolo) != -1:
                                    simbolo_ok = True
                              break
                        for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': 
                              if num.find(letra) != -1:
                                    letra_ok = True
                              break
                        print('-------------------------------------------------------')
                        print(f'\nNumero minimo de caracters: {caracteres_ok} \n' 
                        f'Presença de numeros:  {num_ok} (valor desejado: True)\n'
                        f'Presença de simbolos: {simbolo_ok} (valor desejado: False)\n'
                        f'Presença de letra maiuscula: {letra_ok} (valor desejado: False)\n')
                        print('-------------------------------------------------------')
                  else: 
                        caracteres_ok =False
                        print('-------------------------------------------------------')
                        print('O numro precisa ter no minimo 8 digitos, tente novamente')
                        print('-------------------------------------------------------')

            agenda[nome] = num
            print(agenda[nome])

      elif action == 2:
            # Remover contato
            nome = input("Digite o nome do contato que voce deseja deletar:\n").lower()
            if nome == 'sair' :
                  break

            try:
                  del agenda[nome]
            except KeyError:
                  print("Esse contato nao existe na sua agenda.")

      elif action == 3:
            # Editar um contato
            nome_antigo = input('Digite o nome do contato que voce deseja alterar:').lower()

            try:
                  del agenda[nome_antigo]
            except KeyError:
                  print("Esse contato nao existe na sua agenda.")
                         
            nome_novo = input("Digite o novo nome do seu contato?:\n").lower() 
            if nome_novo == 'sair' :
                  break

            num_ok = False
            simbolo_ok = False
            letra_ok = False
      
            while num_ok == False or simbolo_ok == True or letra_ok == True:

                  num_ok = False
                  simbolo_ok = False
                  letra_ok = False

                  num = input("Digite o novo numero do seu contato:\n").lower()

                  if len (num) >= 8 :
                        caracteres_ok = True
                        for num in '0123456789':
                              if num.find(num) != -1:
                                    num_ok = True
                                    break
                        for simbolo in '$&!?_#':
                              if num.find(simbolo) != -1:
                                    simbolo_ok = True
                                    break
                        for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': 
                              if num.find(letra) != -1:
                                    letra_ok = True
                                    break
                        print('-------------------------------------------------------')
                        print(f'\nNumero minimo de caracters: {caracteres_ok} \n' 
                        f'Presença de numeros:  {num_ok} (valor desejado: True)\n'
                        f'Presença de simbolos: {simbolo_ok} (valor desejado: False)\n'
                        f'Presença de letra maiuscula: {letra_ok} (valor desejado: False)\n')
                        print('-------------------------------------------------------')
                  else: 
                        caracteres_ok =False
                        print('-------------------------------------------------------')
                        print('O numro precisa ter no minimo 8 digitos, tente novamente')
                        print('-------------------------------------------------------')
            
            agenda[nome_novo] = num
            print (agenda[nome_novo])


      elif action == 4:
            # Pesquisar um contato
            nome = input('Digite o nome do contato que voce deseja pesquisar:').lower()
            try:
                  print(agenda(nome))
            except KeyError:
                  print('Esse contato nao existe')
            
      elif action == 5:
            # Exibir todos os contatos
            print(agenda,"\n")