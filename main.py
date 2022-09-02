import tkinter as tk

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
frem2.config(bg='black')
frem2.place(x=102,y=30)
log=tk.Text(frem2,background='black',foreground='cyan',pady=0,padx=0)
log.place(x=0,y=0)
frem1 = tk.Frame(root,height=500,width=100)
frem1.configure(background='white')
frem1.place(x=0,)
#buttons
#functions
def dtfun():
    log.delete('1.0','end')
    log.insert(tk.END,'scanning for fastboot device ')
def btn(cnt,txt,nem):
    nem = tk.Button(cnt, text=txt)
    return
detect=tk.Button(frem1,text='Detect',bg='black',width='5',command=dtfun)
detect.place(x=0)
btn
root.mainloop()