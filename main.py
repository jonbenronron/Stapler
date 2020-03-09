"""
    Program:    Stapler - Simple Pdf File Editor
    Author:     Roni Keuru
    Licence:    Open source GNU General Public License v3.0
    Date:       8.3.2020
"""

################
#   IMPORTS    #
################

# Standard library imports
import sys  # System
import os   # Operating system
import tkinter as tk    # Tkinter ~ Pythons standard GUI package

from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Try to import PyPDF2
try:
    # Update PyPDF2 package
    if os.name == "nt":
        command = "python -m pip install pypdf2 --upgrade"
    else:
        command = "pip install pypdf2 --upgrade"

    os.system(command)

    from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

# If PyPDF2 is not installed
except ImportError:

    # Command to install and/or upgrade pip (Python package index)
    command = "python -m ensurepip --upgrade"
    os.system(command)
    # Command to install PyPDF2
    command = "python -m pip install pypdf2"
    os.system(command)


#########################
#   GLOBAL VARIABLES    #
#########################

files = []  # List of pdf-files.
lsPages = []  # List of pages
index = 0  # Number of items in files list.

###############
#   CLASSES   #
###############

# Class for the Stapler application.


class Stapler(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()


# Class for pdf files.


class Pdf:

    def __init__(self, filepath=None, filename=None, pages=[]):
        self.filepath = filepath
        self.inputPdf = PdfFileReader(self.filepath, "rb")
        self.docInfo = self.inputPdf.getDocumentInfo()
        self.author = self.docInfo.author
        self.title = self.docInfo.title
        self.filename = filename
        self.numPages = self.inputPdf.getNumPages()
        self.pages = pages  # List of page objects

    @property
    def filepath(self):
        return self.path

    @property
    def filename(self):
        return self.name

    @property
    def pages(self):
        return self.pg

    @filepath.setter
    def filepath(self, filepath):
        self.path = filepath

    @filename.setter
    def filename(self, filename):
        if filename == None:
            name = os.path.basename(self.filepath)
            self.name = name.split(".")[0]
        else:
            self.name = filename

    @pages.setter
    def pages(self, pages):
        pages = []
        for p in range(self.numPages):
            pages.append(self.inputPdf.getPage(p))
        self.pg = pages


############
#   INIT   #
############

# Initializing a window for the app.
stapler = Stapler()
stapler.master.title("Stapler - Simple Pdf File Editor")
stapler.rowconfigure(1, minsize=600, weight=1)
stapler.columnconfigure(1, minsize=800, weight=1)

# Listbox widget to let user select usable pdf file items.
ls_files = tk.Listbox(master=stapler, activestyle='dotbox',
                      selectmode=tk.EXTENDED)

# Entry widget for naming the new pdf file.
lb_name = tk.Label(master=stapler, text="Pdf title")
pdfname = tk.StringVar(master=stapler)
ent_name = ttk.Entry(master=stapler, textvariable=pdfname)


#################
#   FUNCTIONS   #
#################

# Function for warning.

def message(type, title, message):
    if type == "info":
        messagebox.showinfo(title, message)
    elif type == "warning":
        messagebox.showwarning(title, message)
    elif type == "error":
        messagebox.showerror(title, message)
    elif type == "yesno":
        messagebox.askyesno(title, message)
    else:
        pass


# Function for import button.


def import_file():
    global files
    global index

    path = askopenfilename(
        filetypes=[("Pdf Files", "*.pdf"), ("All Files", "*.*")])
    pdf = Pdf(filepath=path)
    if not path:
        return
    files.append(pdf)
    print(files)
    ls_files.insert(index, pdf.filename)
    index += 1


# Function for delete button.


def delete_file():
    global files
    global index

    # List of selected items indices.
    selected_indices = list(ls_files.curselection())
    if len(selected_indices) == 0:
        return
    # Items have to be deleted in reversed order to avoid an IndexError.
    selected_indices.reverse()
    print(selected_indices)
    for i in selected_indices:
        print(i)
        ls_files.delete(i, last=None)
        del files[i]
        if index > 0:
            index -= 1


# Function for merge button.


def merge_files():
    global files
    global index
    global ent_name
    pdf_merge = PdfFileMerger()

    # Check if any files are selected on the listbox.
    if ls_files.curselection():
        # Check if title entry is empty.
        if ent_name.get() == "":
            # When empty give an error and return from merge function.
            message("error", "No title", "File has no title")
            return
        else:
            # When user has given a title for the new pdf file,
            # function will merge over selected items.
            selected_indices = list(ls_files.curselection())
            print(selected_indices)
            for i in selected_indices:
                file = files[i]
                pdf_merge.append(fileobj=file.filepath)

            # Check if user wants to keep old pdf files on the list.
            answer = message("yesno", "Keep old files?",
                             "Do you want to keep old pdf files?")
            if answer != True:
                # If not,
                # files will be removed in reversed order
                # to avoid any indexing errors.
                selected_indices.reverse()
                for i in selected_indices:
                    ls_files.delete(i, last=None)
                    del files[i]
                    if index > 0:
                        index -= 1

            try:
                # Try to remove previous temporary files.
                os.remove('temp.pdf')
            except OSError as e:
                # If no temporary files exists give an error.
                print("Error: %s - %s." % (e.filename, e.strerror))
            # Create a new pdf file into temporary form.
            with open('temp.pdf', 'wb') as temp:
                pdf_merge.write(temp)

            # Name of the new pdf file
            name = ent_name.get()
            pdf = Pdf('temp.pdf', name)
            files.append(pdf)
            ls_files.insert(index, pdf.filename)
            index += 1
    else:
        return


# Function for split button.


def split_file():
    global files
    global index
    global ls_files
    global lsPages
    global ent_name
    pdf_writer = PdfFileWriter()

    for p in lsPages:
        pdf_writer.addPage(p)

    try:
        # Try to remove previous temporary files.
        os.remove('temp.pdf')
    except OSError as e:
        # If no temporary files exists give an error.
        print("Error: %s - %s." % (e.filename, e.strerror))
    # Create a new pdf file into temporary form.
    with open('temp.pdf', 'wb') as temp:
        pdf_writer.write(temp)

    pdf = Pdf(filepath='temp.pdf', filename=ent_name)
    files.append(pdf)
    ls_files.insert(index, ent_name.get())
    index += 1


def split_window():
    global files
    global ls_files
    global lsPages

    # Tuple of selected files
    selected = ls_files.curselection()
    # Split only if one item is selected
    if selected and len(selected) == 1:
        if not ent_name.get():
            # When empty give an error and return from split_window function.
            message("error", "No title", "File has no title")
            return
        else:
            # Pick the file from 'selected' tuple
            file = files[selected[0]]
            pNum = file.numPages

            top = tk.Toplevel()
            top.title("Select pages")

            split_msg = str(
                "Choose a page or range of pages to be split from '" + file.filename + "' file.")
            msg = tk.Message(master=top, text=split_msg)
            msg.pack(side="top")

            page_in_list = tk.StringVar(master=top)
            page_list = tk.Listbox(master=top,
                                   height=10,
                                   selectmode=tk.EXTENDED,
                                   listvariable=page_in_list)
            scrollbar = tk.Scrollbar(master=top,
                                     orient="vertical")
            scrollbar.config(command=page_list.yview)
            scrollbar.pack(side="right",
                           fill="y")
            page_list.config(yscrollcommand=scrollbar.set)
            for i in range(pNum):
                page_list.insert(i, "page. " + str(i + 1))
            page_list.pack()

            def selPages():
                selected_pages = page_list.curselection()
                for p in selected_pages:
                    lsPages.append(file.pages[p])

            button = tk.Button(master=top,
                               text="Split")
            button.config(command=lambda: [f()
                                           for f in [selPages, split_file, top.destroy]])
            button.pack()

# Function for save button.


def save_file():
    global files
    global ls_files
    pdf_writer = PdfFileWriter()

    # Tuple of selected files
    selected = ls_files.curselection()
    # Save only if one item is selected
    if selected and len(selected) == 1:
        # Pick the file from 'selected' tuple
        file = files[selected[0]]
        # Ask user where the file is going to be saved
        filepath = asksaveasfilename(
            defaultextension="pdf",
            filetypes=[("Pdf Files", "*.pdf")],
        )
        # Add pages together from from the pdf object
        for page in file.pages:
            pdf_writer.addPage(page)
        if not filepath:
            return
        # Write out the pdf file
        with open(filepath, "wb") as output:
            pdf_writer.write(output)
        # Remove unnecessary temporary pdf files
        try:
            os.remove('temp.pdf')
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    else:
        return


########################
#   INIT FOR BUTTONS   #
########################

# Buttons are initialized here because they need functions
# to be defined.
fr_buttons = tk.Frame(master=stapler, relief=tk.RAISED, bd=2)
btn_import = tk.Button(master=fr_buttons,
                       text="Import",
                       command=import_file)
btn_delete = tk.Button(master=fr_buttons,
                       text="Delete",
                       command=delete_file)
btn_merge = tk.Button(master=fr_buttons,
                      text="Merge",
                      command=merge_files)
btn_split = tk.Button(master=fr_buttons,
                      text="Split",
                      command=split_window)
btn_save = tk.Button(master=fr_buttons,
                     text="Save",
                     command=save_file)


##################
#   THE LAYOUT   #
##################

# Position of widgets.
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

# Positions of the buttons.
btn_import.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_delete.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_merge.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_split.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

#################
#   MAIN LOOP   #
#################

stapler.mainloop()

#################
#   CLEAN UP    #
#################

try:
    # Any unsaved temporary files will be removed.
    os.remove('temp.pdf')
except OSError as e:
    # Temporary file does not exist.
    print("Error: %s - %s." % (e.filename, e.strerror))

# Exit the program.
exitMsg = "Thank you for using Stapler!"
quit(exitMsg)
