# Stapler - Simple Pdf File Editor
Application that allows its user to merge (and in future split) pdf files with each other. <br/>

### Dependences
Pdf file manipulation is executed with [PyPDF2](https://pypi.org/project/PyPDF2/). <br/>
GUI (general user interface) is created with Tkinter. (Included in python standard library.) <br/>

### How to:
1. Download and install python 3 from [Python](https://www.python.org/), if it's not installed. <br/>
2. Download and put the Stapler to a directory of your choice. <br/>
3. Open command prompt and navigate to the directory that contains the `main.py` file. Example: <br/>
  - Windows: `cd C:/path/to/Stapler`
  - Mac/Linux: `cd root/absolute/path/to/Stapler`
4. Write following command: <br/>
  - `python main.py`
5. Program should start working now. <br/>

### Notes:
- Program will automatically ensure [pip](https://pypi.org/project/pip/) and install PyPDF2 package if it's not already installed on your computer.
In future this is not needed because executable version of application will include all packages you need to run it.

### Future plans:
- [X] Object oriented approach. (Working with this at the moment.)
- [ ] Split feature that allows user to copy a page or several pages from pdf file and creates a new pdf file from it or them.
- [ ] Make it executable stapler.exe (windows) and stapler.app (mac).
- [ ] Change file maintenance from list into sqlite3 data bases.

### Known bugs:
- [X] Unmerged pdf-files can't be saved. (OO-approach will probably fix this issue.)
- [X] Saving has some issues.
- [ ] Pdf info is not transfered to the newly created pdf files.
