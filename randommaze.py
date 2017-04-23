import numpy as np
import random
from collections import deque

rows = []
columns = []
cells = []
walls = 0
saved_mazes = []
saved_size = 0

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class MazeCell:
	def __init__(self,x,y):
		self.x = x
    		self.y = y
        	self.visited = False

def set_maze_size(size):
	global saved_size
	saved_size = size

def generate(maze_size, trial):
	
	global walls
	global rows
	global columns 
	global cells 

	if(saved_size > 0 and len(saved_mazes) == saved_size):
		rows, columns = saved_mazes[trial%saved_size]
		return rows, columns

	walls = maze_size
	rows = [[1 for i in range(walls)] for j in range(walls+1)] 
	columns = [[1 for i in range(walls+1)] for j in range(walls)] 

	for y in range(walls):
		for x in range(walls):
			cells.append(MazeCell(x,y))

	cell_stack = Stack()
	unvistedCells = len(cells)
	currentCell = 0
	cells[currentCell].visited = True
	unvistedCells -= 1
	
	while (unvistedCells > 0):
		nextCell = chooseUnvisitedNeighbor(currentCell)
		if(nextCell != -1):
			cell_stack.push(currentCell)
			removeWall(currentCell,nextCell)
			currentCell = nextCell
			cells[currentCell].visited = True	
			unvistedCells -= 1
		elif(cell_stack.size() > 0):
			currentCell = cell_stack.pop()
	
	cells = [] 

	if(saved_size > 0 and len(saved_mazes) < saved_size):
		saved_mazes.append((rows,columns))
	return rows, columns

def chooseUnvisitedNeighbor(currentCell):
	x = cells[currentCell].x
	y = cells[currentCell].y
	
	candidates = []

	# left
	if(x > 0 and cells[currentCell-1].visited is False):
		candidates.append(currentCell-1)
	# right
	if(x < (walls-1) and cells[currentCell+1].visited is False):
		candidates.append(currentCell+1)
	# up
	if(y > 0 and cells[currentCell-walls].visited is False):
		candidates.append(currentCell-walls)	
	# down
	if(y < (walls-1) and cells[currentCell+walls].visited is False):
		candidates.append(currentCell+walls)

	if(len(candidates) == 0):
		return -1

	random_choice = random.sample(candidates,len(candidates))
	
	return random_choice[0]

def removeWall(currentCell,nextCell):

	global columns
	global rows

	if(nextCell-currentCell == 1):
		columns[currentCell/walls][currentCell%walls+1] = 0

	elif(currentCell - nextCell == 1):
		columns[currentCell/walls][currentCell%walls] = 0

	elif(currentCell - nextCell == walls):
		rows[currentCell/walls][currentCell%walls] = 0

	elif(nextCell - currentCell == walls):
		rows[currentCell/walls+1][currentCell%walls] = 0
