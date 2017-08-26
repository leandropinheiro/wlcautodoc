import sys

if sys.version_info < (3,0):
    import Tkinter as tkinter
    import tkMessageBox as mbox
else:
    import tkinter
    import tkinter.messagebox as mbox

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = tkinter.Tk()
master.title('Informações de Acesso')
print(master.geometry())
master.geometry("280x80")

tkinter.Label(master, text="First Name").grid(row=0)
tkinter.Label(master, text="Last Name").grid(row=1)

e1 = tkinter.Entry(master)
e2 = tkinter.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = tkinter.Button(master, text='Quit', command=master.quit)
b2 = tkinter.Button(master, text='Show', command=show_entry_fields)

b1.pack(side=LEFT, padx=5, pady=5)
b2.pack(side=LEFT, padx=5, pady=5)

master.mainloop()