import tkinter as tk
from tkinter import ttk
import components

root = tk.Tk()
root.title("TdroidTool")
root.iconbitmap(None)
root.config()
ico=tk.PhotoImage(file="./rootico.png")
root.iconphoto(True,ico)
root.configure(relief="flat")
root.configure(background="#125173")
root.resizable(False,False)
#notebool
ntbk=ttk.Notebook(root,height=500,width=900)
ntbk.grid(row=0,column=0)

#function to make frames

"""adbtab=tk.Frame(ntbk,bg="#4d6182")
adbframe=ttk.Frame(adbtab,height=500,width=100)
adbframe.grid(row=0,column=0)


fastab=tk.Frame(ntbk,bg="#4d6182")
fastframe=ttk.Frame(fastab,height=500,width=100)
fastframe.grid(row=0,column=0)"""
adbtab = components.frame(ntbk,'adbframe')
fastab = components.frame(ntbk,'fastbootframe')
ntbk.add(adbtab,text='Adb Utils')
ntbk.add(fastab,text='Fastboot Utils')

tk.mainloop()