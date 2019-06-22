import sys
import os

Path = os.path.abspath(os.curdir)
sys.path.insert(0, Path[:Path.find("Scripts")]+"\\Library")  # Нужно для того, чтобы использовать файлы из др папки
sys.path.insert(0, Path[:Path.find("Scripts")]+"\\Graphics")
from library import *
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from Create import *
from DeleteMember import *
from AddMember import *
from Function import *
from WinFun import *
from tkinter.filedialog import askopenfilename
from LoadData import Load_data
from interface import *


def Change_fields(root, rows, color6, color7, color8, color9, font1):
    """
    Функция для открытия pic файла, а также для вызова фукнции создания базы данных\n
    Принимает значения:\n
                        color6-color9 - цвета\n
                        root - главное окно\n
                        rows - матрица из ссылок на виджеты Entry, куда записаны данные из файла pic\n
    Возвращает:\n
                data - словарь словарей\n
                rows - матрицу из ссылок\n
                max_rows+2 - максимальное значение индекса виджета Entry\n
                max_cols - количество столбцов виджетов Entry\n
                max_rows+2 - количество строк виджетов Entry\n
    Выполнил Сапожников А.А.
    """
    Path = askopenfilename()
    Path = str(Path)
    if Path != "":
        data = Load_data(Path)
    rows, max_rows, max_cols = fields(root, data, rows, color6, color7, color8, color9, font1)
    return data, rows, max_rows+2, max_cols, max_rows+1


def GlobEl(color6, color7, color8, color9, font1):
    """функция нужная для глобальных переменных/n
    Принимает на вход:
                    color6-color9 - цвета
    Выполнил Сапожников А.А"""
    global rows, data, max_rows, max_cols, max_rows1
    rows, data, max_rows, max_cols, max_rows1 = Change_fields(root, data, color6, color7, color8, color9, font1)


def GlobEl2(root, ent1, ent2, root1, color6, color7, color8, color9, font1):
    """функция нужная для глобальных переменных\n
    принимает значения:
                        root - основное окно с базой данных\n
                        ent1 - поле для ввода количества строк\n
                        ent2 - поле для ввода количества столбцом\n
                        root1 - второстепенное окно, где спрашивается какого размера должна быть база данных\n
    Выполнил Нигметзянов И.И"""
    global data, max_rows, max_cols, max_rows1
    data, max_rows, max_cols, max_rows1 = Create(data, root, ent1, ent2, root1, color6, color7, color8, color9, font1)


def GlobEl3(root, ent1, root2, color6, color7, font1):
    """функция нужная для глобальных переменных\n
    принимает значения:\n
                        root - основное окно с базой данных\n
                        ent1 - поле для ввода количества строк, которые вы хотите добавить в имеющуюся базу данных\n
                        root2 - второстепенное окно, где спрашивается сколько строк вы хотите добавить\n
    Выполнил  Сапожников А.А."""
    global data, max_rows, max_cols, max_rows1
    data, max_rows, max_cols, max_rows1 = Add(max_rows, max_cols, root2, data, ent1, root, max_rows1, color6, color7,
                                              font1)


def GlobEl4(root, ent1, ent2, root3):
    """функция нужная для глобальных переменных\n
    принимает значения:\n
                        root - основное окно с базой данных\n
                        ent1 - поле для ввода фамилии\n
                        ent2 - поле для ввода имени\n
                        root3 - второстепенное окно, где спрашивается кого вы хотите удалить\n
    Выполнил Нигметзянов И.И"""
    global data, max_rows, max_cols, max_rows1
    data, max_rows1 = Delete(ent1, ent2, root3, data, max_rows1)


def WinBaza(root, color2, color1, color3, color5, color4, color6, color7, font1, font):
    """Функция для вызова окна создания базы данных\n
    принимает значение:\n
                        root - основное окно с базой данных\n
                        color1-color7 - цвета
    Выполнил Нигметзянов И.И"""
    root1 = Toplevel()
    root1['bg'] = color2
    w, h = root1.winfo_screenwidth(), root1.winfo_screenheight()
    root1.geometry("220x145+{}+{}".format(int(w / 2.3), int(h / 2.3)))
    btn4 = Button(root1, width=6, text="OK",
                  command=lambda: GlobEl2(root, ent1, ent2, root1, color6, color7, color8, color9, font1), font=font)
    btn4['bg'] = color1
    btn4['activebackground'] = color3
    btn4['fg'] = color5
    btn4['activeforeground'] = color4
    ent1 = Entry(root1, relief=RIDGE, font=font1)
    ent2 = Entry(root1, relief=RIDGE, font=font1)
    ent1["bg"] = color6
    ent1["fg"] = color7
    ent2["bg"] = color6
    ent2["fg"] = color7
    label1 = Label(root1, text="Введите количесто строк", font=font1)
    label1['bg'] = color2
    label2 = Label(root1, text="Введите количесто столбцов", font=font1)
    label2['bg'] = color2
    label3 = Label(root1, text="   ")
    label3['bg'] = color2
    label3.grid(row=4)
    btn4.grid(row=5, column=0, sticky=NW)
    label2.grid(row=2, column=0, sticky=NW)
    label1.grid(row=0, column=0, sticky=NW)
    ent1.grid(row=1, column=0, sticky=NW)
    ent2.grid(row=3, column=0, sticky=NW)
    root1.focus_set()  # принять фокус ввода,
    root1.grab_set()  # запретить доступ к др. окнам, пока открыт диалог
    root1.wait_window()


def WinAdd(root, color2, color1, color3, color5, color4, color6, color7, font1, font):
    """функция для вызова окна, где добавляются в базу данных пустые поля для заполнения\n
    принимает значения:\n
                        root - основное окно с базой данных\n
                        color1-color7 - цвета\n
    Выполнил Сапожников А.А."""
    if data:
        root2 = Toplevel()
        root2.title('Добавление пустых полей')
        root2['bg'] = color2
        w, h = root2.winfo_screenwidth(), root2.winfo_screenheight()
        root2.geometry("220x120+{}+{}".format(int(w / 2.3), int(h / 2.3)))
        btn4 = Button(root2, width=6, text="OK", command=lambda: GlobEl3(root, ent1, root2, color6, color7, font1),
                      font=font)
        btn4['bg'] = color1
        btn4['activebackground'] = color3
        btn4['fg'] = color5
        btn4['activeforeground'] = color4
        ent1 = Entry(root2, relief=RIDGE, font=font1)
        ent1["bg"] = color6
        ent1["fg"] = color7
        label1 = Label(root2, text="Введите количество человек\n которых вы хотите добавить", font=font1)
        label1['bg'] = color2
        label2 = Label(root2, text=" ")
        label2['bg'] = color2
        label2.grid(row=4)
        btn4.grid(row=5, column=0, sticky=NW)
        label1.grid(row=0, column=0, sticky=NW)
        ent1.grid(row=1, column=0, sticky=NW)
        root2.focus_set()  # принять фокус ввода,
        root2.grab_set()  # запретить доступ к др. окнам, пока открыт диалог
        root2.wait_window()
    else:
        showinfo(title="Внимание", message="Создайте базу данных")


def WinDel(root, color2, color1, color3, color5, color4, color6, color7, font1, font):
    """функция для вызова окна, где удаляется строка базы данных по имени и фамилии\n
        принимает значения:\n
                            root - основное окно с базой данных\n
                            color1-color7 - цвета
    Выполнил Нигметзянов И.И."""
    if data:
        l = 1
        for i in range(max_rows1):
            if i != 0:
                try:
                    num1 = int(data[i][2].get())
                    num2 = int(data[i][3].get())
                    num3 = int(data[i][4].get())
                    if num1 > 100 or num2 > 100 or num3 > 100 or num1 < 0 or num2 < 0 or num3 < 0:
                        num1 = num1 / 0
                    else:
                        l += 1
                except:
                    showerror("Ошибка", "Проверьте введенные вами значения в строке {}".format(str(data[i][0].get()))+
                              "\nУбедитесь, что у вас в столбцах:\nМатематика, Русский и Физика\nнаписаны цифры в диапазоне от 0 до 100")
        if l == max_rows1:
            root3 = Toplevel()
            root3.title("Удаление человека по имени и фамилии")
            root3['bg'] = color2
            w, h = root3.winfo_screenwidth(), root3.winfo_screenheight()
            root3.geometry("200x145+{}+{}".format(int(w / 2.3), int(h / 2.3)))
            btn4 = Button(root3, width=6, text="OK", command=lambda: GlobEl4(root, ent1, ent2, root3), font=font)
            btn4['bg'] = color1
            btn4['activebackground'] = color3
            btn4['fg'] = color5
            btn4['activeforeground'] = color4
            ent1 = Entry(root3, relief=RIDGE, font=font1)
            ent2 = Entry(root3, relief=RIDGE, font=font1)
            ent1["bg"] = color6
            ent1["fg"] = color7
            ent2["bg"] = color6
            ent2["fg"] = color7
            label1 = Label(root3, text="Введите фамилию человека", font=font1)
            label1['bg'] = color2
            label2 = Label(root3, text="Введите имя человека", font=font1)
            label2['bg'] = color2
            label3 = Label(root3, text="          ")
            label3['bg'] = color2
            btn4.grid(row=5, column=0, sticky=NW)
            label3.grid(row=4)
            label2.grid(row=2, column=0, sticky=NW)
            label1.grid(row=0, column=0, sticky=NW)
            ent1.grid(row=1, column=0, sticky=NW)
            ent2.grid(row=3, column=0, sticky=NW)
            root3.focus_set()  # принять фокус ввода,
            root3.grab_set()  # запретить доступ к др. окнам, пока открыт диалог
            root3.wait_window()

    else:
        showinfo(title="Внимание", message="Удалять нечего")


"""
Создание основного окна
"""

font, font1, color1, color2, color3, color4, color5, color6, color7, color8, color9 = interface()
max_rows1 = 0
max_rows = 0
max_cols = 0
data = None
rows = None
root = Tk()
root.title('База данных баллов ЕГЭ по городам и различным предметам')
root["bg"] = color2
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("1000x700")
btn = Button(width=17, text="Открыть файл", command=lambda: GlobEl(color6, color7, color8, color9, font1), font=font)
btn1 = Button(width=17, text="Сохранить", command=lambda: Save(data, max_cols, max_rows1), font=font)
btn2 = Button(width=17, text="Создать", command=lambda: WinBaza(root, color2, color1, color3, color5, color4,
                                                                color6, color7, font1, font), font=font)
btn3 = Button(width=17, text="Добавить человека", command=lambda: WinAdd(root, color2, color1, color3, color5, color4,
                                                                         color6, color7, font1, font), font=font)
btn4 = Button(width=17, text="Удалить человека", command=lambda: WinDel(root, color2, color1, color3, color5,
                                                                        color4, color6, color7, font1, font), font=font)
btn5 = Button(width=17, text="Доп. функции",
              command=lambda: WinFun(data, max_rows1, rows, color6, color7, color8, color9,
                                     color2, color1, color3, color5, color4, font1, font), font=font)
btn['bg'] = color1
btn['activebackground'] = color3
btn['fg'] = color5
btn['activeforeground'] = color4
btn1['bg'] = color1
btn1['activebackground'] = color3
btn1['fg'] = color5
btn1['activeforeground'] = color4
btn2['bg'] = color1
btn2['activebackground'] = color3
btn2['fg'] = color5
btn2['activeforeground'] = color4
btn3['bg'] = color1
btn3['activebackground'] = color3
btn3['fg'] = color5
btn3['activeforeground'] = color4
btn4['bg'] = color1
btn4['activebackground'] = color3
btn4['fg'] = color5
btn4['activeforeground'] = color4
btn5['bg'] = color1
btn5['activebackground'] = color3
btn5['fg'] = color5
btn5['activeforeground'] = color4
btn.grid(row=0, column=0, sticky=NW)
btn1.grid(row=0, column=1, sticky=NW)
btn2.grid(row=0, column=2, sticky=NW)
btn3.grid(row=0, column=3, sticky=NW)
btn4.grid(row=0, column=4, sticky=NW)
btn5.grid(row=0, column=5, sticky=NW)
root.mainloop()
