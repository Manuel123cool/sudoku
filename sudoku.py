#!/usr/bin/python3

import random
import numpy
import arcade
import pdb
import solving

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "sudoku"

solve = solving.Solve()

class Sudoku:
    def __init__(self):
        self.sudokuList = [] 
        for i in range(0, 81):
            self.sudokuList.append(-1)

        self.fieldClicket = -1
    def getIndex(self, x, y):
        xRow = 0
        yRow = 0
        count = 0
        for i in range(0, 9):
            if i * 66.666 - x < xRow:
                xRow = count    
                count += 1

        count1 = 0 
        for i in range(0, 9):
            if i * 66.666 - y < yRow:
                yRow = count1
                count1 += 1
        
        index = yRow * 9 + xRow
        return index        
    def mousePressed(self, x, y):
        index = self.getIndex(x, y)
        self.fieldClicket = index
    def keyPressed(self, key):
        if key == 115:
            self.sudokuList = solve.solveList(self.sudokuList)
            
        realKey = -1 
        
        keyDict = {
            49: 1,
            50: 2,
            51: 3,
            52: 4,
            53: 5,
            54: 6,
            55: 7,
            56: 8,
            57: 9
        }
        if key in keyDict:
            realKey = keyDict.get(key) 

        if realKey != -1 and self.fieldClicket != -1:
            self.sudokuList[self.fieldClicket] = realKey

sudoku = Sudoku()

def on_draw(delte_time):
    arcade.start_render()
    
    for y in range(3, 600, 200):
        arcade.draw_line(0, y, 600, y, arcade.color.ASH_GREY, 6)
    
    for x in range(3, 600, 200):
        arcade.draw_line(x, 600, x, 0, arcade.color.ASH_GREY, 6)
        
    arcade.draw_line(597, 0, 597, 600, arcade.color.ASH_GREY, 6)
    arcade.draw_line(600, 597, 0, 597, arcade.color.ASH_GREY, 6)

    for x in numpy.arange(0, 600, 66.6666):
        arcade.draw_line(x, 0, x, 600, arcade.color.ASH_GREY, 1) 

    for y in numpy.arange(0, 600, 66.6666):
        arcade.draw_line(0, y, 600, y, arcade.color.ASH_GREY, 1) 

    # draw sudoku array
    count = 0
    for i in range(0, 9): 
        for j in range(0, 9):
            x = j * 66.666 + 33.33
            y = i * 66.666 + 33.33
            if sudoku.sudokuList[count] != -1: 
                arcade.draw_text(str(sudoku.sudokuList[count]), x, y, 
                        arcade.color.BLACK, 20, width=200, align="center",
                                    anchor_x="center", anchor_y="center")
            count += 1
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
    def on_key_press(self, key, modifiers):
        sudoku.keyPressed(key)
    def on_mouse_press(self, x, y, button, modifiers):
         if button == arcade.MOUSE_BUTTON_LEFT:
            sudoku.mousePressed(x, y)
arcade.schedule(on_draw, 1 / 80)
MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
