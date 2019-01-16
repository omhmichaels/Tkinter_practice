
"""
# 
# Author: l33tH@x0rxxGh0u1
# 
# 
#
#
"""
# Imports
import tkinter as tk

# Global Variables
Large_Font = ("Verdana", 12)

class SeaofBTCapp(tk.Tk):     # Initialization of class. (tk.Tk) defines inheritance 
    def __init__(self, *args, **kwargs):          # __init__ method initializes with the class. 
        tk.Tk.__init__(self, *args, **kwargs)     # i.e it always runs on startup
                                                  # # args == unlimited variables, kwargs dictionaries
        # container always needs to be defined and populated
        container = tk.Frame(self)                # Frame is the window
        container.pack(side="top", fill="both", expand=True)    

        # Basic Configuration
        container.grid_rowconfigure(0, weight=1) 
        #
        container.grid_columnconfigure(0, weight=1) 

        # Dictionary
        self.frames = {}

        #
        for F in (StartPage, PageOne, PageTwo):
            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Works by holding a bunch of frames then bringing the one you want to the front

        
        # sticky is alignment north,south,east,west

        # show frame == what do you want to show
        self.show_frame(StartPage)

    def show_frame(self, cont):
       frame = self.frames[cont]
       frame.tkraise()

    # This code is the base code for making pages
"""
# Function that prints whatever is passed into it
def qf(quickPrint):
    print(quickPrint)
"""

# Start Page code
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # How to add text in tk
        label = tk.Label(self, text="Welcome Ghoul", font=Large_Font)
        # Padding
        # Use grid instead of pack unless simple
        label.pack(pady=10, padx=10)

        # Button for changing pages
        button = tk.Button(self, text="Visit the next page",
        command=lambda: controller.show_frame(PageOne))

        button.pack()

        button2 = tk.Button(self, text="Visit Page Two", 
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageOne(tk.Frame):
    
    def __init___(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=Large_Font )
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage) )
        button1.pack() 

        button2 = tk.Button(self, text="Page Two",command=lambda: controller.show_frame(PageTwo))
        button2.pack()
       
class PageTwo(tk.Frame):
    
    def __init___(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=Large_Font )
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage) )
        button1.pack() 

        button2 = tk.Button(self, text="Page One",command=lambda: controller.show_frame(PageTwo))
        button2.pack()

app = SeaofBTCapp()
app.mainloop()




       
