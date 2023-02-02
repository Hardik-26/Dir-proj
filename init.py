# Imports-
import os
import re
import pandas as pd
import tkinter as tk
from tkinter import * 
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import time

# GUI----------------------------------------------------

def browse_folder():
    global folder_get
    folder_get.set(filedialog.askdirectory())

def submit():
    global folder_get,folder_path
    folder_path=folder_get.get()
    root.destroy()

# Main Window-
root = tk.Tk()
root.geometry("275x125")
root.title("Select Folder")

# Folder Path-
folder_get = tk.StringVar()
folder_path_entry = tk.Entry(root, textvariable=folder_get)
folder_path_entry.place(x=95,y=29)
lbl = Label(root, text = "Select Folder: ",font = ("Arial Bold",10)).place(x=5,y=29)

# Browse button-
file_icon =  PhotoImage(file = "IOC.png")
browse_button = tk.Button(root, text="Browse",image = file_icon ,command=browse_folder)
browse_button.place(x=230, y=25)
# Submit button
submit_button = tk.Button(root, text="Submit",font = ("Arial Bold",10),command=submit).place(x=110,y=60)

root.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------

# Main----------------------------------

#get dir list
file_list=os.scandir(folder_path)

main_dict=dict()
for i in file_list:
    if i.is_dir():
        continue
    cur_file=i.name[11:13]
    try:
        main_dict[cur_file]=main_dict[cur_file]+1
    except KeyError:
        main_dict[cur_file]=1

print(main_dict)