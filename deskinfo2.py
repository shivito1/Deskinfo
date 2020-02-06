import os
from tkinter import *


class Deskinfo:
    def __init__ (self, root):
        self.root = root
        root.wm_title("JS")
        root.maxsize(width=400, height=400)
        root.bind("<FocusIn>", self.Test)
        root.bind("<Enter>", self.expand)
        root.bind("<Leave>", self.collapse)
        root.bind("<FocusOut>", self.Back)
        root.overrideredirect(1)
        root.configure(background="#7fb2c6")
        root.attributes("-topmost", True)

        # width for the Tk root
        self.screen_w = 200
        # height for the Tk root
        self.screen_h = 70
        root.protocol('WM_DELETE_WINDOW', self.Onexit)
        # get screen width and height
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        self.screen_x = ws - 200
        self.screen_y = hs - hs

        # set the dimensions of the screen 
        # and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (self.screen_w, self.screen_h, self.screen_x, self.screen_y))
        root.attributes('-alpha', 0.1)

        hostname = os.popen(r"hostname").read()

        # Copy computer name to clipboard
        def CopyHostName():

            def topdestroy():
                top.destroy()
            top = Toplevel()
            top.overrideredirect(1)
            top.attributes("-topmost", True)
            
            w = 200 # width for the Tk top
            h = 70 # height for the Tk top
            top.protocol('WM_DELETE_WINDOW', self.Onexit)
            # get screen width and height
            ws = top.winfo_screenwidth() # width of the screen
            hs = top.winfo_screenheight() # height of the screen

            # calculate x and y coordinates for the Tk top window
            x = ws - 200
            y = hs - hs

            # set the dimensions of the screen with w, h
            # and where it is placed with x, y
            top.geometry('%dx%d+%d+%d' % (w, h, x, y))
            
            label = Label(top,text="Computer Name\nCoppied",height=40)
            label.pack()
            label.bind("<Button-1>", lambda e: top.destroy())
            self.root.clipboard_clear()
            self.root.clipboard_append(hostname)
            top.after(750, topdestroy)

        frame1 = Frame(root,width=200,height=70,bg="#7fb2c6")
        frame1.grid(row=3,rowspan=8,column=0,columnspan=5)

        lb = Label(root, text=("Computer Name:" + "\n" + hostname),font="""Times 14 bold""",bg="#7fb2c6")
        lb.grid(row=3,column=0)
        lb.bind("<Button-1>", lambda e: CopyHostName()) # Copy computer name to clipboard

        self.root.mainloop()
        
    def Test(self,event):
        self.root.attributes('-alpha', 1)
        print("test")

    def Back(self,event):
        self.root.attributes('-alpha', 0.5)
        self.root.geometry('%dx%d+%d+%d' % (self.screen_w, self.screen_h, self.screen_x + 195, self.screen_y - 65))
        
    def expand(self, event):
        self.root.attributes('-alpha', 1)
        self.root.geometry('%dx%d+%d+%d' % (self.screen_w, self.screen_h, self.screen_x, self.screen_y))
        
    def collapse(self, event):
        if str(self.root.focus_get()) == 'None':
            self.root.attributes('-alpha', 0.5)
            self.root.geometry('%dx%d+%d+%d' % (self.screen_w, self.screen_h, self.screen_x + 195, self.screen_y - 65))
            
        else:
            pass

    def Onexit(self):
        self.root.iconify()

    def Eexit(self):
        toast = os.getpid()
        os.popen("taskkill /F /IM " + str(toast))


Deskinfo(Tk())
