from tkinter import Tk, Frame, Button, Label , Entry, StringVar,W


xdis = 5
ydis= 5
# root = Tk()
# root.title("friction welding")

# frame1 = Frame(root)
# frame1.pack()

def set_text(text):
    widget = gui.focus_get()
    if widget in [entry1, entry2]:
        widget.insert("insert", text)
    
def backspace():#Delete one digit at a time into perticular entry field
    pass

def clear():#Clear text in perticular entry field 
    entry1.delete(0,END)
    entry2.delete(0,END)



#create GUI
# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk()
    gui.title("GUI") 

   
    #Label 1
    label1 = Label(text ="Pumpenhöhe 1 [cm]")
    label1.grid (row =0 , column =0 , padx = xdis , pady = ydis )

    #Eingabefeld 1 definieren
    entry1 = Entry(gui, textvariable=StringVar(), width=4, bg ='#ffffff')
    entry1.grid(row=0, column=1, padx=xdis, pady = ydis)
    

    #Label 2
    label2 = Label (text ="Pumpenhöhe 2 [cm]") 
    label2.grid(row=1,column =0 , padx = xdis ,pady = ydis)

    #Eingabefeld 2
    entry2 = Entry(gui, textvariable=StringVar(), width=4,  bg ='#ffffff')
    entry2.grid(row=1, column=1, padx=xdis, pady = ydis)
    
    
    #create exit button
    ex_bt = Button(gui, text='Exit', command=root.destroy)
    ex_bt.grid(row=4, column=2, sticky=W, padx=xdis, pady=ydis)
    
    #button obj to start thread
    #start_thread = tkinter.Button(text ="start thread(main loop)", command=start_thread)
    #start_thread.grid(row=2, column=1, padx=xdis, pady = ydis)
    
    #button obj to stop thread
    #stop_thread = tkinter.Button(text ="Stop", command=stop_thread)
    #stop_thread.grid(row=2, column=3, padx=xdis, pady = ydis)

    #button obj on framework to send values
    set_setpoints = Button(text ="Send", command = set_setpoints)
    set_setpoints.grid(row=2, column=2, padx= xdis, pady = ydis)
    
    
    
        
    #buttons for numpad
    Button(gui, text="7", command=lambda: set_text("7"),height=1, width=7).grid(row=5, column=0)
    Button(gui, text="8", command=lambda: set_text("8"),height=1, width=7).grid(row=5, column=1)
    Button(gui, text="9", command=lambda: set_text("9"),height=1, width=7).grid(row=5, column=2)
    Button(gui, text="4", command=lambda: set_text("4"),height=1, width=7).grid(row=6, column=0)
    Button(gui, text="5", command=lambda: set_text("5"),height=1, width=7).grid(row=6, column=1)
    Button(gui, text="6", command=lambda: set_text("6"),height=1, width=7).grid(row=6, column=2)
    Button(gui, text="1", command=lambda: set_text("1"),height=1, width=7).grid(row=7, column=0)
    Button(gui, text="2", command=lambda: set_text("2"),height=1, width=7).grid(row=7, column=1)
    Button(gui, text="3", command=lambda: set_text("3"),height=1, width=7).grid(row=7, column=2)
    Button(gui, text="0", command=lambda: set_text("0"),height=1, width=7).grid(row=7, column=1)
    
    backspace = Button(gui, text='<-', command = lambda:backspace())                      
    backspace.grid(row=3,column=1, padx=xdis, pady=ydis)
    
    clear_btn = Button(gui, text='C', command = lambda:clear())
    clear_btn.grid(row=3,column=2, padx=xdis, pady=ydis)

    gui.mainloop()