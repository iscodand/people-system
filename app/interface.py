def line(len=40):
    return '\033[;1m-\033[m' * len


def header(txt):
    print(line())
    print(txt.center(42))
    print(line())


def menu():
    header('\033[1;33m MENU PRINCIPAL \033[m')
    print('\033[1;33m 1 - Mostrar Pessoas \033[m')
    print('\033[1;33m 2 - Adicionar Pessoa \033[m')
    print('\033[1;33m 3 - Fechar Programa \033[m')
    print(line())


def menu_person():
    print(line())
    print(f'{"NOME":^10} {"IDADE":^40}')
    print(line())
