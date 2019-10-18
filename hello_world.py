#!/usr/bin/env python3
#import tkinter as tk
from tkinter import ttk

class Application(ttk.Frame):

    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.mondialLabel = ttk.Label(self, text='Hello World')
        self.mondialLabel.grid()
        style = ttk.Style()
        style.map("C.TButton",
                  foreground=[('pressed', 'red'), ('active', 'blue')],
                  background=[('pressed', '!disabled', 'black'),
                              ('active', 'white')]
                  )
        self.quitButton = ttk.Button(self, text='Quit', command=self.quit, style='C.TButton')
        self.quitButton.grid(row=2, column=2, sticky='w')

app = Application()
app.master.title('Sample application')
app.mainloop()