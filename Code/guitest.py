import tkinter

class ShowInfoGui:
	def __init__(self):

		#Main window
		self.main_window = tkinter.Tk()

		#Set Window Default Size
		self.main_window.geometry('400x300')

		#Set Window Title
		self.main_window.wm_title("File Transfer Program")

		#Creating the three frames
		self.top_frame = tkinter.Frame(self.main_window)
		self.middle_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)

		#Variables that are user input
		self.ipAddr = tkinter.StringVar()
		self.usrN = tkinter.StringVar()
		self.usrP = tkinter.StringVar()
		self.destPath= tkinter.StringVar()
		self.sourPath = tkinter.StringVar()

		#Setting HeaderFrame with a HeaderLabel
		self.head_label = tkinter.Label(self.top_frame, text="File Transfer Program", font=(16))
		self.head_label.pack(side = "top", fill = "both")

		#Setting labels and entry widget for the different user inputs
		#Setting default entries
		self.ipAddr_label = tkinter.Label(self.middle_frame, text="IP Adress:").grid(row=0,column=0)

		self.ipAddr_entry = tkinter.Entry(self.middle_frame, bd =5)
		self.ipAddr_entry.grid(row=0, column=1)
		self.ipAddr_entry.insert(0, "10.0.0.0")

		self.usrN_label = tkinter.Label(self.middle_frame, text="Username:").grid(row=1, column=0)

		self.usrN_entry = tkinter.Entry(self.middle_frame, bd =5).grid(row=1, column=1)

		self.usrP_label = tkinter.Label(self.middle_frame, text="Password:").grid(row=2,column=0)
		self.usrP_entry = tkinter.Entry(self.middle_frame, bd =5).grid(row=2,column=1)

		self.destPath_label = tkinter.Label(self.middle_frame, text="Destination Path:").grid(row=3,column=0)
		self.destPath_entry = tkinter.Entry(self.middle_frame, bd =5).grid(row=3,column=1)

		self.sourPath_label = tkinter.Label(self.middle_frame, text="Source Path:").grid(row=4,column=0)
		self.sourPath_entry = tkinter.Entry(self.middle_frame, bd =5).grid(row=4,column=1)

		#Sets the button widgets
		#NEED TO ADD: FUNCTIONS FOR HELP AND CONNECT
		self.get_button = tkinter.Button(self.bottom_frame, text="Get", command=self.info).grid(row=0,column=0, pady=50)
		self.get_button = tkinter.Button(self.bottom_frame, text="Push", command=self.info).grid(row=0,column=1, pady=50)
		self.help_button = tkinter.Button(self.bottom_frame, text="Help", command=self.info).grid(row=0,column=2, pady=50)
		self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy).grid(row=0,column=3, pady=50)

		#Packing the frames
		self.top_frame.pack()
		self.middle_frame.pack()
		self.bottom_frame.pack()

		#Enter the tkinter main loop.
		tkinter.mainloop()

	# The info method is a callback function for
	# the show info button.
	def info(self):
		name = "Kenneth Helweg Hansen"
		address = "Ridderhatten 93B"
		city = "Odense SØ, 5220"

		self.name.set(name)
		self.addr.set(address)
		self.city.set(city)

showInfo = ShowInfoGui()
