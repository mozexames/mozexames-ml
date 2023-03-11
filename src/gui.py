from tkinter import Tk, Label
from lib.reloader import run_with_reloader

class App(Tk):
  def __init__(self):
    Tk.__init__(self)
    Label(self, text="Press CTRL+R or CMD+R to reload me...").pack()

run_with_reloader(App(), '<Meta-r>', '<Control-R>', '<Control-r>')
