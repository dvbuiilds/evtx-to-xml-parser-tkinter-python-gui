# Windows .evtx log file Parser GUI to generate XML

With the help of Python Tkinter package, We create a GUI Application that parses our .evtx file to .xml.


## Acknowledgements

I would like to mention that this project would not have been possible without the help of the below References. Thanks to all the content creators!
 - [python-evtx](https://github.com/williballenthin/python-evtx)
 - [Parsing Windows event log files (.evtx) using Python](https://www.alishaaneja.com/evtx/)
 - [Command line argument processing using argparse](https://www.youtube.com/watch?v=XYUXFR5FSxI)
 - [Windows Powershell](https://docs.microsoft.com/en-us/powershell/?view=powershell-7.1)
 - [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
 - [subprocess — Subprocess management](https://docs.python.org/3/library/subprocess.html#using-the-subprocess-module)

  Besides that, for doubt resolution, I was constantly surfing on Stackoverflow, Stackexchange, and Youtube.

The Logo/Image you will find in this project are downloaded from Wikipedia in .svg format and edited on Figma.


## Roadmap

- Basics of Event Log Files and .evtx entension.

- Installing Python and python-evtx package.

- Windows Powershell Commands

- ArgParse package in Python - Working.

- Implementing evtx_dump.py using Commands in Powershell.

- Learn to build a basic Tkinter GUI Application.

- Try subprocess module API of Python as well.

- Implement the parsing algorithm in Tkinter Application.

- Say "Thank You" to me :D

  
## Installation and Deployment

- First of all, Install Python using Microsoft Store or python.org

- Next, using 'pip' install 'python-evtx' package, to install Evtx and other related packages that will be used in evtx_dump.py file.

```bash
  pip install python-evtx
```
- Clone this repository.
- Run the App by simply double-clicking it or using the command:
```bash
  python app.py
```
- The .evtx file you will find in the project is just a sample .evtx file. You can view your own .evtx files by going to: C:\Windows\System32\winevt\Logs


## Documentation

argparse and Evtx package used in evtx_dump.py are used to parse the binary xml object extracted from .evtx file.

Methods used in [app.py]():
- open_file(): helps in placing an open file dialog box and saving the path of .evtx file selected.
- Run_button(): takes the file address as argument, uses subprocess API module to push the command into command prompt.  
- open_xml(): takes output xml file location as argument. Has two environment dependent variables that you would have to change. one is browser_location and other is pathadd. Add the location of your browswer.exe from Program Files into browser_location. Add the path address of Tkinter in your pc in pathadd.


## Support and Suggestions

For support or any suggestions, kindly email me at varshneydhairya4[at]gmail[dot]com or DM me on [Twitter](https://twitter.com/dv_twts) or [Linkedin](https://www.linkedin.com/in/dhairya-varshney/).