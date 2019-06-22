from tkinter.messagebox import showinfo
def Delete(ent1,ent2,root3,data,max_rows1):
    """
    Функция для удаления человека по имени и фамилии\n
    Принимает на вход:\n
                    ent1 - название виджета Entry, где написана фамилия\n
                    ent2 - название виджета Entry, где написано имя\n
                    root3 - название второстепенного окна, где пишется имя и фамилия\n
                    data - матрица из ссылок виджетов Entry\n
                    max_rows1 - количество строк в базе данных\n
    Возвращает:\n
            data - измененную матрицу из ссылок после удаления\n
            max_rows1 - измененное количество строк в базе данных после удаления\n
    Выполнил Нигметзянов И.И
    """
    sname = str(ent1.get())
    l=-1
    name = str(ent2.get())
    if sname != "" and name != "":
        root3.destroy()  # изменит на quit
        for lst in data:
            l+=1
            name1 = str(lst[0].get())
            name2 = str(lst[1].get())
            if sname == name1 and name == name2:
                max_rows1 -= 1
                for ent in lst:
                    ent.destroy()
                del data[l]
    else:
        showinfo(title="Внимание", message="Вы не написали имя или фамилию")
    return data, max_rows1