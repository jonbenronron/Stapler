# Stapler
Application that allows user to merge (and split in future) pdf files with each other. <br/>

### Dependences
Pdf handling is done with PyPDF2. <br/>
GUI is done with tkinter. <br/>

### How to:
1. Download and install python 3 from [Python](https://www.python.org/), if not installed. <br/>
2. Download and put the Stapler to a directory of your choice. <br/>
3. Open command prompt and navigate to the directory that contains the main.py file. <br/>
4. Write following commands <br/>
  - `python -m pip install -U pip` (This upgrades the package manager [PyPi](https://pypi.org/)) <br/>
  - `python -m pip install tkinter` (This package is needed for general user interface [Tkinter](https://docs.python.org/3/library/tk.html)) <br/>
  - `python -m pip install pypdf2` (This package is needed to manipulate the pdf-files [PyPDF2](https://pypi.org/project/PyPDF2/)) <br/>
  - `python main.py` <br/>
5. Program should start working now. <br/>

### Notes:
Python package manager 'pip' should be installed already in newer versions of python.
At this point Stapler won't run without 'tkinter' and 'pypdf2' packages.

### Future plans:
- [X] Object oriented approach. (Working with this at the moment.)
- [ ] Split feature that allows user to split a page from pdf when needed.
- [ ] Make it executable stapler.exe (windows) and stapler.app (mac).

### Known bugs:
- [X] Unmerged pdf-files can't be saved. (OO-approach will probably fix this issue.)
- [ ] Saving has some issues.
- [ ] Pdf info is not transfered to the newly created pdf files.
