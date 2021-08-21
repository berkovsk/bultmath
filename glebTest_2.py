import sys
if sys.platform != 'linux':
    import msvcrt as ms
import time
import random as rnd
import task_generator as gen
import wdgtCnfg as cnfg
from tkinter import *



  
class Setting:
    timeOut_ms = 15000
    numEx = 30
    def finalImg(perc):
        if perc <= 25:
            return 'Очень плохо, включи мозги!',5
        elif perc <= 50:
            return 'Плохо!', 0
        elif perc <= 85:
            return 'Можешь лучше!', 4
        elif perc < 100:
            return 'Молодец!', 2
        else:
            return '', 3
        
        
    
    
class Tsk:    
    def readTasks(tasks):
        Tsk.ex = tasks
    def clear():
        Tsk.ex = []
        Tsk.exFail = []
        Tsk.nCurr = 0        
    def onAns(ans): 
        if stateTest.corrAns:
           if (ans):
              Tsk.nCurr += 1
        else:
            if not(ans):
                Tsk.exFail.append(Tsk.nCurr)
            Tsk.nCurr += 1
        
root = Tk();   
e = Entry()
cnfg.exmplEntryCnfg(e)
l = Label()
l0 = Label() #Информационная метка,отображает состояние тест/исправление
l_img = Label()
class stateTest:
    corrAns = False
    percSolved = 0;

def chMod():
    windMod = Toplevel(root)   
    b = Button(windMod,text ='OK',command = windMod.destroy)
    l = Label(windMod,text = 'Время на решение,сек')
    l.pack()
    e = Entry(windMod)   
    e.pack()    
    def setTimeOut(event):
        Setting.timeOut_ms = 1000 * eval(e.get())
    e.bind( '<Return>', setTimeOut)
    l1 = Label(windMod,text = 'Количество примеров')
    l1.pack()
    e1 = Entry(windMod)   
    e1.pack()    
    def setTimeOut(event):
        Setting.timeOut_ms = 1000 * eval(e.get())
    def setNumEx(event):
        Setting.numEx = eval(e1.get())
    e1.bind( '<Return>', setNumEx)    
    b.pack()  
    print('Mode is changed')
    
b = Button(text = 'Изменить настройки', command = chMod)
b.pack()
cnfg.menuBtnCnfg(b)

def startTest():
   Tsk.clear()
   if Tsk.nCurr == 0:
        e.pack_forget()
        l0.pack()
        e.pack()
        l.pack()        
   l0['text'] = 'Основной тест, пример ' + str(Tsk.nCurr + 1) + ' из ' + str(Setting.numEx)
   cnfg.stateLblCnfg(l0)
   l.pack_forget()
   l_img.pack_forget()
   stateTest.corrAns = False
   e['state'] = NORMAL
   b['state'] = DISABLED
   b1['state'] = DISABLED
   e.delete(0,END)
   ex = gen.get_tasks(Setting.numEx) 
   print(ex)       
   Tsk.readTasks(ex)
   e.focus()
   e.pack() 
   e.insert(0,Tsk.ex[0][0] + ' = ')
   if len(Tsk.ex[0]) == 2:
       root.task = e.after(Setting.timeOut_ms, timeOut)
   elif len(Tsk.ex[0]) == 3:
       root.task = e.after(Tsk.ex[Tsk.nCurr][2], timeOut)

   
   
def endTest():
     e.insert(0,'Основной тест закончен ')
     l0.focus()
     l0.pack_forget()
     e['state']  = DISABLED
     l.pack()
     cnfg.infoLblCnfg(l)      
     if len(Tsk.exFail) > 0:
         msg = 'Не решенo '+ str(len(Tsk.exFail)) + \
         '  из '+ str(Setting.numEx) +'!\n Исправление ошибок скоро начнется. Жди...'
         l['text'] = msg
         Tsk.nCurr = 0;
         stateTest.corrAns = True
         l.after(5000,nextEx_corr)
         stateTest.percSolved = 100 * (1 - len(Tsk.exFail) / Setting.numEx)
         finMsg,finImg = Setting.finalImg(stateTest.percSolved)
         l_img['image'] = img[finImg]
         l_img.pack()
     else:
         msg = ' Tecт пройден без ошибок!\nТы СУПЕРГЕРОЙ!!'
         l['text'] = msg
         b['state'] = NORMAL
         b1['state'] = NORMAL
         finMsg,finImg = Setting.finalImg(100)
         l_img['image'] = img[finImg]
         l_img.pack()
         
def endTest_corr():
     e.insert(0,'Ошибки исправлены! ')
     l0.pack_forget()
     e['state']  = DISABLED
     l.pack()
     cnfg.infoLblCnfg(l)
     finMsg,finImg = Setting.finalImg(stateTest.percSolved)
     msg = 'Вовремя решенo '+ str(Setting.numEx - len(Tsk.exFail)) \
     +' из '+ str(Setting.numEx) +'!\n' + finMsg
     l['text'] = msg
     b['state'] = NORMAL
     b1['state'] = NORMAL    
     l_img['image'] = img[finImg]
     l_img.pack()
     
   
def nextEx():
    e.focus()
    l.pack_forget()
    l_img.pack_forget()
    l0['text'] = 'Основной тест, пример ' + str(Tsk.nCurr + 1) + ' из ' + str(Setting.numEx)      
    e['state'] = NORMAL
    e.delete(0,END)
    if Tsk.nCurr >= Setting.numEx:
       endTest()
    else:
        e.insert(0,Tsk.ex[Tsk.nCurr][0] + ' = ') 
        if len(Tsk.ex[Tsk.nCurr]) == 2:
           root.task = e.after(Setting.timeOut_ms, timeOut)
        elif len(Tsk.ex[Tsk.nCurr]) == 3:
           root.task = e.after(Tsk.ex[Tsk.nCurr][2], timeOut)
        
def nextEx_corr():
    e.focus()
    if Tsk.nCurr == 0:
        e.pack_forget()
        l0.pack()
        e.pack()
    l.pack_forget()
    l_img.pack_forget()     
    e['state'] = NORMAL
    l0['text'] = 'Исправление ошибок, пример ' + str(Tsk.nCurr + 1) + ' из ' + str(len(Tsk.exFail))
    e.delete(0,END)
    if Tsk.nCurr >= len(Tsk.exFail):
       endTest_corr()
    else:
        e.insert(0,Tsk.ex[Tsk.exFail[Tsk.nCurr]][0] + ' = '  )
        #root.task = e.after(Setting.timeOut_ms, timeOut)
        
b1 = Button(text = 'Пройти тест', command = startTest)
b1.pack()
cnfg.menuBtnCnfg(b1)
l.pack()
cnfg.greetingsLblCnfg(l)
img = []
for k in range(1,7):
   img.append(PhotoImage(file='/home/bna/GlebTestPy/bultik/Dog_'+str(k)+'.gif'))
l_img['image'] = img[1]
l_img.pack()

def timeOut():
    l0.focus() # Чтобы уБрать фокус с поля ввода
    e['state']  = DISABLED
    cnfg.ErrorLblCnfg(l)    
    l['text'] ='Время истекло!'
    Tsk.onAns(False)
    l.pack()    
    l.after(2000,nextEx)
    l_img['image'] = img[5]
    l_img.pack()

def checkAns(event):
    e['state']  = DISABLED 
    e.after_cancel(root.task)
    l0.focus() # Чтобы уБрать фокус с поля ввода
    s = e.get();
    print(s)
    ans = False
    if stateTest.corrAns:
        trueAns = Tsk.ex[Tsk.exFail[Tsk.nCurr]][1]
    else:
        trueAns = Tsk.ex[Tsk.nCurr][1]
    
    try:
        if (s[-len(trueAns) :] == trueAns) and (s[-len(trueAns)-3:-len(trueAns)] == ' = '):
            cnfg.OKLblCnfg(l)
            l['text'] = 'Правильно!'
            ans = True            
            l_img['image'] = img[2]            
        else:
            cnfg.ErrorLblCnfg(l)
            l['text'] ='Ошибка!'            
            l_img['image'] = img[5]           
    except:
        l['text'] ='Ошибка!'       
        l_img['image'] = img[5]
    Tsk.onAns(ans)
    l.pack()
    l_img.pack()
    if stateTest.corrAns:
       l.after(2000,nextEx_corr)
    else:
       l.after(2000,nextEx)
    
    
    
       
        
   
e.bind('<Return>',checkAns)

root.mainloop()      
            
    
       
        
        