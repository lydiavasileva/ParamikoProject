# ask_yes_no.py
from tkinter import messagebox

dialog_title = 'Entry Information'
dialog_text = "In the first entry box you type in the IP address "\
"of the networks device you want to connect to."\
'The format of the IP address shall look like the default,'\
' which have been shown in the entry box.\n'\
'__________________________________________________________________________\n'\
'The second entry box is where you type in the username for the account,'\
'which you are going to use for logging into the network device.\n'\
'__________________________________________________________________________\n'\
'The third entry box is where you type in the password for the account,'\
' which match the username you type in, in the second entry box.\n'\
'__________________________________________________________________________\n'\
'The fourth entry box is for the source path. This means where the config file,'\
' is stored on the network device. A path has been given as an example.\n'\
'___________________________________________________________________________\n'\
'The fifth entry box is for the destination path. This means where you want to'\
' save the config file on your computer. A path has been given as an example.'
messagebox.showinfo(dialog_title, dialog_text)
