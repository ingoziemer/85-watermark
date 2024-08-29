import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
from functools import partial

# # -------------------------/ Watermark Implementation / -------------------------


def add_watermark():
    # open image
    image_path = filepath_entry.get()
    image = Image.open(image_path)
    watermark_image = image.copy()

    watermark = watermark_entry.get()
    # Add Font
    size = float(size_entry.get())
    font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', size=size)

    # Rotate image backwards
    watermark_image = watermark_image.rotate(315, expand=1)

    # point to print text from
    width, height = watermark_image.size
    _, _, wi, hi = font.getbbox(watermark)
    p_width = width/2 - wi
    p_height = height/2 - hi

    # Print into the rotated image
    d = ImageDraw.Draw(watermark_image)
    d.text((p_width, p_height), watermark, font=font, fill=(255, 255, 0))

    # Rotate it forward again
    watermark_image = watermark_image.rotate(-315, expand=1)
    watermark_image.show()


def upload_image(entry):
    # to do: specify filetypes
    filename = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(tk.END, filename)
    print('Selected:', filename)


window = Tk()

window.title("Watermarker")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

# Label
watermark_label = Label(text="Watermark text:")
watermark_label.grid(column=0, row=1)

size_label = Label(text="Choose Font Size:")
size_label.grid(column=0, row=2)

# Entries
filepath_entry = Entry(width=30)
filepath_entry.grid(column=1, row=0, sticky='e')

watermark_entry = Entry(width=30)
watermark_entry.grid(column=1, row=1)

size_entry = Entry(width=30)
size_entry.grid(column=1, row=2)

# Buttons
upload = Button(text="Upload Image", command=partial(upload_image, filepath_entry))
upload.grid(column=0, row=0)

add_watermark = Button(text="Add watermark to image", command=add_watermark)
add_watermark.grid(column=0, row=3, columnspan=2)


window.mainloop()

# optional to-do's to improve functionality:
# - restrict filetypes to images
# - let user choose color, transparency and angle of watermark
