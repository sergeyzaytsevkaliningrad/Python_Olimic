from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from tkinter.filedialog import asksaveasfilename
import pickle as pk



def fields(root,data,rows,color6,color7,color8,color9,font1):
    """
        Функция создания базы данных на основе файла pic\n
        Принимает 3 значения:\n
                            root - главное окно\n
                            rows - матрица из ссылок на виджеты Entry, куда записаны данные из файла pic\n
                            data - словарь словарей\n
        Возвращает:\n
                    rows - матрицу из ссылок\n
        Выполнил Сапожников А.А.
    """
    z=0
    if rows:
        for lst in rows:
            for ent in lst:
                ent.destroy()
        for lst in rows:
            del rows[0]
    rows = []
    max_rows = len(data) # надо будет посчитать из файла
    if max_rows:
        l=-1
        cols = []
        for i in data:
            k = i
        for j in data[k]:
            l+=1
            ent = Entry(root,width=17,relief=RIDGE,font = font1)
            ent.grid(row=z+1, column=l, sticky=NSEW)
            ent["bg"] = color8
            ent["fg"] = color9
            ent.insert(END, j)
            cols.append(ent)
        rows.append(cols)
        max_cols = l+1
        print(data)
        for i in data:
            z+=1
            l=-1
            cols = []
            for j in data[i]:
                l+=1
                ent = Entry(root,width=17, relief=RIDGE, font = font1)
                ent.grid(row=z+1, column=l, sticky=NSEW)
                ent["bg"] = color6
                ent["fg"] = color7
                ent.insert(END, data[i][j])
                cols.append(ent)
            rows.append(cols)
    return rows,max_rows,max_cols


def Save(data,max_cols,max_rows1):
    """
        Функция сохранения базы данных на основе файла pic\n
        Принимает 3 значения:\n
                            data - словарь ссылок на виджеты Entry\n
                            max_cols - количество столбцов в базе данных\n
                            max_rows1 - количество строк виджетов Entry\n
        Выполнил Нигметзянов И.И
    """
    key = []
    key1 = []
    par1 = []
    if data:
        l = 1
        for i in range(max_rows1):
            if i != 0:
                try:
                    num1 = int(data[i][2].get())
                    num2 = int(data[i][3].get())
                    num3 = int(data[i][4].get())
                    if num1>100 or num2>100 or num3>100 or num1<0 or num2<0 or num3<0:
                        num1=num1/0
                    else:
                        l += 1
                except:
                    showerror("Ошибка", "Проверьте введенные вами значения в строке {}".format(str(data[i][0].get())) +
                              "\nУбедитесь, что у вас в столбцах:\nМатематика, Русский и Физика\nнаписаны цифры в диапазоне от 0 до 100")
        if l == max_rows1:
            for i in range(max_rows1):
                if i != 0:
                    key.append(data[i][0].get())
            for i in range (1):
                for j in range(max_cols):
                    key1.append(data[i][j].get())
            for i in range(max_rows1):
                par = []
                if i!=0:
                    for j in range(max_cols):
                        par.append(data[i][j].get())
                    par1.append(par)
            w2 = [dict(zip(key1,x)) for x in par1]
            w3 = dict(zip(key,w2))
            file_name = asksaveasfilename()
            file_name = str(file_name)
            fn = open(file_name, 'wb')
            pk.dump(w3, fn)
    else:
        showinfo(title="Внимание", message="База данных нет")


