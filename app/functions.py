from interface import *


archive = 'app/data.txt'

def read_archive():

    try:
        with open(archive, 'r') as open_archive:
            for lines in open_archive:
                return lines

    except Exception as e:
        print(f'\033[1;31m---- {e} ----\033[m')


def modify_archive():

    read_archive()

    try:
        with open(archive, 'a+') as open_archive:
            name = open_archive.writelines(str(input('Nome: ')).capitalize())
            age = open_archive.writelines(str(input('Idade: ')))
            
    except Exception as e:
        print(f'\033[1;31m---- {e} ----\033[m')

    return read_archive()
