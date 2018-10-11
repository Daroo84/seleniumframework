
###  Program do generowania dziennej listy bugow. Wyłącznie dla
###  confluence samsung ze wzgledu na generujący się w excelu link
###  do każdego raportowanego bugu.

###   pip install xlwt

#Biblioteki
from xlwt import Workbook
from tkinter import *
import xlwt
import getpass
import datetime
import tkinter.messagebox

okno=Tk()
okno.title('Daily bugs raport')

heading = Label(okno, text = 'Daily bugs raport', font = 'bold')
heading.grid(row = 0, columnspan = 4)

#wprowadzanie danych do GUI
bug = StringVar()
bug = Entry(okno, textvariable = bug)
urzadzenie = StringVar()
urzadzenie = Entry(okno, textvariable = urzadzenie)
data = StringVar()
data = Entry(okno, textvariable = data)
priority = StringVar()
priority = Entry(okno, textvariable = priority)

bug1 = Label(okno, text = "Bug's name: ")
urzadzenie1 = Label(okno, text = "Device's name: ")
data1 = Label(okno, text = 'Date: ')
priority1 = Label(okno, text = 'Priority: ')

#Generowanie arkusza excel
wb = Workbook()
sheet1 = wb.add_sheet('Bugs')
sheet1.col(0).width = 6000
sheet1.col(1).width = 6000
sheet1.col(2).width = 4000
sheet1.col(3).width = 4000
sheet1.col(4).width = 11000
sheet1.write(0, 0, "Bugs: ")
sheet1.write(1, 0, "Bug's number: ")
sheet1.write(1, 1, 'Device: ')
sheet1.write(1, 2, 'Date: ')
sheet1.write(1, 3, 'Priority: ')
sheet1.write(1, 4, 'Link: ')


#Funckje dla przycisków
def clear_text():
    bug.delete(0, 'end')
    urzadzenie.delete(0, 'end')
    data.delete(0, 'end')
    priority.delete(0, 'end')

def exportxlc():
    czas = datetime.datetime.now()
    wb.save('C:/Users/'+getpass.getuser()+'/Desktop/Daily bugs list '+czas.strftime("%d-%B-%Y")+'.xls')

global r
r = int(1)

def dodawaniebuga():
    global r
    r += 1
    a = bug.get()
    b = urzadzenie.get()
    c = data.get()
    d = priority.get()
    passed = xlwt.easyxf('pattern: pattern solid, fore_colour green;')
    failed = xlwt.easyxf('pattern: pattern solid, fore_colour red;')
    medium = xlwt.easyxf('pattern: pattern solid, fore_colour yellow;')
    color = (passed if d in ['minor', 'Minor', 'MINOR'] else medium if d in ['major', 'Major'] else
             (failed if d in ['Critical', 'critical', 'blocker', 'Blocker'] else xlwt.easyxf()))
    sheet1.write(r, 0, a.upper())
    sheet1.write(r, 1, b.capitalize())
    sheet1.write(r, 2, c)
    sheet1.write(r, 3, d.capitalize(), style = color)
    sheet1.write(r, 4, 'https://smartthings.atlassian.net/browse/'+a)
    tkinter.messagebox._show('Bugs', 'Bug has been added!')


#przyciski
nastepny = Button(okno, text = 'Add bug', fg = 'black',padx = 20, pady = 10, command = dodawaniebuga)
cleaned = Button(okno, text = 'Clear', fg = 'black', padx = 20, pady = 10, command = clear_text)
export = Button(okno, text = 'Export to xls', fg = 'black',padx = 20, pady = 10, command = exportxlc)

#Modelowanie okna
bug1.grid(row = 2, column = 1)
urzadzenie1.grid(row = 3, column = 1)#, padx = 80, pady = 50)
data1.grid(row = 4, column = 1)
priority1.grid(row = 5, column = 1)#, padx = 80, pady = 50)
bug.grid(row = 2, column = 2)
urzadzenie.grid(row = 3, column = 2)#, padx = 80, pady = 50)
data.grid(row = 4, column = 2)
priority.grid(row = 5, column = 2)#, padx = 80, pady = 50)
nastepny.grid(row = 6, column = 1,padx = 20, pady = 10)#, padx = 40, pady = 10)
export.grid(row = 6, column = 2,padx = 20, pady = 10)
cleaned.grid(row = 6, column = 3, padx = 20, pady = 10)


okno.mainloop()

