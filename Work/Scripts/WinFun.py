from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from Function import *

def maincheck(ent1):
    """
    Функция нужная для того, чтобы либо создать или спрятать виджет Entry в зависимости от условия\n
    Получает на вход параметр ent1 это название виджета Entry\n
    Выполнил Сапожников А.А.
    """
    if bl or bl1 or bl2:
        ent1.grid(row=2, column=1,sticky=NSEW)
    else:
        ent1.grid_remove()

def checked(ent1):
    """
    Функция нужная для показания состояния флажка\n
    Получает на вход ent1 это название виджета Entry\n
    Выполнил Сапожников А.А.
    """
    global bl
    bl = not bl
    maincheck(ent1)

def checked1(ent1):
    """
    Функция нужная для показания состояния флажка\n
    Получает на вход ent1 это название виджета Entry\n
    Выполнил Сапожников А.А.
    """
    global bl1
    bl1 = not bl1
    maincheck(ent1)

def checked2(ent1):
    """
    Функция нужная для показания состояния флажка\n
    Получает на вход ent1 это название виджета Entry\n
    Выполнил Сапожников А.А.
    """
    global bl2
    bl2 = not bl2
    maincheck(ent1)

def checked3(ent4):
    """
    Функция нужная для показания состояния флажка, а также для создания или скрывания виджета\n
    Получает на вход ent4 это название виджета Entry\n
    Выполнил Сапожников А.А.
    """
    global bl3
    bl3 = not bl3
    if bl3:
        ent4.grid(row=5, column = 1,sticky=NSEW)
    else:
        ent4.grid_remove()

def checked4():
    """
    Функция нужная для показания состояния флажка\n
    Выполнил Нигметзянов И.И.
    """
    global bl4
    bl4 = not bl4


def checked5():
    """
    Функция нужная для показания состояния флажка\n
    Выполнил Нигметзянов И.И.
    """
    global bl5
    bl5 = not bl5

def checked6():
    """
    Функция нужная для показания состояния флажка\n
    Выполнил Нигметзянов И.И.
    """
    global bl6
    bl6 = not bl6

def checked7(ent5):
    """
    Функция нужная для показания состояния флажка, а также для создания или скрывания виджета\n
    Получает на вход ent5 это название виджета Entry\n
    Выполнил Нигметзянов И.И.
    """
    global bl7
    bl7 = not bl7
    if bl7:
        ent5.grid(row=11, column = 1,sticky=NSEW)
    else:
        ent5.grid_remove()

def WinFun(data,max_rows1,rows,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font):
    """
    Функция для создания окна, где выбирается то, что мы хотим увидеть на основе полученных данных\n
    Принимает на вход:\n
    data - матрица ссылок виджетов Entry\n
    max_rows1 - количество строк в базе данных\n
    rows - словарь словарей\n
    Выполнил Сапожников А.А. и Нигметзянов И.И.
    """
    if data or rows:
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
                    showerror("Ошибка", "Проверьте введенные вами значения в строке {}".format(str(data[i][0].get())) +
                              "\nУбедитесь, что у вас в столбцах:\nМатематика, Русский и Физика\nнаписаны цифры в диапазоне от 0 до 100")
        if l == max_rows1:
            root4 = Toplevel()
            root4["bg"] = color2
            w, h = root4.winfo_screenwidth(), root4.winfo_screenheight()
            root4.geometry("233x350+{}+{}".format(int(w / 2.3), int(h / 2.3)))
            ent1 = Entry(root4, width=10, font = font1)
            ent4 = Entry(root4, width=10, font = font1)
            ent5 = Entry(root4, width=10, font = font1)
            label = Label(root4, text = "Вывод людей по критериям:", font = font1)
            label.grid(row=1, columnspan =2)
            check = Checkbutton(root4 ,text="Математика", command = lambda:checked(ent1), font = font1)
            check.grid(row=2, column=0,sticky=W)
            check1 = Checkbutton(root4, text="Русский", command=lambda:checked1(ent1), font = font1)
            check1.grid(row=3, column=0, sticky=W)
            check2 = Checkbutton(root4, text="Физика", command=lambda:checked2(ent1), font = font1)
            check2.grid(row=4, column=0, sticky=W)
            check3 = Checkbutton(root4, text="Город", command=lambda:checked3(ent4), font = font1)
            check3.grid(row=5, column=0, sticky=W)
            btn1 = Button(root4, text="Показать", command = lambda:Output(bl,bl1,bl2,bl3,ent1,ent4,data,max_rows1-1,rows,color2,color1,color3,
                                                                          color5,color4,color6,color7,color8,color9,font1,font), font = font)
            btn1.grid(row=6, columnspan=2)
            label2 = Label(root4, text="  Выберите предмет по которому\nхотите вывести средний балл", font = font1)
            label2.grid(row=7, columnspan=2)
            check4 = Checkbutton(root4, text="Физика", command=lambda: checked4(), font = font1)
            check4.grid(row=8, columnspan=2, sticky=W)
            check5 = Checkbutton(root4, text="Математика", command=lambda: checked5(), font = font1)
            check5.grid(row=9, columnspan=2, sticky=W)
            check6 = Checkbutton(root4, text="Русский", command=lambda: checked6(), font = font1)
            check6.grid(row=10, columnspan=2, sticky=W)
            check7 = Checkbutton(root4, text="Город", command=lambda: checked7(ent5), font = font1)
            check7.grid(row=11, columnspan=2, sticky=W)
            btn2 = Button(root4, text="Показать", command = lambda: SumSr(bl4,bl5,bl6,bl7,max_rows1-1,data,ent5,color2,color1,
                                                                          color3,color5,color4,font1,font), font = font)
            btn2.grid(row=12, columnspan=2)
            btn1['bg'] = color1
            btn1['activebackground'] = color3
            btn1['fg'] = color5
            btn1['activeforeground'] = color4
            btn2['bg'] = color1
            btn2['activebackground'] = color3
            btn2['fg'] = color5
            btn2['activeforeground'] = color4
            ent1["bg"] = color6
            ent1["fg"] = color7
            ent4["bg"] = color6
            ent4["fg"] = color7
            ent5["bg"] = color6
            ent5["fg"] = color7
            check["bg"] = color2
            check1["bg"] = color2
            check2["bg"] = color2
            check3["bg"] = color2
            check4["bg"] = color2
            check5["bg"] = color2
            check6["bg"] = color2
            check7["bg"] = color2
            label["bg"] = color2
            label2["bg"] = color2
            root4.focus_set()  # принять фокус ввода,
            root4.grab_set()  # запретить доступ к др. окнам, пока открыт диалог
            root4.wait_window()
    else:
        showinfo(title="Внимание", message="Создайте базу данных")


bl = False
bl1 = False
bl2 = False
bl3 = False
bl4 = False
bl5 = False
bl6 = False
bl7 = False
