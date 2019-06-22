from tkinter import *
from SaveHuman import *
def Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font):
    """
    Функция для создания окна, где выводятся люди подходящие под критерии\n
    Принимает на вход:\n
                    rows - словарь словарей\n
                    ndata - массив из индексов подходящих людей\n
    Выполнил Нигметзянов И.И.
    """
    z=1
    root5 = Toplevel()
    root5["bg"] = color2
    w, h = root5.winfo_screenwidth(), root5.winfo_screenheight()
    root5.geometry("1000x720")
    data = []
    l = -1
    cols = []
    for i in rows:
        k = i
    for j in rows[k]:
        l += 1
        ent = Entry(root5,relief=RIDGE, font = font1)
        ent["bg"] = color8
        ent["fg"] = color9
        ent.grid(row=z, column=l, sticky=NSEW)
        ent.insert(END, j)
        cols.append(ent)
    data.append(cols)
    for i in rows:
        z+=1
        l=-1
        cols = []
        for f in ndata:
            if f == z-1:
                for j in rows[i]:
                    l+=1
                    ent = Entry(root5, relief=RIDGE, font = font1)
                    ent["bg"] = color6
                    ent["fg"] = color7
                    ent.grid(row=z+1, column=l, sticky=NSEW)
                    ent.insert(END, rows[i][j])
                    cols.append(ent)
        data.append(cols)
    btn = Button(root5,text = "Сохранить",command= lambda : SaveHuman(data,ndata,root5), font = font)
    btn['bg'] = color1
    btn['activebackground'] = color3
    btn['fg'] = color5
    btn['activeforeground'] = color4
    btn.grid(row=0,sticky=NSEW)
    root5.focus_set()  # принять фокус ввода,
    root5.grab_set()  # запретить доступ к др. окнам, пока открыт диалог
    root5.wait_window()
