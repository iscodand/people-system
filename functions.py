def readArchive():
    try:
        archive = 'data.txt'
        open_archive = open(archive, 'r')
        for line in open_archive:
            print(line)
    except Exception as e:
        print(f'\033[1;31m---- {e} ----\033[m')


def modifyArchive():
    archive = 'data.txt'
    try:
        readArchive()
        with (open(archive, 'a')) as open_archive:
            open_archive.writelines(str(input('Nome: ')))
            open_archive.writelines(str(input('Idade: ')))
            return readArchive()
    except Exception as e:
        print(f'\033[1;31m---- {e} ----\033[m')
