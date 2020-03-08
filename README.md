# Stapler
Application that allows user to merge (and split in future) pdf files with each other. <br/>

### Dependences
Pdf handling is done with PyPDF2. <br/>
GUI is done with tkinter. (Included in python standard library.) <br/>

### How to:
1. Download and install python 3 from [Python](https://www.python.org/), if not installed. <br/>
2. Download and put the Stapler to a directory of your choice. <br/>
3. Open command prompt and navigate to the directory that contains the `main.py` file. Example: <br/>
  - Windows: `cd C:/path/to/Stapler`
  - Mac/Linux: `cd root/path/to/Stapler`
4. Write following command: <br/>
  - `python main.py`
5. Program should start working now. <br/>

### Notes:
- Program will ensure [pip](https://pypi.org/project/pip/) and automaticly install [PyPDF2](https://pypi.org/project/PyPDF2/) package if it's not already installed.
In future this is not needed because executable version of application will include all packages you need to run it.

### Future plans:
- [X] Object oriented approach. (Working with this at the moment.)
- [ ] Split feature that allows user to split a page from pdf when needed.
- [ ] Make it executable stapler.exe (windows) and stapler.app (mac).
- [ ] Change file handling into sqlite data bases.

### Known bugs:
- [X] Unmerged pdf-files can't be saved. (OO-approach will probably fix this issue.)
- [X] Saving has some issues.
- [ ] Pdf info is not transfered to the newly created pdf files.
