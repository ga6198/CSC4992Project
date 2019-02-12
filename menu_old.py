import tkinter as tk
from tkinter import ttk
from os.path import join, realpath, dirname
#from homemenu import HomeMenu

#define default fonts
TITLE_FONT = ('Verdana', 12)

class Menu(tk.Tk):

    def __init__(self, *args, **kwargs):
        # initialize tkinter
        tk.Tk.__init__(self, *args, **kwargs)

        # set window title
        tk.Tk.wm_title(self, "Memory Game")

        # Initialize window  
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #create menu frames/pages
        self.frames = {}

        #add new frames in this for loop
        for eachFrame in (HomeMenu, SinglePlayerMenu, TwoPlayerMenu):
            frame = eachFrame(container, self)
            self.frames[eachFrame] = frame
            frame.grid(row=0, column = 0, sticky="nsew")

        self.showFrame(HomeMenu)

    def showFrame(self, controller):
        '''display function to show menu frames'''
        frame = self.frames[controller]
        frame.tkraise() #send passed frame to front

class HomeMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Memory Game", font=TITLE_FONT)
        label.pack(padx=20, pady=10, side=tk.TOP)
        #label.grid(row=1,column=1)

        #create single player button
        singlePlayerButton = ttk.Button(self, text="Single Player",
                                       command=lambda: controller.showFrame(SinglePlayerMenu))
        singlePlayerButton.pack(padx=10, pady=10, side=tk.LEFT)
        #singlePlayerButton.grid(row=3,column=1)

        #create two player button
        twoPlayerButton = ttk.Button(self, text="Two Player",
                                     command=lambda: controller.showFrame(TwoPlayerMenu))
        twoPlayerButton.pack(padx=10, pady=10, side=tk.RIGHT)
        #twoPlayerButton.grid(row=4,column=1)

        #FIXME: Switch to minimenu later (might be easier to use toolbar)
        #twoPlayerButton.grid(row=6,column=2)
        

class SinglePlayerMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Single Player", font=TITLE_FONT)
        label.pack(padx=10, pady=10)

        #create back button
        backButton = tk.Button(self, text="Back",
                                       command=lambda: controller.showFrame(HomeMenu))

        #getting image directory
        #FIXME: use directoryParser class eventually
        currentPath = dirname(realpath(__file__))
        imagePath = join(currentPath, "images", "menu", "back_button.gif")
        backImage = tk.PhotoImage(file=imagePath)
        backButton.image=backImage #keep reference to photo
        backButton.config(image=backImage)
        backButton.pack()

class TwoPlayerMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Two Player", font=TITLE_FONT)
        label.pack(padx=10, pady=10)

        #create back button
        backButton = tk.Button(self, text="Back",
                                       command=lambda: controller.showFrame(HomeMenu))
        backButton.pack()
                

if __name__ == "__main__":
    menus = Menu()
    menus.mainloop()





    