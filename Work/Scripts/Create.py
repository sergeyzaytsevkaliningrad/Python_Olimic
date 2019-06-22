from tkinter import *
from tkinter.messagebox import showerror
def Create(data,root,ent1,ent2,root1,color6,color7,color8,color9,font1):
    """
    Функция для созданеия базы данных с нуля\n
    Принимает на вход:\n
                    data - матрицу из ссылок виджетов Entry\n
                    root - название гл окна\n
                    ent1 - название виджета, где хранится количества строк\n
                    ent2 - название виджета, где хранится количества столбцов\n
                    root1 - название второстепенног окна, где спрашивает о количестве строк и столбцов\n
    Возвращает:\n
            rows - матрицу из ссылок виджетов Entry\n
            max_rows - максимальный индекс у виджета Entry\n
            max_cols - количество столбцов\n
            max_rows - количество строк\n
    Выполнил Нигметзянов И.И
    """
    l = 0
    try:
        max_rows = int(ent1.get())
        max_cols = int(ent2.get())
        l += 1
    except:
        showerror("Ошибка", "Проверьте введенные вами значения\nвсе поля должны быть заполнены\nа также не содержать букв")
    if l==1:
        root1.destroy() #изменит на quit
        if data:
            for lst in data:
                for ent in lst:
                    ent.destroy()
            for lst in data:
                del data[0]
        rows = []
        z = -1
        for i in range(1) :
            z += 1
            l = -1
            cols = []
            for j in range(max_cols):
                l += 1
                ent = Entry(root,width=20,relief=RIDGE,font = font1)
                ent['bg']=color8
                ent['fg']=color9
                ent.grid(row=z + 1, column=l, sticky=NSEW)
                ent.insert(END, "")
                cols.append(ent)
            rows.append(cols)
        for i in range(max_rows-1) :
            z += 1
            l = -1
            cols = []
            for j in range(max_cols):
                l += 1
                ent = Entry(root,width=20,relief=RIDGE,font = font1)
                ent['bg']=color6
                ent['fg']=color7
                ent.grid(row=z + 1, column=l, sticky=NSEW)
                ent.insert(END, "")
                cols.append(ent)
            rows.append(cols)
    return rows,max_rows,max_cols, max_rows

