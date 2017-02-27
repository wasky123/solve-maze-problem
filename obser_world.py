from Tkinter import *
import maze_gen
import numpy as np
import time as tm
master = Tk()
master2 = Tk()

wall_width = 45
pip_width = 3
(x, y) = (10, 10)
gui_display = True

board = Canvas(master, width=(x+1)*pip_width+x*wall_width, height=(y+1)*pip_width+y*wall_width)
board2 = Canvas(master2, width=(x+1)*pip_width+x*wall_width, height=(y+1)*pip_width+y*wall_width)
#player = (0, y-1)
#me = 0


rows, columns = maze_gen.generate(10,0)


def render_grid():
	global walls, Width, x, y,player
	board.create_rectangle(0, 0, (x+1)*pip_width+x*wall_width, (y+1)*pip_width+y*wall_width, fill="white", width=1)
	for i in range(x+1):
		for j in range(y+1):
			#create yellow pegs
			board.create_rectangle(i*pip_width+i*wall_width, j*pip_width+j*wall_width, (i+1)*pip_width+i*wall_width, (j+1)*pip_width+j*wall_width, fill="yellow", width=1)
	for n in range(len(rows)):
		for i in range(len(rows[n])):
			if rows[n][i] is 1:
				board.create_rectangle((i+1)*pip_width+i*wall_width, n*pip_width+n*wall_width, (i+1)*pip_width+(i+1)*wall_width, (n+1)*pip_width+n*wall_width, fill="black", width=1)
	for n in range(len(columns)):
		for i in range(len(columns[n])):
			if columns[n][i] is 1:
				board.create_rectangle(i*pip_width+i*wall_width, (n+1)*pip_width+n*wall_width, (i+1)*pip_width+i*wall_width, (n+1)*pip_width+(n+1)*wall_width, fill="black", width=1)

	board.grid(row=0, column=0)


def render_grid2():
	global walls, Width, x, y,player
	board2.create_rectangle(0, 0, (x+1)*pip_width+x*wall_width, (y+1)*pip_width+y*wall_width, fill="white", width=1)

	for n in range(len(rows)):
		for i in range(len(rows[n])):
			if rows[n][i] is 1:
				board2.create_rectangle((i+1)*pip_width+i*wall_width, n*pip_width+n*wall_width, (i+1)*pip_width+(i+1)*wall_width, (n+1)*pip_width+n*wall_width, fill="black", width=1)
	for n in range(len(columns)):
		for i in range(len(columns[n])):
			if columns[n][i] is 1:
				board2.create_rectangle(i*pip_width+i*wall_width, (n+1)*pip_width+n*wall_width, (i+1)*pip_width+i*wall_width, (n+1)*pip_width+(n+1)*wall_width, fill="black", width=1)

	board2.grid(row=0, column=0)


def render_player():
	global me
	me = board.create_rectangle((player[0]+1)*pip_width+player[0]*wall_width+wall_width*1/3, (player[1]+1)*pip_width+player[1]*wall_width+wall_width*1/3,
			(player[0]+1)*pip_width+player[0]*wall_width+wall_width*2/3, (player[1]+1)*pip_width+player[1]*wall_width+wall_width*2/3, fill="grey", width=1, tag="me")	


def start_game(trial):
	global rows, columns

	rows, columns = rows, columns = maze_gen.generate(10,trial)
	if(gui_display):
		 render_grid()
                 #render_player()
		 master.mainloop()
	#restart = False

def refresh():
	global rows, columns

	rows, columns = rows, columns = maze_gen.generate(10,0)
	render_grid()
	#render_player()
     
	
b = Button(board2, text="refresh", command=refresh).pack()
     

	 

