from Tkinter import *
import tkMessageBox
import socket
from checkAlgorithm import *
from tkFileDialog import *
import pygame
import os


class Login:
	def __init__ (self,parent):
		self.main = Toplevel(parent)
		self.parent = parent

		#Settings of titles, labels etc
		self.main.title("Login Box")
		self.main.geometry("200x225")
		self.main.resizable(width=FALSE, height=FALSE)

		#Username label and entry box
		Label(self.main,text="Username").pack()
		self.user = Entry(self.main)
		self.user.pack()

		#Password label and entry box
		Label(self.main,text="Password").pack()
		self.password = Entry(self.main,show="*")
		self.password.pack()

		#Username label and entry box
		Label(self.main,text="Opponent").pack()

		#Password label and entry box
		self.var = StringVar(self.main)
		self.var.set("srazak")
		opponent = OptionMenu(self.main, self.var,'sabithas', 'iron_clad', 'yasirama1', 'rohith2707', 'rayanS', 'ashleyevans', 'fatmat', 'umair', 'absy', 'zan18', 'omar-al-mukhtar', 'swegmaster132', 'sonic', 'DSOZ', 'milkshake', 'daanishalikhan','srazak').pack()
		# self.opponent = opponent.get(self.main)
		# self.opponent.pack()
		v = IntVar()
		b1 = Radiobutton(self.main, text="Red", variable=v, value=1).pack()

		b2 = Radiobutton(self.main, text="Black", variable=v, value=2).pack()





		#Login and quit button.
		Button(self.main,text="Login",command=lambda: online(self.getuser(),self.getpassword(),self.getopponent(),v.get())).pack()
		Button(self.main,text="Quit", command = self.quit).pack()

		#Close program
		self.main.protocol('WM_DELETE_WINDOW', self.deletekey)

	#quit function
	def quit(self):
		self.main.destroy()
		self.parent.destroy()
		
	#getuser from the Entry
	def getuser(self):
		return self.user.get()

	#getpassword from the Entry
	def getpassword(self):
		return self.password.get()

	#getopponent from the Entry
	def getopponent(self):
		return self.var.get()

	def deletekey(self):
		self.parent.destroy()
class optionwindow:
	def __init__(self,parent):
		self.main = Toplevel(parent)
		self.parent = parent

		#Settings of titles, labels etc
		self.main.title("Checkers by Umair")
		# self.main.geometry("200x100")
		# self.main.resizable(width=FALSE, height=FALSE)
		#self.frame = Frame(self.parent)
		#img = "checkers.gif"
		#background image
		#self.ck = PhotoImage(file="checkers.jpg")
		

		#Label background
		back = Canvas(self.main,width=640,height=512)
		back.pack()

		#back.create_image(0,0,image=self.ck,anchor="nw")
			
		#back.grid(row=1,column=1)

		#Labels for main window
		v = IntVar()

		b2 = Radiobutton(self.main, text="Two player Offline", variable=v, value=2)#.pack()
		b2.grid(row=1,column=3)
		buttonwindow2 =back.create_window(500,90,window=b2)




		# b3 = Radiobutton(self.main, text="Against Computer", variable=v, value=3)#.pack()
		# b3.grid(row=1,column=4)
		# buttonwindow3 =back.create_window(500,130,window=b3)
		#b3.pack()
		#Close program
		self.main.protocol('WM_DELETE_WINDOW', self.deletekey)

		#Login and quit button.
		bs = Button(self.main,text="Start",command=lambda: self.start(v.get()))
		bs.grid(row=1,column=5)
		buttonwindow4 =back.create_window(470,170,window=bs)
		#.pack()
		bq = Button(self.main,text="Quit", command = self.quit)#.pack()
		bq.grid(row=1,column=6)
		buttonwindow5 =back.create_window(530,170,window=bq)


	def deletekey(self):
		self.parent.destroy()

	def start(self,option):
		global loginwnd

		#Login Online
		if option == 1:
			loginwnd = Login(wnd)
			self.main.withdraw()

		
		elif option == 3:
			self.main.withdraw()
			import checkersAI
			theme.set_volume(0.1)
			
			

		#Offline Multiplayer
		elif option == 2:
			self.parent.deiconify()
			theme.set_volume(0.1)
			self.main.withdraw()


			
		



	def quit(self):
		self.main.destroy()
		self.parent.destroy()

	def withdraw(self):
		self.main.withdraw()

#Main window.
wnd = Tk()
wnd.title("ARGO")
#Height of the canvas
h = 600 
#Width of the canvas
w = 600
#Geometry of window
wnd.geometry(str(w+5)+"x"+str(h+100))
wnd.resizable(width=FALSE, height=FALSE)


#Options
option = optionwindow(wnd)


#Board creation on canvas

#withdraw window
wnd.withdraw()


wnd.mainloop()