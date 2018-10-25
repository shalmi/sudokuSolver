from cell import cell

class board:
    """Represents the Sudoku Board and it's main functions"""

    __AllCells = []

    def __init__(self,puzzleStart):
        print("Board Initializing")
        for eachRow in range(9):
            row = []
            for eachCell in range(9):
                row.append(cell())
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
        self.__AllCells[row][column].setValue(value)

    def getCell(self,row,column):
        # print(row,column,value)
        return self.__AllCells[row][column]

    def printTable(self):
        for eachRow in self.__AllCells:
           print(eachRow)

    def reduceBoard(self):
        self.cleanPotentialNumbers()
    
    def cleanPotentialNumbers(self):
        # Start with eachRow
        for row in range(9):
            usedNums = self.numsInRow(row)
            for eachCell in self.__AllCells[row]:
                eachCell.removeFromPotentials(usedNums)
        
        for column in range(9):
            usedNums = self.numsInColumn(column)
            for eachCell in self.getColumn(column):
                eachCell.removeFromPotentials(usedNums)
    
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