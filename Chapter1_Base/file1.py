def readAll():
    with open('dict1.py') as file1:
        content = file1.read()
        print(content)


def readByLine():
    with open('dict1.py') as file1:
        contents = file1.readlines()
        for content in contents:
            print(content.rstrip())


if __name__ == '__main__':
    print('Revert readAll():')
    readAll()
    print('RevertByLine():')
    readByLine()
