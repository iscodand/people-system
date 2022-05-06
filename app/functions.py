from interface import *


archive = 'app/data.txt'

def read_archive():

    menu_person()

    try:
        with open(archive, 'r') as open_archive:
            return open_archive.read()

    except Exception as e:
        print(f'\033[1;31m---- {e} ----\033[m')


def modify_archive():

    print(line())

    try:
        with open(archive, 'a+') as open_archive:
            name = open_archive.writelines(str(input('Nome: ')).upper() + f'{" ":>15}')
            age = open_archive.writelines((str(input('Idade: ')) + f'{" ":<5}' + '\n'))
            
    except Exception as e:
        print(f'\033[1;31m---- {e} ----\033[m')

    return read_archive()
