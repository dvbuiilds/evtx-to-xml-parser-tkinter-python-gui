import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import subprocess
import os
import webbrowser
from pc_variables import browser_path_in_my_pc, url_path_for_browser


def Run_Button(file):
    dumppath = "evtx_dump.py"
    output_name = "Log_XMLs/" + os.path.basename(file)
    output_name = os.path.splitext(output_name)[0] + '.xml'
    f = open(output_name, "w", encoding = "utf-8")
    stout = subprocess.check_output(['python', dumppath, file])
    stout = stout.decode('utf-8')
    f.write(stout)
    f.close()
    return output_name


def open_xml(xmlfile):
    # Add browser location from the C drive below:
    browser_location = browser_path_in_my_pc
    pathadd = url_path_for_browser + xmlfile
    webbrowser.get(browser_location).open(pathadd)


def open_file():
    file= askopenfile(parent = root, mode='rb', title="Choose a file", initialdir="Logs/")
    xmlfile = None
    if file:
        file = str(file.name)
        xmlfile = Run_Button(file)
        open_xml(xmlfile)
    else:
        print("No file selected! Please select a file to parse.")


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Windows Event Log Parser')
    canvas = tk.Canvas(root, width=1000, height=600, background="#ffffff")
    canvas.grid(columnspan=3, rowspan=4)
 
    # Heading text
    heading = tk.Label(root, text="Windows Event Log Parsing with\nPython package python-evtx", font=("Poppins", 35, "bold"), fg='#3F3D56', background="#ffffff")
    heading.grid(columnspan=3, column=0, row = 0)
    
    # Logo
    logo = Image.open('icon.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image = logo, height=85, width=85, background="#ffffff")
    logo_label.image = logo
    logo_label.grid(column=1, row= 1)

    # Instructions
    instructions = tk.Label(root, text="Select a Windows Event File to Parse!", font = "Poppins", background="white")
    instructions.grid(columnspan=3, column=0, row = 2)

    # Browse Button
    browse_btn = tk.Button(root, text="Browse & Generate", command=lambda:open_file(), font = "Poppins", background = '#6C63FF', fg='#fff', width=15, padx=25, pady=5)
    browse_btn.grid(column=1, rowspan = 2, row=2)
    root.mainloop()