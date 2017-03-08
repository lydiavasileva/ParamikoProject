import tkinter

class ShowInfoGui:
	def __init__(self):

		#Main window
		self.main_window = tkinter.Tk()

		#Creating the two frames
		self.top_frame = tkinter.Frame(self.main_window)
		self.middle_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)


		#Variables
		self.ipAddr = tkinter.StringVar()
		self.usrN = tkinter.StringVar()
		self.usrP = tkinter.StringVar()


		#Sets the frame where the info is shown
		self.head_label = tkinter.Label(self.top_frame, \
									text="Initial Connection") 
		self.head_label.pack(side = "left")
		

		self.ipAddr_label = tkinter.Label(self.middle_frame, \
									text="Ip Adress:").grid(row=0,column=0)

		self.ipAddr_entry = tkinter.Entry(self.middle_frame, \
									bd =5).grid(row=0,column=1)



		self.usrN_label = tkinter.Label(self.middle_frame, \
									text="Username:").grid(row=1,column=0)

		self.usrN_entry = tkinter.Entry(self.middle_frame, \
									bd =5).grid(row=1,column=1)


		self.usrP_label = tkinter.Label(self.middle_frame, \
									text="Password:").grid(row=2,column=0)
		

		self.usrP_entry = tkinter.Entry(self.middle_frame, \
									bd =5).grid(row=2,column=1)
		



		#Sets the frames for the buttons
		self.showInfo_button = tkinter.Button(self.bottom_frame, \
											text="Connect", \
											command=self.info)

		self.help_button = tkinter.Button(self.bottom_frame, \
										text="Help", \
										command=self.info)
		self.quit_button = tkinter.Button(self.bottom_frame, \
										text="Quit", \
										command=self.main_window.destroy)

		self.showInfo_button.pack(side="left")
		self.help_button.pack(side="left")
		self.quit_button.pack(side="left")



		self.top_frame.pack()
		self.middle_frame.pack()
		self.bottom_frame.pack()

		# Enter the tkinter main loop.
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
