import tkinter as tk 
from tkinter import ttk 
feet_force=0
'''
LARGEFONT =("Verdana", 35) 
class tkinterApp(tk.Tk): 
    
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
        
        # __init__ function for class Tk 
        tk.Tk.__init__(self, *args, **kwargs) 
        
        # creating a container 
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True) 
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 
        # initializing frames to an empty array 
        self.frames = {} 
        # iterating through a tuple consisting 
        # of the different page layouts 
        for F in (StartPage, Page1, Page2): 
            frame = F(container, self) 
            # initializing frame of that object from 
            # startpage, page1, page2 respectively with 
            # for loop 
            self.frames[F] = frame 
            frame.grid(row = 0, column = 0, sticky ="nsew") 
        self.show_frame(StartPage) 
    # to display the current frame passed as 
    # parameter 
    def show_frame(self, cont): 
        frame = self.frames[cont] 
        frame.tkraise() 
# first window frame startpage 
class StartPage(tk.Frame): 
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent) 
        
        # label of frame Layout 2 
        label = ttk.Label(self, text ="Startpage", font = LARGEFONT) 
        
        # putting the grid in its place by using 
        # grid 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
        button1 = ttk.Button(self, text ="Page 1", 
        command = lambda : controller.show_frame(Page1)) 
    
        # putting the button in its place by 
        # using grid 
        button1.grid(row = 1, column = 1, padx = 10, pady = 10) 
        ## button to show frame 2 with text layout2 
        button2 = ttk.Button(self, text ="Page 2", 
        command = lambda : controller.show_frame(Page2)) 
    
        # putting the button in its place by 
        # using grid 
        button2.grid(row = 2, column = 1, padx = 10, pady = 10) 
        
# second window frame page1 
class Page1(tk.Frame): 
    
    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="Page 1", font = LARGEFONT) 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
        # button to show frame 2 with text 
        # layout2 
        button1 = ttk.Button(self, text ="StartPage", 
                            command = lambda : controller.show_frame(StartPage)) 
    
        # putting the button in its place 
        # by using grid 
        button1.grid(row = 1, column = 1, padx = 10, pady = 10) 
        # button to show frame 2 with text 
        # layout2 
        button2 = ttk.Button(self, text ="Page 2", 
                            command = lambda : controller.show_frame(Page2)) 
    
        # putting the button in its place by 
        # using grid 
        button2.grid(row = 2, column = 1, padx = 10, pady = 10) 
# third window frame page2 
class Page2(tk.Frame): 
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT) 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
        # button to show frame 2 with text 
        # layout2 
        button1 = ttk.Button(self, text ="Page 1", 
                            command = lambda : controller.show_frame(Page1)) 
    
        # putting the button in its place by 
        # using grid 
        button1.grid(row = 1, column = 1, padx = 10, pady = 10) 
        # button to show frame 3 with text 
        # layout3 
        button2 = ttk.Button(self, text ="Startpage", 
                            command = lambda : controller.show_frame(StartPage)) 
    
        # putting the button in its place by 
        # using grid 
        button2.grid(row = 2, column = 1, padx = 10, pady = 10) 
# Driver Code 
app = tkinterApp() 
app.mainloop() 
'''

LARGEFONT =("Verdana", 35) 
def goto_page_2():
        page1.forget()
        page2.pack(fill="both", expand=1)
        # page1.forget()

def goto_page_1():
        page2.forget()
        page1.pack(fill="both", expand=1)
        # page2.forget()


def set_text(num:int):
    global feet_force
    feet_force = feet_force*10 + num
    #feet_force_diasplay.config(text="{}".format(feet_force)) 
    feet_force_diasplay = tk.Label(page1, text=feet_force).grid(row=1,column=3)

    print(feet_force)

def clear():
    global feet_force
    feet_force=0
    feet_force_diasplay = tk.Label(page1, text="0").grid(row=1,column=3)


def show_feet_force():
    global feet_force
    return feet_force

def stop():
    root.destroy()

root = tk.Tk()
root.geometry('350x200')
root.title("welding")

page1 = tk.Frame(root)
page2 = tk.Frame(root)

heading_pg1 = tk.Label(page1,text = "Enter Feet Force:")
heading_pg1.grid(row=1,column=0)
feet_force_diasplay = tk.Label(page1, text=feet_force if feet_force !=0 else "0").grid(row=1,column=3)

tk.Button(page1, text="1", command=lambda: set_text(1),height=1, width=7).grid(row=5, column=0)
tk.Button(page1, text="2", command=lambda: set_text(2),height=1, width=7).grid(row=5, column=1)
tk.Button(page1, text="3", command=lambda: set_text(3),height=1, width=7).grid(row=5, column=2)
tk.Button(page1, text="4", command=lambda: set_text(4),height=1, width=7).grid(row=6, column=0)
tk.Button(page1, text="5", command=lambda: set_text(5),height=1, width=7).grid(row=6, column=1)
tk.Button(page1, text="6", command=lambda: set_text(6),height=1, width=7).grid(row=6, column=2)
tk.Button(page1, text="7", command=lambda: set_text(7),height=1, width=7).grid(row=7, column=0)
tk.Button(page1, text="8", command=lambda: set_text(8),height=1, width=7).grid(row=7, column=1)
tk.Button(page1, text="9", command=lambda: set_text(9),height=1, width=7).grid(row=7, column=2)
tk.Button(page1, text="0", command=lambda: set_text(0),height=1, width=7).grid(row=8, column=1)
tk.Button(page1, text="clear",command = lambda: clear(),height=1, width=7).grid(row=8, column=2)

button_to_page2 = tk.Button(page1,text="Start",command=goto_page_2,height=1, width=21)
button_to_page2.grid(row=10, column=1)

page1.pack(expand=1,fill="both")

######################### PAGE 2 ################################

heading_pg2 = tk.Label(page2,text = "this is page 2")
heading_pg2.grid(row=0, column=0)


tk.Button(page2, text="page 1",command=goto_page_1,height=1, width=7).grid(row=1,column=0)
tk.Button(page2,text="STOP",bg="red",command=stop, height=2, width=7).grid(row=2,column=1)


# page2.pack(expand=1,fill="both")
page2.forget()

root.mainloop()