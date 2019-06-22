import pickle as pk
def Load_data(Path):
    """
    Функция для прочтения файла\n
    Принимает:\n
            Path - путь файла\n
    Возвращает:\n
            d - значение файла (словарь словарей)\n
    Выполнил Сапожников А.А.
    """
    fn = open(Path, 'rb')
    d = pk.load(fn)
    fn.close()
    return d