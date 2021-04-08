from tkinter import *
from tkinter import messagebox

root = Tk()
root.iconbitmap("TicTacToe.ico")
root.title("Tic Tac Toe by ULAN")
root.resizable(False, False)


# True >>> "X" and False >>>> "O"
click = True 
total = 0

# For CheckWin() We'll need it
btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

O = PhotoImage(file="O.png")
X = PhotoImage(file="X.png")


def play():
	button1 = Button(root, padx=75, pady=65, bd=3, relief="ridge", bg="#d7d9d7", textvariable=btn1, command=lambda: Click(1,0,0))
	button2 = Button(root, padx=75, pady=65, bd=3, relief="ridge",bg="#d7d9d7", textvariable=btn2, command=lambda: Click(2,0,1))
	button3 = Button(root, padx=75, pady=65, bd=3, relief="ridge",bg="#d7d9d7", textvariable=btn3, command=lambda: Click(3,0,2))
	button4 = Button(root, padx=75, pady=65, bd=3, relief="ridge",bg="#caccca", textvariable=btn4, command=lambda: Click(4,1,0))
	button5 = Button(root, padx=75, pady=65, bd=3, relief="ridge",bg="#caccca", textvariable=btn5, command=lambda: Click(5,1,1))
	button6 = Button(root, padx=75, pady=65, bd=3, relief="ridge",bg="#caccca", textvariable=btn6, command=lambda: Click(6,1,2))
	button7 = Button(root, padx=75, pady=65, bd=3, relief="ridge",bg="#a1a6a2", textvariable=btn7, command=lambda: Click(7,2,0))
	button8 = Button(root, padx=75, pady=65, bd=3, relief="ridge",bg="#a1a6a2", textvariable=btn8, command=lambda: Click(8,2,1))
	button9 = Button(root, padx=75, pady=65, bd=3, relief="ridge",bg="#a1a6a2", textvariable=btn9, command=lambda: Click(9,2,2))

	button1.grid(row=0, column=0)
	button2.grid(row=0, column=1)
	button3.grid(row=0, column=2)
	button4.grid(row=1, column=0)
	button5.grid(row=1, column=1)
	button6.grid(row=1, column=2)	
	button7.grid(row=2, column=0)
	button8.grid(row=2, column=1)
	button9.grid(row=2, column=2)


def Click(num,row,column):
	global click,total
	if click == True:
		label_image = Label(root, image=X)
		label_image.grid(row=row, column=column)
		if num == 1:
			btn1.set("X")
		if num == 2:
			btn2.set("X")
		if num == 3:
			btn3.set("X")
		if num == 4:
			btn4.set("X")
		if num == 5:
			btn5.set("X")
		if num == 6:
			btn6.set("X")
		if num == 7:
			btn7.set("X")
		if num == 8:
			btn8.set("X")
		if num == 9:
			btn9.set("X")
		total+=1
		click=False
		CheckWin()
	else:
		label_image = Label(root, image=O)
		label_image.grid(row=row, column=column)
		if num == 1:
			btn1.set("O")
		if num == 2:
			btn2.set("O")
		if num == 3:
			btn3.set("O")
		if num == 4:
			btn4.set("O")
		if num == 5:
			btn5.set("O")
		if num == 6:
			btn6.set("O")
		if num == 7:
			btn7.set("O")
		if num == 8:
			btn8.set("O")
		if num == 9:
			btn9.set("O")
		total+=1
		click=True
		CheckWin()

# ---------------------------------------------------- CheckWin() ---------------------------------------

def CheckWin():
	global click,total
	if ((btn1.get() == "X" and btn2.get() == "X" and btn3.get() == "X") or
		(btn4.get() == "X" and btn5.get() == "X" and btn6.get()== "X") or
		(btn7.get() == "X" and btn8.get() == "X" and btn9.get() == "X") or
		(btn1.get() == "X" and btn4.get() == "X" and btn7.get() == "X") or
		(btn2.get() == "X" and btn5.get() == "X" and btn8.get() == "X") or
		(btn3.get() == "X" and btn6.get() == "X" and btn9.get() == "X") or
		(btn1.get() == "X" and btn5.get() == "X" and btn9.get() == "X") or
		(btn3.get() == "X" and btn5.get() == "X" and btn7.get() == "X")):
		response = messagebox.askquestion("Tic Tac Toe", "Player X Wins!\nDo you want to play again?")
		if response == "no":
			quit()
		click = True
		total = 0
		clear()
		play()

	elif ((btn1.get() == "O" and btn2.get() == "O" and btn3.get() == "O") or
		(btn4.get() == "O" and btn5.get() == "O" and btn6.get() == "O") or
		(btn7.get() == "O" and btn8.get() == "O" and btn9.get() == "O") or
		(btn1.get() == "O" and btn4.get() == "O" and btn7.get() == "O") or
		(btn2.get() == "O" and btn5.get() == "O" and btn8.get() == "O") or
		(btn3.get() == "O" and btn6.get() == "O" and btn9.get() == "O") or
		(btn1.get() == "O" and btn5.get() == "O" and btn9.get() == "O") or
		(btn3.get() == "O" and btn5.get() == "O" and btn7.get() == "O")):
		response = messagebox.askquestion("Tic Tac Toe", "Player O Wins!\nDo you want to play again?")
		if response == "no":
			quit()
		click = True
		total = 0
		clear()
		play()

	elif total == 9:
		response = messagebox.askquestion("Tic Tac Toe", "Tie Game!\nDo you want to play again?")
		if response == "no":
			quit()
		click = True
		total = 0
		clear()
		play()

def clear():
	btn1.set("")
	btn2.set("")
	btn3.set("")
	btn4.set("")
	btn5.set("")
	btn6.set("")
	btn7.set("")
	btn8.set("")

play()

mainloop()