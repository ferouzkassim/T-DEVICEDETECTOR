import tkinter as tk
from tkinter import ttk
import components

root = tk.Tk()
root.title("TdroidTool")
root.iconbitmap(None)
root.config(height=600,width=1000)
ico=tk.PhotoImage(file="./rootico.png")
root.iconphoto(True,ico)
root.configure(relief="flat")
root.configure(background="#125173")
root.resizable(False,False)
ntbk=ttk.Notebook(root,height=600,width=1000,padding=10,)
ntbk.place(x=0,y=0)
#frames
adbframe=tk.Frame(ntbk)
fastbutframe=tk.Frame(ntbk)
samsungtab=tk.Frame(ntbk)
samtabfrm=tk.Frame(samsungtab)
samtabfrm.place(x=10, y=0)
samtabfrm.config(bg="black")
bl=tk.Radiobutton(samtabfrm)
ntbk.add(adbframe, text="AdbTab")
ntbk.add(fastbutframe, text="Fastboot Frame")
ntbk.add(samsungtab, text="Samsung module")
#notebool
def addbtn(name,root,txt):
  name = ttk.Button(root,text=txt)
  name.place(x=0,y=0)
adbinf = addbtn('adbinfo',adbframe,'ReadInfo')


tk.mainloop()