from tkinter.filedialog import asksaveasfilename

def Srsave(srball,gorod,bl4,bl5,bl6,root6):
    """
    Функция для сохранения среднего балла в txt файл\n
    Принимает на вход:\n
                    srball - средний балл по выбранным предметам\n
                    gorod - название города, если имеется\n
                    bl4 - значение флажка (true or false)\n
                    bl5 - значение флажка (true or false)\n
                    bl6 - значение флажка (true or false)\n
                    root6 - название второстепенного окна\n
    Выполнил Сапожников А.А.
    """

    file_name = asksaveasfilename()
    file_name = str(file_name)
    fn = open(file_name, 'w')
    root6.destroy()
    srball = round(srball,2)
    srball = str(srball)
    if gorod != "" and bl4 and bl5 and bl6:
        fn.write('Средний балл по физике, математике и русскому в городе ' + gorod + ' равен ' + srball)
    elif gorod != "" and bl4 and bl5:
        fn.write('Средний балл по физике и математике в городе ' + gorod + ' равен ' + srball)
    elif gorod != "" and bl4 and bl6:
        fn.write("Средний балл по физике и русскому в городе " + gorod + " равен " + srball)
    elif gorod != "" and bl5 and bl6:
        fn.write("Средний балл по математике и русскому в городе " + gorod + " равен " + srball)
    elif gorod == "" and bl4 and bl5 and bl6:
        fn.write("Средний балл по физике, математике и русскому в стране равен " + srball)
    elif gorod == "" and bl4 and bl5:
        fn.write("Средний балл по физике и математике в стране равен " + srball)
    elif gorod == "" and bl4 and bl6:
        fn.write("Средний балл по физике и русскому в стране равен " + srball)
    elif gorod == "" and bl5 and bl6:
        fn.write("Средний балл по математике и русскому в стране равен " + srball)
    elif gorod != "" and bl4:
        fn.write("Средний балл по физике в городе " + gorod + " равен " + srball)
    elif gorod != "" and bl6:
        fn.write("Средний балл по русскому в городе " + gorod + " равен " + srball)
    elif gorod != "" and bl5:
        fn.write("Средний балл по математике в городе " + gorod + " равен " + srball)
    elif gorod == "" and bl4:
        fn.write('Средний балл по физике в стране равен ' + srball)
    elif gorod == "" and bl6:
        fn.write("Средний балл по русскому в стране равен " + srball)
    elif gorod == "" and bl5:
        fn.write("Средний балл по математике в стране равен " + srball)
    fn.close()