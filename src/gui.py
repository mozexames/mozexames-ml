from tkinter import Frame, Grid, PhotoImage, Tk, Label
from turtle import bgcolor
from PIL import ImageTk, Image, ImageOps
from lib.reloader import run_with_reloader
from lib.root import Root

class App(Tk):
  def __init__(self):
    Tk.__init__(self)

    screen_width = 800 # self.winfo_screenwidth()
    screen_height = 500 # self.winfo_screenwidth()

    self.geometry(f"{screen_width}x{screen_height}")

    image_path = Root.out('1.jpg')
    out_image_path = Root.out('ml.png')

    input_frame = Frame(self, width=int(screen_width / 2), height=screen_height)
    input_frame.grid(column=0, row=0)

    output_frame = Frame(self, width=int(screen_width / 2), height=screen_height, bg='orange')
    output_frame.grid(column=1, row=0)

    with Image.open(image_path) as image:
      resized = ImageOps.contain(image, (int(screen_width / 2), int(screen_height / 2)))

      tkimg = ImageTk.PhotoImage(resized)
      Label(input_frame, image=tkimg).pack()

    with Image.open(out_image_path) as out_image:
      resized = ImageOps.contain(out_image, (int(screen_width / 2), int(screen_height / 2)))

      tkimg = ImageTk.PhotoImage(resized)
      Label(output_frame, image=tkimg).pack()

    self.mainloop()

if __name__ == '__main__':
  App()
