import tkinter as tk
from tkinter import filedialog as fd
import tkinter.filedialog

import fastboot
from fastboot import *
root=tk.Tk()
root.configure(background='#a19c8d',height=500,width=500)
root.title('t-device tool')
root.maxsize(height=700,width=800,)
root.resizable(False,False)
#frames
lab=tk.Label(root,text="Fastboot Utility")
lab.place(y=0,x=200)
frem2 =tk.Frame(root,height=250,width=500)
frem2.config(bg='black',relief='flat')
frem2.place(x=102,y=30)
log=tk.Text(frem2,background='black'
            ,foreground='cyan'
            ,pady=1,padx=3,
            highlightthickness=0)
log.place(x=0,y=0)
frem1 = tk.Frame(root,height=500,width=100)
frem1.configure(background='white')
frem1.place(x=0,)
flasher = tk.Frame(root, height=250, width=500)
flasher.config(borderwidth=0)
flasher.place(x=100, y=250)
flasher.configure(bg='grey')
#buttons
#dialog
def filopn():
    file_types=[('xml files','**.xml')]
    load_file=fd.askopenfile(title='load firmware',filetypes=file_types,initialdir='./')

#functions

def dtfun():
    log.delete('1.0','end')
    log.insert(tk.END,"scanning for fastboot device \n")
    detct()
    device = FastbootManager.devices()
    log.insert(tk.END,device)

def btn(cnt,txt,nem):
    nem = tk.Button(cnt, text=txt)
    return
def getvar():
     fastboot.getVar('all')


detect=tk.Button(frem1,text='Detect'
                 ,bg='black',width='5'
                 ,command=dtfun,
                 borderwidth=1,
                 highlightthickness=0)
detect.place(x=0,y=0)
Info=tk.Button(frem1,text='Read Info',width=5,command=getvar)
Info.place(x=1,y=30)
Info.configure(command=getVar,highlightthickness=0,borderwidth=1,)
sel=tk.Button(flasher,text='Load firmware',
              relief='flat'
              ,borderwidth=0,bd=0,
              highlightthickness=0,command=filopn)
oem=tk.Button(frem1,text='Oem Unlock',width=5)
oem.place(x=0,y=60)
flashbtn =tk.Button(flasher,text='flash'
                    ,highlightthickness=0,
                    borderwidth=0,
                    relief='groove')
flashbtn.place(x=0,y=21)
sel.place(x=0)
root.mainloop()