from Srball import *
from Output import *
from tkinter.messagebox import showerror

def SumSr(bl4,bl5,bl6,bl7,max_rows1,data,ent5,color2,color1,color3,color5,color4,font1,font):
    """
    Функция для понимания того, какие флажки нажаты, а какие нет\n
    принимает на вход:\n
                    bl4 - значение флажка (true or false)\n
                    bl5 - значение флажка (true or false)\n
                    bl6 - значение флажка (true or false)\n
                    bl7 - значение флажка (true or false)\n
                    max_rows1 - количество строк в матрице ссылок\n
                    data - матрица ссылок\n
                    ent5 - поле ввода города\n
    Выполнил Сапожников А.А. и Нигметзянов И.И.
    """
    gorod = str(ent5.get())
    if bl4 and bl5 and bl6 and bl7:
        l = 0
        srball = 0
        for i in range(max_rows1):
            if i != 0:
                math = int(data[i][2].get())
                rus = int(data[i][3].get())
                fiz = int(data[i][4].get())
                gorod1 = str(data[i][5].get())
                if gorod == gorod1:
                    srball += math+rus+fiz
                    l += 1
        srball = srball/(3*l)
        Srball(srball,gorod,bl4,bl5,bl6,color2,color1,color3,color5,color4,font1,font)
    elif bl4 and bl5 and bl7:
        l = 0
        srball = 0
        for i in range(max_rows1):
            if i != 0:
                fiz = int(data[i][4].get())
                math = int(data[i][2].get())
                gorod1 = str(data[i][5].get())
                if gorod == gorod1:
                    srball += math+fiz
                    l += 1
        srball = srball /(2*l)
        Srball(srball, gorod, bl4, bl5, bl6,color2,color1,color3,color5,color4,font1,font)
    elif bl4 and bl6 and bl7:
        l = 0
        srball = 0
        for i in range(max_rows1):
            if i != 0:
                rus = int(data[i][3].get())
                fiz = int(data[i][4].get())
                gorod1 = str(data[i][5].get())
                if gorod == gorod1:
                    srball += rus+fiz
                    l += 1
        srball = srball/(2*l)
        Srball(srball, gorod, bl4, bl5, bl6,color2,color1,color3,color5,color4,font1,font)
    elif bl5 and bl6 and bl7:
        l = 0
        srball = 0
        for i in range(max_rows1):
            if i != 0:
                rus = int(data[i][3].get())
                math = int(data[i][2].get())
                gorod1 = str(data[i][5].get())
                if gorod == gorod1:
                    srball +=rus+math
                    l+=1
        srball = srball / (2*l)
        Srball(srball, gorod, bl4, bl5, bl6,color2,color1,color3,color5,color4,font1,font)
    elif bl4 and bl5 and bl6:
        srball = 0
        for i in range(max_rows1):
            if i != 0:
                rus = int(data[i][3].get())
                math = int(data[i][2].get())
                fiz = int(data[i][4].get())
                srball += rus + math + fiz
        srball = srball /(3*max_rows1)
        Srball(srball, gorod, bl4, bl5, bl6,color2,color1,color3,color5,color4,font1,font)
    elif bl5 and bl6:
        srball = 0
        for i in range(max_rows1):
            if i != 0:
                rus = int(data[i][3].get())
                math = int(data[i][2].get())
                srball += rus + math
        srball = srball / (2*max_rows1)
        Srball(srball, gorod, bl4, bl5, bl6,color2,color1,color3,color5,color4,font1,font)
    elif bl4 and bl6:
        srball = 0
        for i in range(max_rows1):
            if i != 0:
                fiz = int(data[i][4].get())
                rus = int(data[i][3].get())
                srball += rus + fiz
        srball = srball / (2*max_rows1)
        Srball(srball, gorod, bl4, bl5, bl6,color2,color1,color3,color5,color4,font1,font)
    elif bl5 and bl4:
        srball = 0
        for i in range(max_rows1):
            if i != 0:
                fiz = int(data[i][4].get())
                math = int(data[i][2].get())
                srball += fiz + math
        srball = srball / (2*max_rows1)
        Srball(srball, gorod, bl4, bl5, bl6,color2,color1,color3,color5,color4,font1,font)

    elif bl6 and bl7:
        num = 0
        srball = 0
        for i in range(max_rows1):
            if i != 0:
                rus = int(data[i][3].get())
                gorod1 = str(data[i][5].get())
                if gorod == gorod1:
                    num += 1
                    srball += rus
        srball = srball / num
        Srball(srball, gorod, bl4, bl5, bl6,color2,color1,color3,color5,color4,font1,font)
    elif bl4 and bl7:
        num = 0
        num = 0
        srball = 0
        for i in range(max_rows1):
            if i != 0:
                fiz = int(data[i][4].get())
                gorod1 = str(data[i][5].get())
                if gorod == gorod1:
                    num += 1
                    srball += fiz
        srball = srball / num
        Srball(srball, gorod, bl4, bl5, bl6,color2,color1,color3,color5,color4,font1,font)
    elif bl5 and bl7:
        num = 0
        srball = 0
        for i in range(max_rows1):
            if i != 0:
                math = int(data[i][2].get())
                gorod1 = str(data[i][5].get())
                if gorod == gorod1:
                    num += 1
                    srball += math
        srball = srball / num
        Srball(srball, gorod, bl4, bl5, bl6,color2,color1,color3,color5,color4,font1,font)
    elif bl5:
        srball = 0
        for i in range(max_rows1):
            if i != 0:
                math = int(data[i][2].get())
                srball += math
        srball = srball / max_rows1
        Srball(srball, gorod, bl4, bl5, bl6,color2,color1,color3,color5,color4,font1,font)
    elif bl6:
        srball = 0
        for i in range(max_rows1):
            if i != 0:
                rus = int(data[i][3].get())
                srball += rus
        srball = srball / max_rows1
        Srball(srball, gorod, bl4, bl5, bl6,color2,color1,color3,color5,color4,font1,font)
    elif bl4:
        srball = 0
        for i in range(max_rows1):
            if i != 0:
                fiz = int(data[i][4].get())
                srball += fiz
        srball = srball / max_rows1
        Srball(srball, gorod, bl4, bl5, bl6,color2,color1,color3,color5,color4,font1,font)

def Output(bl,bl1,bl2,bl3,ent1,ent4,data,max_rows1,rows,color2,color1,color3,color5,color4,color6,color7,color8,color9,font1,font):
    """
    Функция для понимания того, какие флажки нажаты, а какие нет\n
    принимает на вход:\n
                        bl - значение флажка (true or false)\n
                        bl1 - значение флажка (true or false)\n
                        bl2 - значение флажка (true or false)\n
                        bl3 - значение флажка (true or false)\n
                        max_rows1 - количество строк в матрице ссылок\n
                        data - матрица ссылок\n
                        ent1 - поле ввода условия\n
                        ent4 - поле ввода города\n
                        rows - словарь словарей\n
    Выполнил Сапожников А.А. и Нигметзянов И.И.
    """
    get = str(ent1.get())
    gorod = str(ent4.get())
    num = 0
    ind=0
    num1 = 0
    ndata = []
    lend = len(get)
    boolean = True
    boolean1 = True
    check = True
    i=-1
    while boolean and i+1!=lend:
        i+=1
        if lend > 3:
            if (get[0] == "x" and get[1] == "="):
                if i!=0 and i!=1:
                    try:
                        num = int(get[i])
                        boolean = True
                    except:
                        boolean = False
                        showerror("Ошибка", "Проверьте введенные вами значения в вверхнем поле для ввода")
            elif (get[0] == "x" and (get[1] == "<" or get[1] == ">") and get[2]=="="):
                if i!=0 and i!=1 and i!=2:
                    try:
                        num = int(get[i])
                        boolean = True
                    except:
                        boolean = False
                        showerror("Ошибка", "Проверьте введенные вами значения в вверхнем поле для ввода")
            elif boolean:
                try:
                    num += int(get[i])
                    boolean = True
                except:
                    if get[i]=="<" and get[i+1]=="=" and get[i+2]=="x" and get[i+3]=="<" and get[i+4]=="=":
                        i = lend-1
                    else:
                        boolean = False
                        showerror("Ошибка", "Проверьте введенные вами значения в вверхнем поле для ввода")
        else:
            boolean = False
            showerror("Ошибка", "Проверьте введенные вами значения в вверхнем поле для ввода")
    if boolean:
        num=0
        num1=0
        for i in range(lend):
            if (get[1] == "=" and get[0] == "x"):
                if i != 0 and i!=1:
                    num += int(get[i])
                    if i != (lend - 1):
                        num *= 10
                        boolean1 = False
            elif((get[1] == "<" or get[1] == ">") and get[2]=="=" and get[0]=="x"):
                if i != 0 and i != 1 and i != 2:
                    num += int(get[i])
                    if i != (lend - 1):
                        num *= 10
                        boolean1 = False
        i=-1
        while boolean1 and i+1!=lend:
            i+=1
            try:
                    num += int(get[i])
                    num3 = int(get[i + 1])
                    num *= 10
            except:
                ind = i+1
                try:
                    num1 = int(get[i + 6:])
                    check = True
                except:
                    showerror("Ошибка", "Проверьте введенные вами значения в вверхнем поле для ввода")
                    check = False
                boolean1 = False
        if check:
            if bl and bl1 and bl2 and bl3:
                if get[1]=="<" and get[2]=="=":
                    for i in range(max_rows1):
                        if i!=0:
                            math = int(data[i][2].get())
                            rus = int(data[i][3].get())
                            fiz = int(data[i][4].get())
                            gorod1 = str(data[i][5].get())
                            if math <= num and rus <= num and fiz <= num and gorod1 == gorod:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)

                elif get[1]==">" and get[2]=="=":
                    for i in range(max_rows1):
                        if i!=0:
                            math = int(data[i][2].get())
                            rus = int(data[i][3].get())
                            fiz = int(data[i][4].get())
                            gorod1 = str(data[i][5].get())
                            if math >= num and rus >= num and fiz >= num and gorod1 == gorod:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[1]=="=":
                    for i in range(max_rows1):
                        if i!=0:
                            math = int(data[i][2].get())
                            rus = int(data[i][3].get())
                            fiz = int(data[i][4].get())
                            gorod1 = str(data[i][5].get())
                            if math == num and rus == num and fiz == num and gorod1 == gorod:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[ind] == "<" and get[ind + 1] == "=" and get[ind + 2] == "x" and get[ind + 3] == "<" and get[ind + 4] == "=":
                    for i in range(max_rows1):
                        if i!=0:
                            math = int(data[i][2].get())
                            rus = int(data[i][3].get())
                            fiz = int(data[i][4].get())
                            gorod1 = str(data[i][5].get())
                            if math >= num and rus >= num and fiz >= num and gorod1 == gorod and  math <= num1 and rus <= num1 and fiz <= num1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows, ndata, color6, color7, color8, color9, color2, color1, color3, color5, color4, font1,
                               font)

            elif bl and bl1 and bl3:
                if get[1] == "<" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            rus = int(data[i][3].get())
                            gorod1 = str(data[i][5].get())
                            if math <= num and rus <= num and gorod1 == gorod:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)

                elif get[1] == ">" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            rus = int(data[i][3].get())
                            gorod1 = str(data[i][5].get())
                            if math >= num and rus >= num and gorod1 == gorod:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[1] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            rus = int(data[i][3].get())
                            gorod1 = str(data[i][5].get())
                            if math == num and rus == num and gorod1 == gorod:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[ind] == "<" and get[ind + 1] == "=" and get[ind + 2] == "x" and get[ind + 3] == "<" and get[ind + 4] == "=":
                    for i in range(max_rows1):
                        if i!=0:
                            math = int(data[i][2].get())
                            rus = int(data[i][3].get())
                            gorod1 = str(data[i][5].get())
                            if math >= num and rus >= num and gorod1 == gorod and  math <= num1 and rus <= num1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows, ndata, color6, color7, color8, color9, color2, color1, color3, color5, color4, font1,
                               font)
            elif bl and bl2 and bl3:
                if get[1] == "<" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            fiz = int(data[i][4].get())
                            gorod1 = str(data[i][5].get())
                            if math <= num and fiz <= num and gorod1 == gorod:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[1] == ">" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            fiz = int(data[i][4].get())
                            gorod1 = str(data[i][5].get())
                            if math >= num and fiz >= num and gorod1 == gorod:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[1] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            fiz = int(data[i][4].get())
                            gorod1 = str(data[i][5].get())
                            if math == num and fiz == num and gorod1 == gorod:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[ind] == "<" and get[ind + 1] == "=" and get[ind + 2] == "x" and get[ind + 3] == "<" and get[ind + 4] == "=":
                    for i in range(max_rows1):
                        if i!=0:
                            math = int(data[i][2].get())
                            fiz = int(data[i][4].get())
                            gorod1 = str(data[i][5].get())
                            if math >= num and fiz >= num and gorod1 == gorod and  math <= num and fiz <= num1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows, ndata, color6, color7, color8, color9, color2, color1, color3, color5, color4, font1,
                               font)
            elif bl1 and bl2 and bl3:
                if get[1] == "<" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            rus = int(data[i][3].get())
                            fiz = int(data[i][4].get())
                            gorod1 = str(data[i][5].get())
                            if rus <= num and fiz <= num and gorod1 == gorod:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)

                elif get[1] == ">" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            rus = int(data[i][3].get())
                            fiz = int(data[i][4].get())
                            gorod1 = str(data[i][5].get())
                            if rus >= num and fiz >= num and gorod1 == gorod:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[1] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            rus = int(data[i][3].get())
                            fiz = int(data[i][4].get())
                            gorod1 = str(data[i][5].get())
                            if rus >= num and fiz >= num and gorod1 == gorod:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[ind] == "<" and get[ind + 1] == "=" and get[ind + 2] == "x" and get[ind + 3] == "<" and get[ind + 4] == "=":
                    for i in range(max_rows1):
                        if i!=0:
                            rus = int(data[i][3].get())
                            fiz = int(data[i][4].get())
                            gorod1 = str(data[i][5].get())
                            if  rus >= num and fiz >= num and gorod1 == gorod and rus <= num1 and fiz <= num1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows, ndata, color6, color7, color8, color9, color2, color1, color3, color5, color4, font1,
                               font)
            elif bl and bl1 and bl2:
                if get[1] == "<" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            rus = int(data[i][3].get())
                            fiz = int(data[i][4].get())
                            if math <= num and rus <= num and fiz <= num:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)

                elif get[1] == ">" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            rus = int(data[i][3].get())
                            fiz = int(data[i][4].get())
                            if math >= num and rus >= num and fiz >= num:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)

                elif get[1] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            rus = int(data[i][3].get())
                            fiz = int(data[i][4].get())
                            if math == num and rus == num and fiz == num:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[ind] == "<" and get[ind + 1] == "=" and get[ind + 2] == "x" and get[ind + 3] == "<" and get[ind + 4] == "=":
                    for i in range(max_rows1):
                        if i!=0:
                            math = int(data[i][2].get())
                            rus = int(data[i][3].get())
                            fiz = int(data[i][4].get())
                            if math >= num and rus >= num and fiz >= num and  math <= num1 and rus <= num1 and fiz <= num1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows, ndata, color6, color7, color8, color9, color2, color1, color3, color5, color4, font1,
                               font)
            elif bl and bl1:
                if get[1] == "<" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            rus = int(data[i][3].get())
                            if math <= num and rus <= num:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)

                elif get[1] == ">" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            rus = int(data[i][3].get())
                            if math >= num and rus >= num:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)


                elif get[1] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            rus = int(data[i][3].get())
                            if math == num and rus == num:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[ind] == "<" and get[ind + 1] == "=" and get[ind + 2] == "x" and get[ind + 3] == "<" and get[ind + 4] == "=":
                    for i in range(max_rows1):
                        if i!=0:
                            math = int(data[i][2].get())
                            rus = int(data[i][3].get())
                            if math >= num and rus >= num and  math <= num1 and rus <= num1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows, ndata, color6, color7, color8, color9, color2, color1, color3, color5, color4, font1,
                               font)
            elif bl and bl2:
                if get[1] == "<" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            fiz = int(data[i][4].get())
                            if math <= num and fiz <= num:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)

                elif get[1] == ">" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            fiz = int(data[i][4].get())
                            if math >= num and fiz >= num:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)


                elif get[1] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            fiz = int(data[i][4].get())
                            if math == num and fiz == num:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[ind] == "<" and get[ind + 1] == "=" and get[ind + 2] == "x" and get[ind + 3] == "<" and get[ind + 4] == "=":
                    for i in range(max_rows1):
                        if i!=0:
                            math = int(data[i][2].get())
                            fiz = int(data[i][4].get())
                            if math >= num and fiz >= num and  math <= num1 and fiz <= num1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows, ndata, color6, color7, color8, color9, color2, color1, color3, color5, color4, font1,
                               font)
            elif bl and bl3:
                if get[1] == "<" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            gorod1 = str(data[i][5].get())
                            if math <= num and gorod == gorod1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)

                elif get[1] == ">" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            gorod1 = str(data[i][5].get())
                            if math >= num and gorod == gorod1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)


                elif get[1] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            gorod1 = str(data[i][5].get())
                            if math == num and gorod == gorod1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[ind] == "<" and get[ind + 1] == "=" and get[ind + 2] == "x" and get[ind + 3] == "<" and get[ind + 4] == "=":
                    for i in range(max_rows1):
                        if i!=0:
                            math = int(data[i][2].get())
                            gorod1 = str(data[i][5].get())
                            if math >= num and gorod1 == gorod and  math <= num1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows, ndata, color6, color7, color8, color9, color2, color1, color3, color5, color4, font1,
                               font)
            elif bl1 and bl3:
                if get[1] == "<" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            rus = int(data[i][3].get())
                            gorod1 = str(data[i][5].get())
                            if rus <= num and gorod == gorod1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)

                elif get[1] == ">" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            rus = int(data[i][3].get())
                            gorod1 = str(data[i][5].get())
                            if rus >= num and gorod == gorod1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)


                elif get[1] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            rus = int(data[i][3].get())
                            gorod1 = str(data[i][5].get())
                            if rus == num and gorod == gorod1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[ind] == "<" and get[ind + 1] == "=" and get[ind + 2] == "x" and get[ind + 3] == "<" and get[ind + 4] == "=":
                    for i in range(max_rows1):
                        if i!=0:
                            rus = int(data[i][3].get())
                            gorod1 = str(data[i][5].get())
                            if rus >= num and gorod1 == gorod and rus <= num1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows, ndata, color6, color7, color8, color9, color2, color1, color3, color5, color4, font1,
                               font)
            elif bl2 and bl3:
                if get[1] == "<" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            fiz = int(data[i][4].get())
                            gorod1 = str(data[i][5].get())
                            if fiz <= num and gorod == gorod1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)

                elif get[1] == ">" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            fiz = int(data[i][4].get())
                            gorod1 = str(data[i][5].get())
                            if fiz >= num and gorod == gorod1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)


                elif get[1] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            fiz = int(data[i][4].get())
                            gorod1 = str(data[i][5].get())
                            if fiz == num and gorod == gorod1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[ind] == "<" and get[ind + 1] == "=" and get[ind + 2] == "x" and get[ind + 3] == "<" and get[ind + 4] == "=":
                    for i in range(max_rows1):
                        if i!=0:
                            fiz = int(data[i][4].get())
                            gorod1 = str(data[i][5].get())
                            if fiz >= num and gorod1 == gorod and fiz <= num1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows, ndata, color6, color7, color8, color9, color2, color1, color3, color5, color4, font1,
                               font)
            elif bl:
                if get[1] == "<" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            if math <= num:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[1] == ">" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            if math >= num:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)

                elif get[1] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            math = int(data[i][2].get())
                            if math == num:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[ind] == "<" and get[ind + 1] == "=" and get[ind + 2] == "x" and get[ind + 3] == "<" and get[ind + 4] == "=":
                    for i in range(max_rows1):
                        if i!=0:
                            math = int(data[i][2].get())
                            if math >= num and math <= num1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows, ndata, color6, color7, color8, color9, color2, color1, color3, color5, color4, font1,
                               font)
            elif bl1:
                if get[1] == "<" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            rus = int(data[i][3].get())
                            if rus <= num:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)


                elif get[1] == ">" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            rus = int(data[i][3].get())
                            if rus >= num:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)

                elif get[1] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            rus = int(data[i][3].get())
                            if rus == num:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[ind] == "<" and get[ind + 1] == "=" and get[ind + 2] == "x" and get[ind + 3] == "<" and get[ind + 4] == "=":
                    for i in range(max_rows1):
                        if i!=0:
                            rus = int(data[i][3].get())
                            if rus >= num and rus <= num1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows, ndata, color6, color7, color8, color9, color2, color1, color3, color5, color4, font1,
                               font)
            elif bl2:
                if get[1] == "<" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            fiz = int(data[i][4].get())
                            if fiz <= num:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)

                elif get[1] == ">" and get[2] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            fiz = int(data[i][4].get())
                            if fiz >= num:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)


                elif get[1] == "=":
                    for i in range(max_rows1):
                        if i != 0:
                            fiz = int(data[i][4].get())
                            if fiz == num:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)
                elif get[ind] == "<" and get[ind + 1] == "=" and get[ind + 2] == "x" and get[ind + 3] == "<" and get[ind + 4] == "=":
                    for i in range(max_rows1):
                        if i!=0:
                            fiz = int(data[i][4].get())
                            if fiz >= num and fiz <= num1:
                                print(str(data[i][0].get()))
                                ndata.append(i)
                    Add_fields(rows, ndata, color6, color7, color8, color9, color2, color1, color3, color5, color4, font1,
                               font)
            elif bl3:
                for i in range(max_rows1):
                    if i != 0:
                        gorod1 = str(data[i][5].get())
                        if gorod1 == gorod:
                            print(str(data[i][0].get()))
                            ndata.append(i)
                Add_fields(rows,ndata,color6,color7,color8,color9,color2,color1,color3,color5,color4,font1,font)