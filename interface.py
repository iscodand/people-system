def line(len = 40):
    return '-' * len


def header(txt):
    print(line())
    print(txt.center(40))
    print(line())


def menu():
    header('MENU PRINCIPAL')
    print('1 - Mostrar Pessoas')
    print('2 - Adicionar Pessoa')
    print('3 - Fechar Programa')
    print(line())
        