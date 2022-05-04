from interface import *


def readArchive():
    archive = 'app/data.txt'

    try:
        with open(archive, 'r') as open_archive:
            for lines in open_archive:
                return lines

    except Exception as e:
        return f'\033[1;31m---- {e} ----\033[m'
    open_archive.close()


def modifyArchive():
    archive = 'app/data.txt'
    readArchive()

    try:
        with open(archive, 'a+') as open_archive:
            open_archive.writelines(str(input('Nome: ')))
            open_archive.writelines(str(input('Idade: ')))

    except Exception as e:
        print(f'\033[1;31m---- {e} ----\033[m')

    return readArchive()
