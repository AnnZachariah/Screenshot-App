import time
from tkinter import *
import pyautogui

def ss():
    name=int(round(time.time()*1000))
    name='Image'+'{}.png'.format(name)
    #time.sleep(2)
    img = pyautogui.screenshot(name)
    img.show()
    root.deiconify()

def delay():
    root.withdraw()
    root.after(1000,ss)

root = Tk()
root.title('Screenshot')
root['bg']='White'
root.geometry('250x150')
root.wm_iconbitmap('icon.ico')

root.resizable(0,0)

btn1=Button(root,text="Take Screenshot", font=('Arial',10,'bold'),height=2,width=18,fg='yellow',bg='black',command=delay).place(x=45,y=10)
btn1=Button(root,text="Quit", font=('Arial',10,'bold'),height=2,width=18,fg='yellow',bg='black',command=quit).place(x=45,y=80)


root.mainloop()
