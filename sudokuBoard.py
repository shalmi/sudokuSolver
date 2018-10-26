from cell import cell

class board:
    """Represents the Sudoku Board and it's main functions"""

    __AllCells = []

    def __init__(self,puzzleStart):
        print("Board Initializing")
        for eachRow in range(9):
            row = []
            for eachCell in range(9):
                row.append(cell(eachRow,eachCell))
            self.__AllCells.append(row)
        self.__setWholeTable(puzzleStart)

    def getTable(self):
        return self.__AllCells

    def __setWholeTable(self,inputPuzzle):
        row = 0
        column = 0
        for eachNum in inputPuzzle:
            if eachNum == ".":
                pass
            else:
                self.setCell(row,column,int(eachNum))
            column+=1
            if column >8:
                column = 0
                row+=1

    def setCell(self,row,column,value):
        # print(row,column,value)
        cell = self.__AllCells[row][column]
        cell.setValue(value)
        self.updateSurroundings(cell)

    def getCell(self,row,column):
        # print(row,column,value)
        return self.__AllCells[row][column]

    def printTable(self):
        for eachRow in self.__AllCells:
           print(eachRow)

    def reduceBoard(self):
        self.cleanPotentialNumbers()
    
    def cleanPotentialNumbers(self):
        self.cleanRows()
        self.cleanColumns()
        self.clean3By3s()

    def clean3By3s(self):
        cellsOfInterest = []
        for eachCube in range(9):
            allNums = range(1,10)
            usedNums = self.getNumsInThreeByThree(eachCube)
            unusedNums = list(set(allNums)-set(usedNums))
            upperLeftRow = int((eachCube)/3)*3
            upperLeftColumn = (eachCube%3)*3
            for x in range(3):
                for y in range(3):
                    thisCell = self.__AllCells[upperLeftRow+y][upperLeftColumn+x]
                    cellsOfInterest.append(thisCell)
                    self.removePotentialsFromCell(thisCell,usedNums)
            self.findUniquePotentials(cellsOfInterest)
            # next go through all the unusedNums
                #see if from all of the cells if only one has the unused num
                    #set it
        

    def removePotentialsFromCell(self,cell,potentials):
        """ removes potentials from cells and then cleans surroundings if a value was set """
        if cell.removeFromPotentials(potentials):
            self.updateSurroundings(cell)

    def updateSurroundings(self,cell):
        """If a cell is decided, you need to update all surrounding cells"""
        row,column = cell.getCoordinates()
        value = cell.getValue()
        for eachCell in self.__AllCells[row]:
            self.removePotentialsFromCell(eachCell,[value,])
        for eachRow in self.__AllCells:
            self.removePotentialsFromCell(eachRow[column],[value,])
        upperLeftRow = int((row)/3)*3
        upperLeftColumn = int(column/3)*3
        for x in range(3):
            for y in range(3):
                thisCell = self.__AllCells[upperLeftRow+y][upperLeftColumn+x]
                self.removePotentialsFromCell(thisCell,[value,])

        

    def cleanRows(self):
        cellsOfInterest = []
        for row in range(9):
            usedNums = self.numsInRow(row)
            for eachCell in self.__AllCells[row]:
                cellsOfInterest.append(eachCell)
                self.removePotentialsFromCell(eachCell,usedNums)
        self.findUniquePotentials(cellsOfInterest)
        self.findUniquePotentialMultiples(cellsOfInterest)

    def cleanColumns(self):
        cellsOfInterest = []
        for column in range(9):
            usedNums = self.numsInColumn(column)
            for eachCell in self.getColumn(column):
                cellsOfInterest.append(eachCell)
                self.removePotentialsFromCell(eachCell,usedNums)

        self.findUniquePotentials(cellsOfInterest)
        self.findUniquePotentialMultiples(cellsOfInterest)

    def findUniquePotentials(self,cells):
        for iteration in range(len(cells)):
            myCell = cells.pop(0)
            chosenPotentials = myCell.getPotentialNumbers()
            otherPotentials = []
            for eachCell in cells:
                otherPotentials = list(set(otherPotentials) | set(eachCell.getPotentialNumbers()))
            uniquePotentials = list(set(chosenPotentials)-set(otherPotentials))
            if len(uniquePotentials) == 1:
                myCell.setValue(uniquePotentials[0])
                self.updateSurroundings(myCell)
            cells.append(myCell)

    def findUniquePotentialMultiples(self,cells):
        while True:
            # make sure that the list has more things in it
            if len(cells) == 0:
                return
            # grab the first cell off the list
            myCell = cells.pop(0)
            friends = [] #friends have duplicate Potential Numbers
            chosenPotentials = myCell.getPotentialNumbers()
            # if it only has one potential...ignore it and toss it
            if len(chosenPotentials)<=1:
                return
            else:
                for otherCell in cells:
                    if otherCell.getPotentialNumbers() == chosenPotentials:
                        friends.append(otherCell)
                        cells.remove(otherCell)
                if len(friends) == (len(chosenPotentials)-1):
                    #winner winner chicken dinner
                    for otherCell in cells:
                        self.removePotentialsFromCell(otherCell,chosenPotentials)


    def numsInRow(self,row):
        allNums = []
        for eachNum in self.__AllCells[row]:
            if eachNum.getValue() != " ":
                allNums.append(eachNum.getValue())
        return allNums

    def numsInColumn(self,column):
        allNums = []
        for eachNum in self.getColumn(column):
            if eachNum.getValue() != " ":
                allNums.append(eachNum.getValue())
        return allNums
    
    def getColumn(self,column):
        result = []
        for x in range(9):
            result.append(self.__AllCells[x][column])
        return result
    
    def getNumsInThreeByThree(self,request):
        # request = which3x3 (0-8)
        result = []
        upperLeftRow = int((request)/3)*3
        upperLeftColumn = (request%3)*3
        # print("Row:", upperLeftRow)
        # print("Column:", upperLeftColumn)
        for x in range(3):
            for y in range(3):
                val = self.__AllCells[upperLeftRow+y][upperLeftColumn+x].getValue()
                if val != " ":
                    result.append(val)    
        return result
    
    def outputAsString(self):
        output = ""
        for row in self.__AllCells:
            for eachSquare in row:
                output+=str(eachSquare.getValue())
        return output

        
