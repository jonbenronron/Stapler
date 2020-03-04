# Stapler
Pdf merge app with simple GUI (work in progress).. <br/>
Pdf handling is done with PyPDF2. <br/>
GUI is done with tkinter. <br/>

How to:
1. Download and install python 3 from https://www.python.org/, if not installed. <br/>
2. Download and put the Stapler to a directory of your choice. <br/>
3. Open command prompt and navigate to the directory that contains the main.py file. <br/>
4. Write following commands <br/>
  - 'python -m pip install -U pip' (This upgrades the package manager https://pypi.org/) <br/>
  - 'python -m pip install tkinter' (This package is needed for general user interface https://docs.python.org/3/library/tk.html) <br/>
  - 'python -m pip install pypdf2' (This package is needed to manipulate the pdf-files https://pypi.org/project/PyPDF2/) <br/>
  - 'python main.py' <br/>
5. Program should start working now. <br/>

Notes:
Python package manager 'pip' should be installed already in newer versions of python.
At this point Stapler won't run without 'tkinter' and 'pypdf2' packages.
You could just download the main.py file at this point as long as there exists a temp directory
at same directory as the main.py is located. Of course you can create one yourself.
If program is not able to find one, it will give you an error message.

Future plans:
- Split feature that allows user to split a page from pdf when needed.
- Make it executable stapler.exe (windows) and stapler.app (mac).

Known bugs:
- Unmerged pdf-files can't be saved.
