
num_ok = False
simbolo_ok = False
letra_ok = False

print('-------------------------------------------------------------------'
    '- Número mínimo de caracteres: 8;'
   '- Contenha pelo menos um número;' \
   '- Contenha uma letra maiúscula;' \
   '- Contenha um símbolo especial ("$", "&", "!", "?", "_", "#").'
   '-------------------------------------------------------------------')

while num_ok == False or simbolo_ok == False or letra_ok == False:

    num_ok = False
    simbolo_ok = False
    letra_ok = False

    print('-------------------------------------------------------')
    senha = input('Usuario031145, digite sua senha a seguir: \n\t')
    print('-------------------------------------------------------')

    if len(senha) >= 8 :
        caracteres_ok = True
        for num in '0123456789':
            if senha.find(num) != -1:
                num_ok = True
                break
        for simbolo in '$&!?_#':
            if senha.find(simbolo) != -1:
                simbolo_ok = True
                break
        for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': 
            if senha.find(letra) != -1:
                letra_ok = True
                break
        print('-------------------------------------------------------')
        print(f'\nNumero minimo de caracters: {caracteres_ok}\n' 
        f'Presença de numeros:  {num_ok}\n'
        f'Presença de simbolos: {simbolo_ok}\n'
        f'Presença de letra maiuscula: {letra_ok}\n')
        print('-------------------------------------------------------')
    else: 
        caracteres_ok =False
        print('-------------------------------------------------------')
        print('A senha precisa ter no minimo 8 digitos, tente novamente')
        print('-------------------------------------------------------')

print(f'{senha}, senha salva com sucesso\n')

