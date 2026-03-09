from tkinter import *
from PIL import Image
import pytesseract

def convert():
    img = Image.open("scribble.jpg")
    text = pytesseract.image_to_string(img)
    result.insert(END,text)

root = Tk()
root.title("Scribble to Digital")

btn = Button(root,text="Convert",command=convert)
btn.pack()

result = Text(root,height=15,width=50)
result.pack()

root.mainloop()