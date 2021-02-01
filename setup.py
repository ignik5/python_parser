from tkinter import *
from tkinter import scrolledtext

def click():
    file=open('config.ini','w')#открыть фаил конфиг
    file.write('[Settings]'+"\n")#выполняем запись в фаил конфиг
    file.write("urll = " +urll.get(1.0, END)+"\n")
    file.write('koltovara = '+koltovara.get() +"\n")
    file.write('katal = '+katal.get() +"\n")
    file.close()
    import os
    os.system('parstovago.py') # выполнить запуск программы проверки цен xls.py
    window.quit()
   




window = Tk()#открываем окно приложения
window.title("Парсинг")
window.geometry('650x250')
lbl0=Label(window, text='            Парсинг' , font=("Arial Bold", 20))
lbl0.grid(column=0, row=2) 
#верстка приложения 
lbl1 = Label(window, text='вставьте URL каталога который нужно спарсить')
lbl1.grid(column=0, row=3)
urll = scrolledtext.ScrolledText(window, width=20, height=0.5)
urll.grid(column=1, row=3)
lbl2=Label(window, text='Введите количество страниц ')
lbl2.grid(column=0, row=5)
koltovara = Entry(window, width=10)
koltovara.grid(column=1, row=5)
lbl2=Label(window, text='Введите название каталога')
lbl2.grid(column=0, row=6)
katal = Entry(window, width=10)
katal.grid(column=1, row=6)
btn = Button(window, text="ВЫПОЛНИТЬ ", command=click) #кнопка выполнить запись в фаил и начать проверку 
btn.grid(column=2, row=9)  
#конец 'приложения'
window.mainloop()









