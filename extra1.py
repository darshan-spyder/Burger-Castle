import tkinter as tk
import PIL
from Config import *

root = tk.Tk()

class UI(): #Main Menu

    def __init__(self, master):

        #Create Main Menu Window

        self.master = master
        self.master.title("Monopoly")
        self.master.wm_iconbitmap('icons\Monopoly-Icon.ico')
        self.master.geometry((resolution))

        #Menu Buttons

        self.label = tk.Label(master, text= 'Welcome to Monopoly! PLACEHOLDER')
        self.playButton = tk.Button(master, text= 'Play Game', command= self.playGame)
        self.settingsButton = tk.Button(master, text= 'settings', command= self.settings)
        self.exitButton = tk.Button(master, text= 'Exit', command= self.exitGame)

        self.label.grid(columnspan=2)
        self.playButton.grid(column=0)
        self.settingsButton.grid(column=0)
        self.exitButton.grid(column=0)

    def settings(self):       #Opens Settings Window
        s = tk.Toplevel()
        s.title('Settings')
        s.wm_iconbitmap('icons\Monopoly-Icon.ico')
        s.geometry((resolution))
        self.master.withdraw()
        resLabel = tk.Label(s, text= 'Resolution')
        resOption = tk.OptionMenu(s, resolution, *resList)

        resLabel.grid(column=0,row=0)
        resOption.grid(column=0, row=4)

    def showMenu(self):     #Bring back menu windwow
        self.master.deiconify()

    def exitGame(self):    #Exit Game Method
        root.destroy()

    def playGame(self):     #Start the main game window
        self.master.withdraw()
        gameWindow()

class gameWindow(UI):

    def __init__(self):

        self.g = tk.Toplevel()
        self.g.title('Monopoly')
        self.g.wm_iconbitmap('icons\Monopoly-Icon.ico')
        self.g.geometry((resolution))

        self.menuButton = tk.Button(self.g, text= 'Main Menu', command= self.exitMenu)

        self.menuButton.grid(column=0,row=0)

    def exitMenu(self):
        self.g.destroy()
        UI(root).showMenu()

mainMenu = UI(root)

root.mainloop()
