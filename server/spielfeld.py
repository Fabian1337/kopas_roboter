from tkinter import *
import tkinter as tk
from random import randint
from roboter import Roboter

class Gui():
    reference = None
    roboter = None

    __RoboterGui = None

    @staticmethod
    def getReference():
        if Gui.reference == None:
            print("no reference")
        return Gui.reference

    def getCanvas(self):
        return self.canvas

    def getRoboter(self):
        if Gui.__RoboterGui == None:
            Gui.__RoboterGui = Roboter(self.canvas)
        return Gui.__RoboterGui


    def __init__(self, root, columns=7, rows=6, cellsize=50, bordersize=100):
        self.gui = root
        self.cellsize = cellsize
        self.bordersize = bordersize
        self.columns = columns
        self.rows = rows
        self.create_grid(self.columns, self.rows)
        Gui.reference = self

    def create_grid(self, columns, rows):
        #calc window width = columns * cellsize + 2xbordersize
        #calc window height = rows * cellsize + 2xbordersize

        self.window_width = columns * self.cellsize + self.bordersize * 2
        self.window_height = rows * self.cellsize + self.bordersize * 2
        self.canvas = Canvas(self.gui, width=self.window_width, height=self.window_height)
        self.canvas.pack()

        diff = self.bordersize
        for _ in range(rows+1): # +1 to close grid
            #self.canvas.create_line(startpunkt x, startpunkt y, endpunkt x, endpunkt y)
            self.canvas.create_line(self.bordersize, diff, self.window_width-self.bordersize, diff)
            diff += self.cellsize
        
        diff = self.bordersize
        for _ in range(columns+1): # +1 to close grid
            self.canvas.create_line(diff, self.bordersize, diff, self.window_height-self.bordersize)
            diff += self.cellsize
    
    def grid_getXY(self, pos1, pos2, ballsize):
        return self.bordersize + self.cellsize * pos1 - self.cellsize + (self.cellsize - ballsize)/2, self.bordersize + self.cellsize * pos2 - self.cellsize + (self.cellsize - ballsize)/2

    def create_roboter(self, farbe, pos1, pos2):
        self.roboter = Roboter(self.canvas)
        self.roboter.farbe = farbe
        self.roboter.durchmesser = int(self.cellsize*0.9)
        x,y = self.grid_getXY(pos1,pos2, self.roboter.durchmesser)
        self.roboter.setStartPosition(x, y, pos1, pos2)
        self.roboter.display()

    def start_game(self):
        self.create_roboter("red", 3,4)
    
    def moveAbsolute(self, row, column):
        x,y = self.grid_getXY(row, column, self.roboter.durchmesser)
        self.roboter.moveToPosition(x, y, 20)
    
    def moveRelative(self, row, column):
        x,y = self.grid_getXY(self.roboter.row+row, self.roboter.column+column, self.roboter.durchmesser)
        print(x, y)
        self.roboter.moveToPosition(x, y, 20)

