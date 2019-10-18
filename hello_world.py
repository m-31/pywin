#!/usr/bin/env python3
import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.mondialLabel = tk.Label(self, text='Hello World')
        self.mondialLabel.config(bg="#00ffff")
        self.mondialLabel.grid()
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

app = Application()
app.master.title('Sample application')
app.mainloop()