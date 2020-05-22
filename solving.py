#!/usr/bin/python3
import pdb
class Solve:
    def __init__(self):
        self.blockList = []
        for i in range(0, 9):
            self.blockList.append([])   
        # def blocks
        self.blockList[0] = [0, 1, 2, 9, 10, 11, 18, 19, 20]
        self.blockList[1] = [3, 4, 5, 12, 13, 14, 21, 22, 23]
        self.blockList[2] = [6, 7, 8, 15, 16, 17, 24, 25, 26]
        self.blockList[3] = [27, 28, 29, 36, 37, 38, 45, 46, 47]
        self.blockList[4] = [30, 31, 32, 39, 40, 41, 48, 49, 50]
        self.blockList[5] = [33, 34, 35, 42, 43, 44, 51, 52, 53] 
        self.blockList[6] = [60, 61, 62, 69, 70, 71, 78, 79, 80]
        self.blockList[7] = [57, 58, 59, 66, 67, 68, 75, 76, 77]
        self.blockList[8] = [54, 55, 56, 63, 64, 65, 72, 73, 74]
    def delHorizontal(self, numList, mylist, index):
        # get the raw
        count = 0
        stop = False
        raw = -1
        for i in range(0, 9):
            for j in range(0, 9):
                if stop:
                    break
                if index == count:
                    raw = i
                    stop = True
                    break
                count += 1 

        startIndex = raw * 9
        endIndex = startIndex + 9
        for i in range(startIndex, endIndex):
            for indexNum, num in enumerate(numList):
                if num == mylist[i]:
                    numList.pop(indexNum)
                 
        return numList
    def delVertical(self, numList, mylist, index):
        # get the column
        stop = False
        column = -1
        for i in range(0, 9):
            if stop:
                break
            until = 81 + i 
            for j in range(i, until, 9):
                if index == j:
                    column = i 
                    stop = True
                    break 

        startIndex = column 
        endIndex = 81 + column
        for i in range(startIndex, endIndex, 9):
            for indexNum, num in enumerate(numList):
                if num == mylist[i]:
                    numList.pop(indexNum)
        return numList
 
    def testOnePos(self, mylist, index):
        # get block index          
        blockIndex = -1
        stop = False
        for indexNum, elem in enumerate(self.blockList):
            if stop:
                break
            for num in elem:
                if num == index:
                    blockIndex = indexNum
                    stop = True
                    break
        # start delete possibilties
        allNum = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
        for i in self.blockList[blockIndex]:
            if mylist[i] != -1:
                for indexNum1, num1 in enumerate(allNum):
                    if mylist[i] == num1: 
                        allNum.pop(indexNum1)
        
        allNum = self.delHorizontal(allNum, mylist, index)
        allNum = self.delVertical(allNum, mylist, index)
        
        return allNum
    def solveList(self, mylist):
        allNumRe = []
        count = 0
        newPos = 0
        while count <= newPos:
            for i in range(0, 81):
                if mylist[i] == -1:
                    allNumRe = self.testOnePos(mylist, i)
                    if len(allNumRe) == 1:
                        newPos += 1
                        mylist[i] = allNumRe[0]
            count += 1        
        return mylist
