from data import documents, directories

LIST_COMMANDS = '''
p – выводит имя человека, по введенному номеру документа;
s – выводит номер полки, на которой находится документ с введенным номером;
l – выводит список всех документов
a – добавляет новый документ в каталог и в перечень полок
q - выход
'''


def find_doc(num):
    o_id = None
    for id, doc in enumerate(documents):
        if num == doc["number"]:
            o_id = id
    return o_id


def find_shelf(num):
    o_key = None
    for k, v in directories.items():
        if num in v:
            o_key = k
    return o_key


def people(num):
    id = find_doc(num)
    if id is not None:
        result = documents[id]["name"]
    else:
        result = f"Документа с номером {num} нет."
    return result


def shelf(num):
    o_key = find_shelf(num)
    if o_key is not None:
        result = o_key
    else:
        result = f"Документ с номером {num} не найден на полках."
    return result


def add(itype, inum, iname, ishelf):
    id = find_doc(inum)
    if id is not None:
        result = f"Документ с номером {inum} уже есть в базе."
    else:
        if ishelf in directories:
            idict = {}
            idict["type"] = itype
            idict["number"] = inum
            idict["name"] = iname
            documents.append(idict)
            directories[ishelf].append(inum)
            result = f"Документ с номером {inum} добавлен. Помещен на полку {ishelf}."
        else:
            result = f'Нет полки с номером {ishelf}. Документ не добавлен.'
    return result


if __name__ == '__main__':

    print(LIST_COMMANDS)

    run = True
    while run:
        command = input('Введите команду: ')
        if command == 'q':
            run = False
        elif command == 'p':
            inum = input('Введите номер документа: ')
            res = people(inum)
            print(res)
        elif command == 's':
            inum = input('Введите номер документа: ')
            res = shelf(inum)
            print(res)
        elif command == 'l':
            for el in documents:
                type, number, name = el.values()
                print(type, number, name)
        elif command == 'a':
            itype = input('Введите тип документа: ')
            inum = input('Введите номер документа: ')
            iname = input('Введите имя владельца: ')
            ishelf = input('Введите номер полки: ')
            res = add(itype, inum, iname, ishelf)
            print(res)
        else:
            print('Неизвестная команда')
