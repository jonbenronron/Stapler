#   Author:     Roni Keuru
#   Licence:    Open source GNU General Public License v3.0
#   Date:       4.3.2020

#################
#   PACKAGES    #
#################

import os
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

#########################
#   GLOBAL VARIABLES    #
#########################

files = []  # List of pdf-files.
index = 0  # Number of items in files list.

#################
#   Classes     #
#################


class Pdf:

    def __init__(self, state="load", filepath=None, filename=None, pages=[]):
        self.state = state
        self.filepath = filepath
        self.inputPdf = PdfFileReader(self.filepath, "rb")
        self.docInfo = inputPdf.getDocumentInfo()
        self.author = docInfo.author
        self.title = docInfo.title
        self.fileName = fileName
        self.numPages = self.inputPdf.getNumPages()
        self.pages = pages  # List of page objects

    @property
    def filepath(self):
        return self.filepath

    @property
    def fileName(self):
        return self.fileName

    @property
    def pages(self):
        return self.pages

    @filepath.setter
    def filepath(self, value):
        if self.state == "load":
            self.filepath = askopenfilename(
                filetypes=[("Pdf Files", "*.pdf"), ("All Files", "*.*")])

    @fileName.setter
    def fileName(self, value):
        directories = self.filepath.split("/")
        file_name = directories[len(directories) - 1].split(".")
        name = file_name[0]

    @pages.setter
    def pages(self, value):
        self.pages = []
        for p in range(self.numPages):
            self.pages.append(self.inputPdf.getPage(p))


#############
#   Init    #
#############

pdf_merge = PdfFileMerger()  # Not sure if I keep this here.

#   Initializing a window for the app.
window = tk.Tk()
window.title("Stapler - A pdf-file merger")
window.rowconfigure(1, minsize=600, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

#   List widget.
ls_files = tk.Listbox(master=window, activestyle='dotbox',
                      selectmode=tk.EXTENDED)

#   Entry for naming the pdf.
lb_name = tk.Label(master=window, text="Pdf title")
pdfname = tk.StringVar(master=window)
ent_name = ttk.Entry(master=window, textvariable=pdfname)


#################
#   Functions   #
#################

#   Function for import button


def import_file():

    global files
    global index
    pdf = Pdf()

    if not pdf.filepath:
        return

    files.append((pdf.fileName, pdf))
    print(files)

    ls_files.insert(index, name)
    ls_files.activate(index)
    index += 1


#   Function for delete button


def delete_file():
    # List of selected items indices
    selected_indices = list(ls_files.curselection())
    # Items has to be deleted in reversed order to avoid an IndexError
    selected_indices.reverse()
    print(selected_indices)
    for i in selected_indices:
        print(i)
        ls_files.delete(i, last=None)
        del files[i]
        global index
        if index > 0:
            index -= 1


#   Function for merge button


def merge_files():
    global index
    global pdf_merge
    if ls_files.curselection():
        if ent_name.get() == "":
            print("File has no title.")
            return
        else:
            selected_indices = list(ls_files.curselection())
            print(selected_indices)
            for i in selected_indices:
                global files
                f = files[i][1]
                print(f)
                pdf_merge.append(fileobj=f)
            selected_indices.reverse()
            for i in selected_indices:
                ls_files.delete(i, last=None)
                del files[i]
                if index > 0:
                    index -= 1
            name = ent_name.get()
            try:
                os.remove('temp/temp.pdf')
            except OSError as e:
                print("Error: %s - %s." % (e.filename, e.strerror))
            with open('temp/temp.pdf', 'wb') as temp:
                pdf_merge.write(temp)
            file = PdfFileReader('temp/temp.pdf')
            pdf = [name, file]
            files.append(pdf)
            ls_files.insert(index, name)
            ls_files.activate(index)
            index += 1
    else:
        return


#   Function for save button


def save_file():
    global pdf_merge
    if ls_files.curselection() and len(ls_files.curselection()) == 1:
        filepath = asksaveasfilename(
            defaultextension="pdf",
            filetypes=[("Pdf Files", "*.pdf")],
        )
        if not filepath:
            return
        with open(filepath, "wb") as output:
            pdf_merge.write(output)
        try:
            os.remove('temp/temp.pdf')
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    else:
        return


#########################
#   Init for buttons    #
#########################

#   Buttons are initialized here because they need functions to be defined
fr_buttons = tk.Frame(master=window, relief=tk.RAISED, bd=2)
btn_import = tk.Button(master=fr_buttons,
                       text="Import",
                       command=import_file)
btn_delete = tk.Button(master=fr_buttons,
                       text="Delete",
                       command=delete_file)
btn_merge = tk.Button(master=fr_buttons,
                      text="Merge",
                      command=merge_files)
btn_save = tk.Button(master=fr_buttons,
                     text="Save",
                     command=save_file)

#   Positions of the buttons
btn_import.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_delete.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_merge.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

#   The layout of the program
fr_buttons.grid(row=1, column=0,
                rowspan=1, columnspan=1,
                sticky="nesw")
ls_files.grid(row=1, column=1,
              rowspan=1, columnspan=2,
              sticky="nesw")
lb_name.grid(row=0, column=0,
             rowspan=1, columnspan=1,
             sticky="nesw")
ent_name.grid(row=0, column=1,
              rowspan=1, columnspan=2,
              sticky="nesw")

#################
#   Main loop   #
#################

window.mainloop()

#################
#   Clean up    #
#################

try:
    os.remove('temp/temp.pdf')  # Any temporary files has to be removed
except OSError as e:
    # temp directory is empty or does not exist
    print("Error: %s - %s." % (e.filename, e.strerror))
