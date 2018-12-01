from tkinter import PhotoImage
import tkinter as tk
def ErrorLblCnfg(l):
    l['bg'] = 'red'
    l['fg'] = 'yellow'
    l['font'] = ('Helvetica',30)
def OKLblCnfg(l):
    l['bg'] = 'green'
    l['fg'] = 'white'
    l['font'] = ('Helvetica',30)
def infoLblCnfg(l):
    l['bg'] = 'yellow'
    l['fg'] = 'red'
    l['font'] = ('Helvetica',30)
def exmplEntryCnfg(e):
     e['font'] = ('Helvetica',32)
     e['fg'] = 'blue'
def menuBtnCnfg(b):
    b['font'] = ('Helvetica',16)
def stateLblCnfg(l):
    l['bg'] = 'cyan'
    l['fg'] = 'red'
    l['font'] = ('Helvetica',30)
#def imgLblCnfg(l,img):#"ЭТА ФУНКЦИЯ НЕ СТАЛА РАБОТАТЬ
    #fileName = 'Dog_' + str(k) + '.gif'
    #fileName = 'C:\Documents\PythonTrain\Dog_6.gif'
    #img = PhotoImage(file=fileName)
    #l['image'] = img
def greetingsLblCnfg(l):
    l['text'] = "Здорово, Глеб! Меня зовут Бультик!\n Я умею решать примеры.\n  Интересно, на что  способен ты!\n Жми \"Пройти тест!\""
    l['font'] = ('Helvetica',28)
    l['bg'] = 'white'
    l['fg'] = 'green'