from interface import *
from functions import *
from time import sleep


while True:
    menu()

    option_selected = int(input('\033[1;94m\nInsira sua Opção ----> \033[m'))
    print()

    if option_selected == 1:
        print(f'\n{read_archive()}\n')

    elif option_selected == 2:
        print(f'\n{modify_archive()}\n')

    elif option_selected == 3:
        print('\033[1;32m\n---- OBRIGADO POR USAR O PROGRAMA ----\n\033[m')
        break

    else:
        print('\033[1;31m\n---- POR FAVOR, INSIRA UMA OPÇÃO VÁLIDA!!! ----\n\033[m')

    sleep(2)
