# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:56:59 2022

@author: Dorian
"""

import os
import img2pdf
import webbrowser
#Import the Tkinter library
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo

# Create an instance of Tkinter frame
app = tk.Tk()
# Define the geometry
app.geometry("500x250")
app.resizable(False, False)
app.iconbitmap('./icon/icon.ico')
app.title('IMG2PDF')
app.grid()

# String Variable for Labels
name_folder = tk.StringVar()
name_pdf_file = tk.StringVar()
status_progress = tk.StringVar()

extensions = ('jpg','jpeg', 'bmp', 'png', 'gif')   # Add image formats here

def select_folder():
   path = filedialog.askdirectory(title="Select a Directory that contain images")
   name_folder.set(path)
   return path
   
def convert_to_pdf():
    # le folder doit contenir uniquement des images
    # if folder contient uniquement de images alors on peut commencer la conversion
    # else on écrit un message d'erreur

    DIR = name_folder.get()
    filename_ebook = name_pdf_file.get()
    
    if DIR :
        if filename_ebook :
            new_filename_ebook = filename_ebook.strip().replace(" ","_")
            
            pages = [os.path.join(DIR, name) for name in os.listdir(DIR) if name.endswith(extensions)]
            print(pages)
            if len(pages) > 0 :
                status_progress.set("In progress...")
                with open(DIR+"/"+new_filename_ebook+".pdf", "wb") as f :
                    f.write(img2pdf.convert(pages))
                
                showinfo("PDF Generated !", DIR+"/"+new_filename_ebook+".pdf generated")
                webbrowser.open(DIR+"/"+new_filename_ebook+".pdf")
                # reset
                status_progress.set("")
                name_folder.set("")
                name_pdf_file.set("")
                
            else :
                showinfo("Error", "Please choose a folder that contain images !")
        else :
            showinfo("Error", "Please enter a name for your pdf !")
    else :
        showinfo("Error", "Please choose a folder !")
    

#Create a label and a Button to Open the dialog
label_title = tk.Label(app, text="Convert and merge images to PDF", font=('Aerial 15 bold'))
label_title.grid(column=0, row=0, padx=30, pady=30)

# folder path
folder_label = ttk.Label(app, text="Folder Path :")
folder_label.grid(column=0, row=1, padx=30, sticky=tk.W)
folder_entry = ttk.Label(app, textvariable=name_folder, width=30)
folder_entry.grid(column=0, row=1, padx=30, sticky=tk.E)
button= ttk.Button(app, text="Select a folder", command=select_folder)
button.grid(column=1, row=1, sticky=tk.E)

# filename
filename_label = ttk.Label(app, text="Filename for your pdf :")
filename_label.grid(column=0, row=2, padx=30, sticky=tk.W)
filename_entry = ttk.Entry(app, textvariable=name_pdf_file)
filename_entry.grid(column=0, row=2, padx=30, sticky=tk.E)
filename_entry.focus()
filename_label = ttk.Label(app, text=".pdf")
filename_label.grid(column=1, row=2, sticky=tk.W)

# button convert
button_convert = ttk.Button(app, text="Convert2Pdf", command=convert_to_pdf)
button_convert.grid(column=0, row=3, pady=50)

# status converting
status_label = ttk.Label(app, textvariable=status_progress)
status_label.grid(column=0, row=3, sticky=tk.E)

app.mainloop()