from tkinter import *
from Srsave import *
def Srball(srball,gorod,bl4,bl5,bl6,color2,color1,color3,color5,color4,font1,font):
    """
    Функция для создания окна, где показывается средний балл по выбранным предметам\n
    Принимает на вход:\n
                    srball - средний балл по выбранным предметам\n
                    gorod - название города, если имеется\n
                    bl4 - значение флажка (true or false)\n
                    bl5 - значение флажка (true or false)\n
                    bl6 - значение флажка (true or false)\n
    Выполнил Нигметзянов И.И.
    """
    root6 = Toplevel()
    root6['bg'] = color2
    print(srball)
    w, h = root6.winfo_screenwidth(), root6.winfo_screenheight()
    root6.geometry("260x100+{}+{}".format(int(w / 2.3), int(h / 2.3)))
    btn4 = Button(root6, text="Сохранить данные", command = lambda:Srsave(srball,gorod,bl4,bl5,bl6,root6), font = font)
    lab = Label(root6, text = "Средний балл по предметам равен:", font = font1)
    lab1 = Label(root6, text = round(srball,2), font = font1)
    btn4['bg'] = color1
    btn4['activebackground'] = color3
    btn4['fg'] = color5
    btn4['activeforeground'] = color4
    btn4.grid(row=4, columnspan=2)
    lab['bg'] = color2
    lab1['bg'] = color2
    lab.grid(row=1, column=0, sticky=NW)
    lab1.grid(row=2,column=0)
    root6.focus_set()  # принять фокус ввода,
    root6.grab_set()  # запретить доступ к др. окнам, пока открыт диалог
    root6.wait_window()


