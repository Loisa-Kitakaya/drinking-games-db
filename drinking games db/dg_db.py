# This is a GUI application that stores the rules of various drinking games in a database and displays them on prompt.

# This application is built using the following modules and/or libraries: Tkinter | sqlite3

# Author Loisa Kitakaya

import os
import sqlite3
import tkinter
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.filedialog as fdialog
import tkinter.scrolledtext as scrolltextbox

# defining the database
sql = sqlite3.connect("dg.db")
cursor = sql.cursor()

# creating class Main_Window to define the properties of window GUI
class Main_Window:

	# auto initialize defining the properties (__init__)
	def __init__(self, master):

		# setting the window name
		master.title("Drinking Games ;-D")

		master.geometry("900x650")

		# setting the window icon
		icon = Image("photo", file="icon.png")
		master.tk.call('wm','iconphoto',GUI._w, icon)

		# creating the menu bar
		menu_bar = Menu(master)
		master.config(menu = menu_bar)

		# creating submenus
		sub_menu_1 = Menu(menu_bar)
		menu_bar.add_cascade(label = "Options", menu = sub_menu_1)
		# creating submenu commands
		sub_menu_1.add_command(label = "Quit app", command = master.destroy)

		# creating submenus
		sub_menu_2 = Menu(menu_bar)
		menu_bar.add_cascade(label = "Info", menu = sub_menu_2)
		# creating submenu commands
		sub_menu_2.add_command(label = "About", command = self.about)

		# creating the main frame frame
		frame_1 = Frame(master)

		# displaying the frame
		frame_1.pack(fill = "both", expand = 1)

		# creating subframes
		frame01 = Frame(frame_1)
		frame02 = Frame(frame_1)

		# displaying the sub-frames
		frame01.pack(side = TOP, fill = "both", padx=5, pady=5)
		frame02.pack(side = BOTTOM, fill = "both", expand = 1, padx=5, pady=5)

		# setting up the picture
		img = PhotoImage(file = "display_01.gif")   

		# creatung a canvas widget
		label_image = Label(frame01, image = img)   
		label_image.image = img

		# displaying the canvas
		label_image.pack(expand = 1, padx = 1, pady = 5)

		# creating entry fields
		text_box_1 = scrolltextbox.ScrolledText(frame02, bg = "white", wrap = WORD, relief=SUNKEN)

		# displaying the entry fields
		text_box_1.pack(fill = "both")

		# create an option box widget
		# defining the options
		game_options = ["Select game", "Most Likely", "Straight Face", "Drunken Artists", "Attached at the Hip", "Concoctions", "Cup Swap", "Buzz", "Avalanche", "Up and Down the River", "Cheers To The Governor"]

		# commands for the combobox options
		def read_from_DB():

			if "Most Likely" == variablez.get():

				# clearing the text box
				text_box_1.delete('1.0', END)

				# reading from the database
				cursor.execute("SELECT * FROM DrinkingGames WHERE Game = 'Most Likely'")

				data = cursor.fetchall()

				for row in data:

					instructions = row[1]

				# writing into the text box
				text_box_1.insert('1.0', instructions)

			elif "Straight Face" == variablez.get():

				# clearing the text box
				text_box_1.delete('1.0', END)

				# reading from the database
				cursor.execute("SELECT * FROM DrinkingGames WHERE Game = 'Straight Face'")

				data = cursor.fetchall()

				for row in data:

					instructions = row[1]

				# writing into the text box
				text_box_1.insert('1.0', instructions)

			elif "Drunken Artists" == variablez.get():

				# clearing the text box
				text_box_1.delete('1.0', END)

				# reading from the database
				cursor.execute("SELECT * FROM DrinkingGames WHERE Game = 'Drunken Artists'")

				data = cursor.fetchall()

				for row in data:

					instructions = row[1]

				# writing into the text box
				text_box_1.insert('1.0', instructions)

			elif "Attached at the Hip" == variablez.get():

				# clearing the text box
				text_box_1.delete('1.0', END)

				# reading from the database
				cursor.execute("SELECT * FROM DrinkingGames WHERE Game = 'Attached at the Hip'")

				data = cursor.fetchall()

				for row in data:

					instructions = row[1]

				# writing into the text box
				text_box_1.insert('1.0', instructions)

			elif "Concoctions" == variablez.get():

				# clearing the text box
				text_box_1.delete('1.0', END)

				# reading from the database
				cursor.execute("SELECT * FROM DrinkingGames WHERE Game = 'Concoctions'")

				data = cursor.fetchall()

				for row in data:

					instructions = row[1]

				# writing into the text box
				text_box_1.insert('1.0', instructions)

			elif "Cup Swap" == variablez.get():

				# clearing the text box
				text_box_1.delete('1.0', END)

				# reading from the database
				cursor.execute("SELECT * FROM DrinkingGames WHERE Game = 'Cup Swap'")

				data = cursor.fetchall()

				for row in data:

					instructions = row[1]

				# writing into the text box
				text_box_1.insert('1.0', instructions)

			elif "Buzz" == variablez.get():

				# clearing the text box
				text_box_1.delete('1.0', END)

				# reading from the database
				cursor.execute("SELECT * FROM DrinkingGames WHERE Game = 'Buzz'")

				data = cursor.fetchall()

				for row in data:

					instructions = row[1]

				# writing into the text box
				text_box_1.insert('1.0', instructions)

			elif "Avalanche" == variablez.get():

				# clearing the text box
				text_box_1.delete('1.0', END)

				# reading from the database
				cursor.execute("SELECT * FROM DrinkingGames WHERE Game = 'Avalanche'")

				data = cursor.fetchall()

				for row in data:

					instructions = row[1]

				# writing into the text box
				text_box_1.insert('1.0', instructions)

			elif "Up and Down the River" == variablez.get():

				# clearing the text box
				text_box_1.delete('1.0', END)

				# reading from the database
				cursor.execute("SELECT * FROM DrinkingGames WHERE Game = 'Up and Down the River'")

				data = cursor.fetchall()

				for row in data:

					instructions = row[1]

				# writing into the text box
				text_box_1.insert('1.0', instructions)

			elif "Cheers To The Governor" == variablez.get():

				# clearing the text box
				text_box_1.delete('1.0', END)

				# reading from the database
				cursor.execute("SELECT * FROM DrinkingGames WHERE Game = 'Cheers To The Governor'")

				data = cursor.fetchall()

				for row in data:

					instructions = row[1]

				# writing into the text box
				text_box_1.insert('1.0', instructions)

			else:

				# clearing the text box
				text_box_1.delete('1.0', END)

		variablez = StringVar()
		variablez.set(game_options[0]) # default value

		drop_down = OptionMenu(frame01, variablez, *game_options)

		# displaying the combobox
		drop_down.pack(side = LEFT, padx = 5)

		# creating buttons
		button_1 = Button(frame01, text = "Show", relief = RAISED, command = read_from_DB)

		# displaying the buttons
		button_1.pack(side = LEFT, padx = 5)

	# commands for "About"
	def about(self):

		# using messagebox
		tkinter.messagebox.showinfo("About Drinking Games 1.0", "*********** ABOUT *********** \n\nDrinking Games 1.0 is an application that shows you a number of games you and friends can play and have fun while drinking. \n\n********** AUTHOR ********** \n\nFreedom Loisa Kitakaya")

# creating the mainloop window and initializing it with class GUI_Window
GUI =Tk()

main_window = Main_Window(GUI)

GUI.mainloop()