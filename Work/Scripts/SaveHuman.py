from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import showerror
def SaveHuman(data,ndata,root5):
    """
    Функция для сохрнанеия людей по выбранными вами критериями\n
    Принимает на вход:\n
                    data - новую матрицу из ссылок\n
                    ndata - индексы нужных людей в этой матрице\n
                    root5 - название второстепенного окна с доп. функциями\n
    Выполнил Сапожников А.А.
    """
    l = 1
    for i in ndata:
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
    file_name = asksaveasfilename()
    file_name = str(file_name)
    fn = open(file_name, 'w')
    fn.write("Выбранные люди по вашим критериям:\n")
    for i in ndata:
        if i!=0:
            a = data[i][0].get()
            b = data[i][1].get()
            fn.write(a + " " + b + "\n")
    fn.close()
    root5.destroy()
