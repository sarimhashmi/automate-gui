import tkinter
import time

xdis=5
ydis=5

def set_text(text):
    widget = root.focus_get()
    if widget in [entry1, entry2]:
        widget.insert("insert", text)

def clear():
    entry1.delete(0)

if __name__=="__main__":
    root = tkinter.Tk()
    root.title("Wielding")

    entry1 = tkinter.Entry(root, textvariable=tkinter.StringVar(), width=4, bg ='#ffffff')
    entry1.grid(row=0, column=1, padx=5, pady = 5)

    entry2 = tkinter.Entry(root, textvariable=tkinter.StringVar(), width=4,  bg ='#ffffff')
    entry2.grid(row=1, column=1, padx=5, pady = 5)

    ex_bt = tkinter.Button(root, text='Exit', command=root.destroy)
    ex_bt.grid(row=4, column=2, sticky=tkinter.W, padx=xdis, pady=ydis)
    
    tkinter.Button(root, text="7", command=lambda: set_text("7"),height=1, width=7).grid(row=5, column=0)
    tkinter.Button(root, text="8", command=lambda: set_text("8"),height=1, width=7).grid(row=5, column=1)
    tkinter.Button(root, text="9", command=lambda: set_text("9"),height=1, width=7).grid(row=5, column=2)
    tkinter.Button(root, text="4", command=lambda: set_text("4"),height=1, width=7).grid(row=6, column=0)
    tkinter.Button(root, text="5", command=lambda: set_text("5"),height=1, width=7).grid(row=6, column=1)
    tkinter.Button(root, text="6", command=lambda: set_text("6"),height=1, width=7).grid(row=6, column=2)
    tkinter.Button(root, text="1", command=lambda: set_text("1"),height=1, width=7).grid(row=7, column=0)
    tkinter.Button(root, text="2", command=lambda: set_text("2"),height=1, width=7).grid(row=7, column=1)
    tkinter.Button(root, text="3", command=lambda: set_text("3"),height=1, width=7).grid(row=7, column=2)
    tkinter.Button(root, text="0", command=lambda: set_text("0"),height=1, width=7).grid(row=7, column=1)

    clear_btn = tkinter.Button(root, text='C', command = lambda:clear())
    clear_btn.grid(row=3,column=2, padx=xdis, pady=ydis)

    root.mainloop()