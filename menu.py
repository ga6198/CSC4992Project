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
        self.frame = None
        
        self.switchFrame(HomeMenu)

    def switchFrame(self, frameClass):
        '''display function to show menu frames'''
        '''destroy current frame and replace it'''
        newFrame = frameClass(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = newFrame
        self.frame.pack()

class HomeMenu(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Memory Game", font=TITLE_FONT)
        label.pack(padx=20, pady=10, side=tk.TOP)
        #label.grid(row=1,column=1)

        #create single player button
        singlePlayerButton = tk.Button(self, text="Single Player",
                                       command=lambda: master.switchFrame(SinglePlayerMenu))
        singlePlayerButton.pack(padx=10, pady=10, side=tk.LEFT)
        #singlePlayerButton.grid(row=3,column=1)

        #create two player button
        twoPlayerButton = tk.Button(self, text="Two Player",
                                     command=lambda: master.switchFrame(TwoPlayerMenu))
        twoPlayerButton.pack(padx=10, pady=10, side=tk.RIGHT)
        #twoPlayerButton.grid(row=4,column=1)

        #FIXME: Switch to minimenu later (might be easier to use toolbar)
        #twoPlayerButton.grid(row=6,column=2)
        

class SinglePlayerMenu(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Single Player", font=TITLE_FONT)
        label.pack(padx=10, pady=10)

        #create back button
        backButton = tk.Button(self, text="Back",
                                       command=lambda: master.switchFrame(HomeMenu))

        #getting image directory
        #FIXME: use directoryParser class eventually
        currentPath = dirname(realpath(__file__))
        imagePath = join(currentPath, "images", "menu", "back_button.gif")
        backImage = tk.PhotoImage(file=imagePath)
        backButton.image=backImage #keep reference to photo
        backButton.config(image=backImage)
        backButton.pack()

class TwoPlayerMenu(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Two Player", font=TITLE_FONT)
        label.pack(padx=10, pady=10)

        #create back button
        backButton = tk.Button(self, text="Back",
                                       command=lambda: master.switchFrame(HomeMenu))
        backButton.pack()
                

if __name__ == "__main__":
    menus = Menu()
    menus.mainloop()





    
