from Tkinter import *
import tkMessageBox
from humanmove import *
from tkFileDialog import *
import computermove
import pygame
import os
from checkAlgorithmAI import *

#This function draws the board.
def drawboard (b):
	#Draws the first color boxes on the canvas. (red)
	for k in range(0,n):
			if k%2 == 0:
					start = 0
			else:
					start = w/n
			for i in range(start,w,2*w/n):
					b.create_rectangle(i, k*(w/n), i+(w/n), (k+1)*(w/n), outline=outline, fill=col1)

	#Draws the second color boxes on the canvas. (black)
	for k in range(0,n):
			if k%2 == 0:
					start = w/n
			else:
					start = 0
			for i in range(start,w,2*w/n):
					b.create_rectangle(i, k*(w/n), i+(w/n), (k+1)*(w/n), outline=outline, fill=col2)

#Default positions for all the pieces.
def defaultpostion(b):
	#Red pieces
	for k in range(0,n/2-1):
			if k%2 == 0:
					start = w/n
			else:
					start = 0
			for i in range(start,w,2*w/n):
					piece = b.create_oval(i+os, k*(w/n)+os, (i+(w/n))-os, ((k+1)*(w/n))-os, fill = "red", outline="white", width=2)
					pdict[str(i/(w/n))+str(k*(w/n)/(w/n))] = piece
					red.append(str((i+os)/(w/n))+str((k*(w/n)+os)/(w/n)))
					pos.append([(i/(w/n)), (k*(w/n)/(w/n))])

	

	#Black Pieces
	for k in range(n/2+1,n):
			if k%2 == 0:
					start = w/n
			else:
					start = 0
			for i in range(start,w,2*w/n):
					piece = b.create_oval(i+os, k*(w/n)+os, (i+(w/n))-os, ((k+1)*(w/n))-os, fill = "black", outline="white", width=2)
					pdict[str(i/(w/n))+str(k*(w/n)/(w/n))] = piece
					black.append(str((i+os)/(w/n))+str((k*(w/n)+os)/(w/n)))
					pos.append([i/(w/n), k*(w/n)/(w/n)])


#When you click the "Restart" Button, this functions clears all the lists and puts everything in the default starting position.
def startpositions(b):
	global g1,g2,g3,g4,g5,o1,o2,o3,pos,red,black,kingr,kingb,move,x,y,pdict

	n = 8

	b.delete(g1)
	b.delete(g2)
	b.delete(g3)
	b.delete(g4)
	b.delete(g5)

	move = "Human"
	updatelabel(move)
	black = []
	red = []
	kingr = []
	kingb = []
	pos = []

	pdict.clear()

	#Draws the board
	drawboard(b)

	#The default positions
	defaultpostion(b)

#This function checks for the winner.
def checkwinner():
	global g1,g2,g3,g4,g5,o1,o2,o3,pos,red,black,kingr,kingb,move,x,y
	n = 8
	# print "checking"
	if (red == [] and kingr == []):
		win = "HUMAN IS THE WINNER!"
		updatelabel(win)
	elif (black == [] and kingb == []):
		win = "COMPUTER IS THE WINNER!"
		updatelabel(win)

#This function enables the red king to capture. 
def redkingcapture(x,y,x2,y2,key,keymoved):
	global move,wosh,kingb,kingr,king,g1,g2,g3,g4,g5
	n = 8

	#The position where the black piece will lie.
	xp = (x+x2)/2
	yp = (y+y2)/2

	#The position to which the piece will be moved to.
	keymoved = str(x2)+str(y2)
	remove = str(xp)+str(yp)
	pos.remove([x,y])
	pos.append([x2,y2])
	pos.remove([xp,yp])
	kingr.remove(str(x)+str(y))
	kingr.append(keymoved)

	#If the king is being captured, the king will be deleted from the list, else the normal black piece will be.
	if remove in kingb:
		kingb.remove(remove)
	elif remove in black:
		black.remove(remove)

	

	#Draws the king on the new position.
	kingpiece = b.create_oval(x2*(w/n)+os, y2*(w/n)+os, x2*(w/n)+w/n-os, y2*(w/n)+w/n-os, fill = "red", outline="yellow", width=4,dash = (3,5))
	value = pdict[key]
	del pdict[key]
	b.delete(value)
	pdict[keymoved] = kingpiece
	premove = pdict[remove]
	b.delete(premove)

	#This sound is played when something is captured.
	wosh.play()

	#Delete all the green squares that were drawn.
	b.delete(g1)
	b.delete(g2)
	b.delete(g3)
	b.delete(g4)
	b.delete(g5)

	#If from the capturing position there is no capture, the move will switch, else the move will stay the same.
	if checkcapture(keymoved,True,pos,red,black,kingr,kingb,move,n) == False:
		move = "Human"
		updatelabel(move)
	else:
		move = "Computer"


#This function enables the black king to capture. 
def blackkingcapture(x,y,x2,y2,key,keymoved):
	global move,wosh,kingb,kingr,king,g1,g2,g3,g4,g5
	n = 8

	#The position where the red piece will lie.
	xp = (x+x2)/2
	yp = (y+y2)/2

	#The position where the piece has been moved.
	keymoved = str(x2)+str(y2)
	remove = str(xp)+str(yp)
	pos.remove([x,y])
	pos.append([x2,y2])
	pos.remove([xp,yp])
	kingb.remove(str(x)+str(y))
	kingb.append(keymoved)

	#If the red king is captured, red king will be removed from the list, else the normal piece will be removed from the list.
	if remove in kingr:
		kingr.remove(remove)
	elif remove in red:
		red.remove(remove)

	

	#Drawing the king after the capture.
	kingpiece = b.create_oval(x2*(w/n)+os, y2*(w/n)+os, x2*(w/n)+w/n-os, y2*(w/n)+w/n-os, fill = "black", outline="yellow", width=4, dash = (3,5))
	value = pdict[key]
	del pdict[key]
	b.delete(value)
	pdict[keymoved] = kingpiece
	premove = pdict[remove]
	b.delete(premove)

	#The sound played for capture.
	wosh.play()


	#Deleting the green squares that are drawn.
	b.delete(g1)
	b.delete(g2)
	b.delete(g3)
	b.delete(g4)
	b.delete(g5)

	#If there is no capture from the position, the move will switch, else if will remain the same.
	if checkcapture(keymoved,True,pos,red,black,kingr,kingb,move,n) == False:
		move = "Computer"
		updatelabel(move)
	else:
		move = "Human"

#This function enables the black piece to capture. 
def blackcapture(x,y,x2,y2,key,keymoved):
	global move,wosh,kingb,kingr,king,g1,g2,g3,g4,g5

	n = 8

	
	xp = (x+x2)/2
	yp = (y+y2)/2



	remove = str(xp)+str(yp)
	pos.remove([x,y])
	pos.append([x2,y2])

	pos.remove([xp,yp])
	

	if remove in kingr:
		kingr.remove(str(xp)+str(yp))
	elif remove in red:
		red.remove(str(xp)+str(yp))

	keymoved = str(x2)+str(y2)

	#Making king after capture
	if y2 == 0 and keymoved not in kingb:
		kingpiece = b.create_oval(x2*(w/n)+os, y2*(w/n)+os, x2*(w/n)+w/n-os, y2*(w/n)+w/n-os, fill = "black", outline="yellow", width=4, dash = (3,5))
		value = pdict[key]
		del pdict[key]
		b.delete(value)
		pdict[keymoved] = kingpiece
		premove = pdict[remove]
		b.delete(premove)
		black.remove(str(x)+str(y))
		kingb.append(str(x2)+str(y2))
		king.play()
	#Normal capture
	else:
		black.remove(str(x)+str(y))
		black.append(str(x2)+str(y2))
		newpiece = b.create_oval(x2*(w/n)+os, y2*(w/n)+os, x2*(w/n)+w/n-os, y2*(w/n)+w/n-os, fill = "black", outline="white", width=2)
		value = pdict[key]
		del pdict[key]
		b.delete(value)
		pdict[keymoved] = newpiece
		premove = pdict[remove]
		b.delete(premove)
		wosh.play()

	b.delete(g1)
	b.delete(g2)
	b.delete(g3)
	b.delete(g4)
	b.delete(g5)

	#Check whether a capture is available after the move.
	if checkcapture(keymoved,True,pos,red,black,kingr,kingb,move,n) == False:
		move = "Computer"
		updatelabel(move)
	else:
		move = "Human"

#This function enables the red piece to capture. 
def redcapture(x,y,x2,y2,key,keymoved):
	global move,wosh,king,kingb,kingr,g1,g2,g3,g4,g5
	n = 8
	xp = (x+x2)/2
	yp = (y+y2)/2

	remove = str(xp)+str(yp)

	try:
		pos.remove([x,y])
	except ValueError:
			updatelabel("COMPUTER IS THE WINNER")
	pos.append([x2,y2])
	

	pos.remove([xp,yp])
	

	if remove in kingb:
		kingb.remove(str(xp)+str(yp))
	elif remove in black:
		black.remove(str(xp)+str(yp))

	keymoved = str(x2)+str(y2)


	#Red King
	if y2 == n-1 and keymoved not in kingr:
		# print "King made after capture"
		kingpiece = b.create_oval(x2*(w/n)+os, y2*(w/n)+os, x2*(w/n)+w/n-os, y2*(w/n)+w/n-os, fill = "red", outline="yellow", width=4,dash = (3,5))
		value = pdict[key]
		del pdict[key]
		b.delete(value)
		pdict[keymoved] = kingpiece
		premove = pdict[remove]
		b.delete(premove)
		red.remove(str(x)+str(y))
		kingr.append(str(x2)+str(y2))
		king.play()
	else:
		red.remove(str(x)+str(y))
		red.append(str(x2)+str(y2))
		newpiece = b.create_oval(x2*(w/n)+os, y2*(w/n)+os, x2*(w/n)+w/n-os, y2*(w/n)+w/n-os, fill = "red", outline="white", width=2)
		value = pdict[key]
		del pdict[key]
		b.delete(value)

		pdict[keymoved] = newpiece
		premove = pdict[remove]
		b.delete(premove)
		wosh.play()

	b.delete(g1)
	b.delete(g2)
	b.delete(g3)
	b.delete(g4)
	b.delete(g5)

	if checkcapture(keymoved,True,pos,red,black,kingr,kingb,move,n) == False:
		move = "Human"
		updatelabel(move)
	else:
		move = "Computer"

#Updates the label.
def updatelabel(move):
	global moveLabel


	if move == "COMPUTER IS THE WINNER!":
		m.config(text=move)
		m.config(bg="green")

	elif move == "HUMAN IS THE WINNER!":
		m.config(text=move)
		m.config(bg="green")

	else:
		m.config(text=move +"'s move")
		m.config(bg="white")

def dropcomputer(x,y,x2,y2):
	global pos,move,g1,g2,g3,g4,g5,o1,o2,o3,red,black,kingr,kingb,b,capture,tick,keymoved

	
	n = 8
	key = str(x)+str(y)
	keymoved = str(x2)+str(y2)



	#Normal Move Red
	if move == "Computer" and [x2,y2] not in pos and key in red and (x2 == x+1 or x2 == x -1) and (y2 ==y+1):

		try:
			pos.remove([x,y])
		except ValueError:
			updatelabel("HUMAN IS THE WINNER")

		pos.append([x2,y2])


		if y2 == n-1:
			# print "King made after normal move"
			kingpiece = b.create_oval(x2*(w/n)+os, y2*(w/n)+os, x2*(w/n)+w/n-os, y2*(w/n)+w/n-os, fill = "red", outline="yellow", width=4,dash = (3,5))
			value = pdict[key]
			del pdict[key]
			b.delete(value)
			pdict[keymoved] = kingpiece
			if key in red:
				red.remove(key)
				king.play()
			else:
				kingr.remove(key)
				tick.play()
			kingr.append(str(x2)+str(y2))
			

		else:
			red.remove(str(x)+str(y))
			red.append(str(x2)+str(y2))
			newpiece = b.create_oval(x2*(w/n)+os, y2*(w/n)+os, x2*(w/n)+w/n-os, y2*(w/n)+w/n-os, fill = "red", outline="white", width=2)
			value = pdict[key]
			del pdict[key]
			b.delete(value)
			pdict[keymoved] = newpiece
			tick.play()


		
		move = "Human"
		updatelabel(move)


		b.delete(g1)
		b.delete(g2)
		b.delete(g3)
		b.delete(g4)
		b.delete(g5)	
	#Red capture move
	elif move == "Computer" and [x2,y2] not in pos and key in red and (x2 == x+2 or x2 == x -2) and (y2 ==y+2):

		redcapture(x,y,x2,y2,key,keymoved)





	#Red King normal move
	elif move == "Computer" and key in kingr and (x2 == x+1 or x2 == x -1) and (y2 ==y+1 or y2 == y-1):

		pos.remove([x,y])
		pos.append([x2,y2])
		kingr.remove(str(x)+str(y))
		kingr.append(str(x2)+str(y2))

		kingpiece = b.create_oval(x2*(w/n)+os, y2*(w/n)+os, x2*(w/n)+w/n-os, y2*(w/n)+w/n-os, fill = "red", outline="yellow", width=4,dash = (3,5))
		value = pdict[key]
		del pdict[key]
		b.delete(value)
		pdict[keymoved] = kingpiece
		tick.play()

		move = "Human"
		updatelabel(move)


		b.delete(g1)
		b.delete(g2)
		b.delete(g3)
		b.delete(g4)
		b.delete(g5)
	#Red king capture
	elif move == "Computer" and [x2,y2] not in pos and (x2 == x+2 or x2 == x-2) and (y2==y-2 or y2 == y+2) and key in kingr:
		redkingcapture(x,y,x2,y2,key,keymoved)	

	checkwinner()

#When you drop a piece.
def drop(event):
	global pos,x,y,move,g1,g2,g3,g4,g5,o1,o2,o3,red,black,kingr,kingb,b,capture,tick,n,keymoved

	x2 = ((event.x)/(w/n))
	y2 = ((event.y)/(w/n))

	key = str(x)+str(y)
	keymoved = str(x2)+str(y2)
	keyyp = str((x2+x)/2)+str((y2+y)/2)

	#The capture
	capture = checkcapture(keymoved,False,pos,red,black,kingr,kingb,move,n)







	#Nomal Move Black
	if capture == False and move == "Human" and [x2,y2] not in pos and key in black and (x2 == x+1 or x2 == x-1) and (y2==y-1):
		
		pos.remove([x,y])
		pos.append([x2,y2])
		

		if y2 == 0:
			# print "King made after normal move"
			kingpiece = b.create_oval(x2*(w/n)+os, y2*(w/n)+os, x2*(w/n)+w/n-os, y2*(w/n)+w/n-os, fill = "black", outline="yellow", width=4, dash = (3,5))
			value = pdict[key]
			del pdict[key]
			b.delete(value)
			pdict[keymoved] = kingpiece

			if key in black:
				black.remove(key)
				king.play()
			else:
				kingb.remove(key)
				tick.play()
			kingb.append(str(x2)+str(y2))
			


		else:
			black.remove(str(x)+str(y))
			black.append(str(x2)+str(y2))
			newpiece = b.create_oval(x2*(w/n)+os, y2*(w/n)+os, x2*(w/n)+w/n-os, y2*(w/n)+w/n-os, fill = "black", outline="white", width=2)
			value = pdict[key]
			del pdict[key]
			b.delete(value)
			pdict[keymoved] = newpiece
			tick.play()

	
		move = "Computer"
		updatelabel(move)

		b.delete(g1)
		b.delete(g2)
		b.delete(g3)
		b.delete(g4)
		b.delete(g5)

	#Black Capture move black
	elif capture == True and move == "Human" and [x2,y2] not in pos and key in black and (x2 == x+2 or x2 == x-2) and (y2==y-2) and (keyyp in red or kingr):
		blackcapture(x,y,x2,y2,key,keymoved)	

	elif capture == False and move == "Human" and key in kingb and (x2 == x+1 or x2 == x -1) and (y2 ==y+1 or y2 == y-1):

		pos.remove([x,y])
		pos.append([x2,y2])
		kingb.remove(str(x)+str(y))
		kingb.append(str(x2)+str(y2))

		kingpiece = b.create_oval(x2*(w/n)+os, y2*(w/n)+os, x2*(w/n)+w/n-os, y2*(w/n)+w/n-os, fill = "black", outline="yellow", width=4, dash = (3,5))
		value = pdict[key]
		del pdict[key]
		b.delete(value)
		pdict[keymoved] = kingpiece
		tick.play()

		move = "Computer"
		updatelabel(move)


		b.delete(g1)
		b.delete(g2)
		b.delete(g3)
		b.delete(g4)
		b.delete(g5)

	#Black king capture
	elif capture == True and move == "Human" and [x2,y2] not in pos and (x2 == x+2 or x2 == x -2) and (y2 ==y+2 or y2 == y-2) and key in kingb and (keyyp in red or kingr):
		blackkingcapture(x,y,x2,y2,key,keymoved)

	checkwinner()

#When you click a piece.
def click(event):
	global g1,g2,g3,g4,g5,o1,o2,o3,pos,red,black,kingr,kingb,move,x,y
	n = 8


	b.delete(g1)
	b.delete(g2)
	b.delete(g3)
	b.delete(g4)
	b.delete(g5)
	b.delete(o1)
	b.delete(o2)
	b.delete(o3)



	


	
	x = ((event.x)/(w/n))
	y = ((event.y)/(w/n))

	string = str(x)+str(y)


	#The capture
	capture = checkcapture(string,False,pos,red,black,kingr,kingb,move,n)

	cmove = computermove.checkcapture(string,capture,pos,red,black,kingr,kingb,move,n)

	if "random" not in cmove:
		dropcomputer(int(cmove[0]),int(cmove[1]),int(cmove[2]),int(cmove[3]))
	if "random" in cmove:
		dropcomputer(int(cmove[6]),int(cmove[7]),int(cmove[8]),int(cmove[9]))

	
	if move == "Human" and capture == False and ([x,y] in pos) and string in black and string not in kingb:
		g1 = b.create_rectangle(x*(w/n), y*(w/n), (x*(w/n))+(w/n), (y*(w/n))+(w/n), outline="SkyBlue1", fill=None, width = 3)	
		if ([x-1,y-1] not in pos) and x-1>=0 and y-1>=0:
			g2 = b.create_rectangle(x*(w/n)-(w/n), y*(w/n)-(w/n), (x*(w/n))+(w/n)-(w/n), (y*(w/n))+(w/n)-(w/n), outline=selected, fill=None, width = 3)
		if ([x+1,y-1] not in pos) and x+1 <n and y-1>=0: 
			g3 = b.create_rectangle(x*(w/n)+(w/n), y*(w/n)-(w/n), (x*(w/n))+(w/n)+(w/n), (y*(w/n))+(w/n)-(w/n), outline=selected, fill=None, width = 3)

	if move == "Human" and capture == True and ([x,y] in pos) and string in black:
		g1 = b.create_rectangle(x*(w/n), y*(w/n), (x*(w/n))+(w/n), (y*(w/n))+(w/n), outline="yellow", fill=None, width = 3)	
		if ([x-2,y-2] not in pos) and x-2>=0 and y-2>=0 and (str(x-1)+str(y-1) in red or str(x-1)+str(y-1) in kingr):
			g2 = b.create_rectangle(x*(w/n)-2*(w/n), y*(w/n)-2*(w/n), (x*(w/n))+(w/n)-2*(w/n), (y*(w/n))+(w/n)-2*(w/n), outline=selected, fill=None, width = 3)
		if ([x+2,y-2] not in pos) and x+2 <n and y-2>=0 and (str(x+1)+str(y-1) in red or str(x+1)+str(y-1) in kingr): 
			g3 = b.create_rectangle(x*(w/n)+2*(w/n), y*(w/n)-2*(w/n), (x*(w/n))+(w/n)+2*(w/n), (y*(w/n))+(w/n)-2*(w/n), outline=selected, fill=None, width = 3)
	
	if move == "Human" and capture == False and (string in kingb):
		g1 = b.create_rectangle(x*(w/n), y*(w/n), (x*(w/n))+(w/n), (y*(w/n))+(w/n), outline="blue", fill=None, width = 3)
		if ([x-1,y-1] not in pos) and x-1>=0 and y-1>=0:
			g2 = b.create_rectangle(x*(w/n)-(w/n), y*(w/n)-(w/n), (x*(w/n))+(w/n)-(w/n), (y*(w/n))+(w/n)-(w/n), outline=selected, fill=None, width = 3)
		if ([x+1,y-1] not in pos) and x+1 <n and y-1>=0: 
			g3 = b.create_rectangle(x*(w/n)+(w/n), y*(w/n)-(w/n), (x*(w/n))+(w/n)+(w/n), (y*(w/n))+(w/n)-(w/n), outline=selected, fill=None, width = 3)
		if ([x-1,y+1] not in pos) and x-1>=0 and y+1<n:
			g4 = b.create_rectangle(x*(w/n)-(w/n), y*(w/n)+(w/n), (x*(w/n))+(w/n)-(w/n), (y*(w/n))+(w/n)+(w/n), outline=selected, fill=None, width = 3)
		if ([x+1,y+1] not in pos) and x+1 <n and y+1 <n:
			g5 = b.create_rectangle(x*(w/n)+(w/n), y*(w/n)+(w/n), (x*(w/n))+(w/n)+(w/n), (y*(w/n))+(w/n)+(w/n), outline=selected, fill=None, width = 3)
		
	if move == "Human" and capture == True and (string in kingb):
		g1 = b.create_rectangle(x*(w/n), y*(w/n), (x*(w/n))+(w/n), (y*(w/n))+(w/n), outline="yellow", fill=None, width = 3)
		if ([x-2,y+2] not in pos) and x-2>=0 and y+2<n and (str(x-1)+str(y+1) in red or (str(x-1)+str(y+1) in kingr)):
			g2 = b.create_rectangle(x*(w/n)-2*(w/n), y*(w/n)+2*(w/n), (x*(w/n))+(w/n)-2*(w/n), (y*(w/n))+(w/n)+2*(w/n), outline=selected, fill=None, width = 3)
		if ([x+2,y+2] not in pos) and x+2 <n and y+2<n and (str(x+1)+str(y+1) in red or str(x+1)+str(y+1) in kingr): 
			g3 = b.create_rectangle(x*(w/n)+2*(w/n), y*(w/n)+2*(w/n), (x*(w/n))+(w/n)+2*(w/n), (y*(w/n))+(w/n)+2*(w/n), outline=selected, fill=None, width = 3)
		if ([x-2,y-2] not in pos) and x-2>=0 and y-2>=0 and (str(x-1)+str(y-1) in red or str(x-1)+str(y-1) in kingr):
			g4 = b.create_rectangle(x*(w/n)-2*(w/n), y*(w/n)-2*(w/n), (x*(w/n))+(w/n)-2*(w/n), (y*(w/n))+(w/n)-2*(w/n), outline=selected, fill=None, width = 3)
		if ([x+2,y-2] not in pos) and x+2 <n and y-2>=0 and (str(x+1)+str(y-1) in red or str(x+1)+str(y-1) in kingr): 
			g5 = b.create_rectangle(x*(w/n)+2*(w/n), y*(w/n)-2*(w/n), (x*(w/n))+(w/n)+2*(w/n), (y*(w/n))+(w/n)-2*(w/n), outline=selected, fill=None, width = 3)

#Main window.
window = Tk()
window.title("Checkers")
#Height of the canvas
h = 600 
#Width of the canvas
w = 600
#Geometry of window
window.geometry(str(w+5)+"x"+str(h+100))
window.resizable(width=FALSE, height=FALSE)

#Number of boxes in one row
n = 8
#First colour
col1 = "red" 
#Second colour
col2 = "black" 
#Outline of each box
outline = "black"
#Outline when selected
selected = "green"
#Offset for pieces

os = 8
#Pieces on board
pos = []
#pieces positions
black = []
red = []
#Red kings
kingr = []
#Black kings
kingb = []



#Capture bool
capture = False
# Move
move = "Human"

#dict
pdict = {}





#Default test case
keymoved = None

#Board creation on canvas
b = Canvas(window, width=w, height=h)
b.grid(row=2,column=1,columnspan=2)

#Move Label
m = Label(text=move+"'s move!")
m.grid(row=1,column=1,columnspan=2)

#Reset button
r = Button(text= "RESTART", command= lambda: startpositions(b))
r.grid(row=3, column=1,columnspan=2)



#Tip
t= Label(text="ATTENTION: Please drag the piece to the valid place!")
t.grid(row=4,column=1,columnspan=2)

#Tip
cfg= Label(text="Please click anywhere on the canvas for the computer to make a move.")
cfg.grid(row=5,column=1,columnspan=2)

#Draws the board
drawboard(b)

#The default positions
defaultpostion(b)




#Possible moves
g1 = b.create_rectangle(0, 0, w/n, w/n, outline=col2)
g2 = b.create_rectangle(0, 0, w/n, w/n, outline=col2)
g3 = b.create_rectangle(0, 0, w/n, w/n, outline=col2)
g4 = b.create_rectangle(0, 0, w/n, w/n, outline=col2)
g5 = b.create_rectangle(0, 0, w/n, w/n, outline=col2)

#Capture
o1 = b.create_rectangle(0, 0, w/n, w/n, outline=col2)
o2 = b.create_rectangle(0, 0, w/n, w/n, outline=col2)
o3 = b.create_rectangle(0, 0, w/n, w/n, outline=col2)





#Binding the click button.
b.bind("<Button-1>",click)

#Binding the release button.
b.bind("<ButtonRelease-1>",drop)






#The sounds for the game.
pygame.mixer.init()
theme = pygame.mixer.Sound("checkers.ogg")
theme.play(-1)
theme.set_volume(0.2)
tick = pygame.mixer.Sound("tick.ogg")
wosh = pygame.mixer.Sound("wosh.ogg")
king = pygame.mixer.Sound("king.ogg")



window.mainloop()