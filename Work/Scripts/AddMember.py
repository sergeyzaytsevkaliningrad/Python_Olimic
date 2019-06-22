from tkinter import *
def Add(max_rows,max_cols,root2,data,ent1,root,max_rows1,color6,color7,font1):
    """
    Функция для добавления пустой строки для заполнения\n
    Принимает:\n
            max_rows - максимальный индекс виджета Entry\n
            max_cols - количество столбцов\n
            root2 - название второстепенного окна, где спрашивается о количестве строк\n
            data - матрица ссылок на виджета Entry\n
            ent1 - название виджета Entry откуда считывается количество строк\n
            root - название главного окна\n
            max_rows1 - максимальное значение индекса у виджета Entry\n
    возвращает:\n
            data - измененную матрицу ссылок на виджеты\n
            max_rows+number - измененное макс значение индекса у виджета\n
            max_cols - количество столбцов\n
            max_rows1+number - измененное количество строк матрицы из виджетов Entry\n
    Выполнил Сапожников А.А.
    """
    number = int(ent1.get())
    root2.destroy()  # изменит на quit
    for i in range(number):
        cols = []
        for j in range(max_cols):
            ent = Entry(root, relief=RIDGE,font = font1)
            ent['bg'] = color6
            ent['fg'] = color7
            ent.grid(row=i+max_rows, column=j, sticky=NSEW)
            ent.insert(END, "")
            cols.append(ent)
        data.append(cols)
    max_rows1 = max_rows1+number
    max_rows = max_rows+number
    return data, max_rows, max_cols, max_rows1
