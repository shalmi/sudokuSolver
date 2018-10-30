from cell import cell
import time

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
    def setSolution(self,inputSolution):
        row = 0
        column = 0
        for eachNum in inputSolution:
            self.__AllCells[row][column].setAnswerKey(int(eachNum))
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
        print("~~~~~~~~~~~~~~~~~~")
        for eachRow in self.__AllCells:
           print(eachRow)
        # time.sleep(.01)

    def cleanPotentialNumbers(self):
        self.cleanRows()
        self.cleanColumns()
        self.clean3By3s()
        print("(~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~)")
        # search for naked Triplets on all Rows
        # for eachRow in self.__AllCells:
        #     self.searchForNakedTripletsAdvanced(eachRow)

        # for x in range(9):
        #     self.searchForNakedTripletsAdvanced(self.getColumn(x))
        #     self.searchForNakedTripletsAdvanced(self.getThreeByThree(x))
        
        # check Cubes For Rows With Unique Potentials
        self.checkCubesForRowsWithUniquePotentials()
        self.checkAislesForMiniAislesWithUniquePotentials()

    def clean3By3s(self):
        for eachCube in range(9):
            cellsOfInterest = []
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
    
    def searchForNakedTripletsAdvanced(self,cells):
        """Naked Triplets where not all cells have all 3"""

        # row,column = cells[0].getCoordinates()
        # print("searchForNakedTripletsAdvanced WAS HIT:[{}][{}]".format(row,column))

        # Make a Major copy to not destroy cells
        # cellsMajorCopy = cells.copy()
        triplet = 3
        cellsMajorCopy = []
        # Now parse out the cells we dont need such as: 
        for eachCell in cells:
            # Cells that have already been found
            if not eachCell.isFound():
                # Cells with more than 3 potentials
                if len(eachCell.getPotentialNumbers())<=triplet:
                    cellsMajorCopy.append(eachCell)
            # That should leave us with cells that have a potential of 2 or 3
        if len(cellsMajorCopy)<=triplet:
            return #we cant do 3s compliment with only 3 items
        print("cellsMajoryCopy: {}".format(cellsMajorCopy))
        for lilCell in cellsMajorCopy:
            print(lilCell)
        for cellChooser in range(len(cellsMajorCopy)):
            # copy the list again as we will be destructive
            cellsCopy = cellsMajorCopy.copy()
            myCell = cellsCopy.pop(cellChooser)
            mainPotentialNums = myCell.getPotentialNumbers()
            for numOfSibling1s in range(len(cellsCopy)):
                potentialFirstSibling = cellsCopy.pop()
                setOfNums2 = potentialFirstSibling.getPotentialNumbers()
                combinedPotentials = list(set(setOfNums2) | set(mainPotentialNums))
                if len(combinedPotentials)>triplet:
                    continue #leave this sibling behind!
                    print("THIS LINE SHOULD NEVER BE PRINTED...IF IT IS SOMETHING WENT WRONG.")
                else:
                    # Lets find a 2nd sibling (aka 3rd cell)
                    if len(cellsCopy) == 0:
                        continue
                    ListOfPotentialThirdSiblings = cellsCopy.copy()
                    for numOfSiblings2 in range(len(ListOfPotentialThirdSiblings)):
                        potentialSecondSibling = ListOfPotentialThirdSiblings.pop()
                        setOfNums3 = potentialSecondSibling.getPotentialNumbers()
                        threeCombinedPotentials  = list(set(combinedPotentials) | set(setOfNums3))
                        if len(threeCombinedPotentials) == triplet:
                            print("WE DID IT!!!!!!!!!!!!!!!")
                            print(threeCombinedPotentials)
                            print(myCell,potentialFirstSibling,potentialSecondSibling)
                        else:
                            continue



    def removePotentialsFromCell(self,cell,potentials):
        """ removes potentials from cells and then cleans surroundings if a value was set """
        if cell.removeFromPotentials(potentials):
            self.updateSurroundings(cell)
        # self.printTable()

    def updateSurroundings(self,cell):
        """If a cell is decided, you need to update all surrounding cells\n
            Works on columns,rows, and surrounding 3x3"""
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
# Two functions to make
# 1. Checks to see if each miniAisle contains a potential that doest exist in the other 2 miniAisles
#       from the two other rubiks
#       If it does then It can remove that potential from the original miniAisle's rubik
# 2. Check if miniAisle contains a potential that doesnt exist in the other 2 miniAisles of the SAME rubik
#      if so, remove that potential from the other miniAisles on that Aisle
# 3. MAKE SURE TO DO THE SAME THING FOR COLUMNS FOR BOTH!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def getPuzzleByMiniRows(self,rowOrColumn):
        """returns the puzzle by rows or columns but with 
        each aisle split into 3 sets of 3.\n
        rowOrColumn can equal "row" or "column"""

        wholePuzzle = []
        if rowOrColumn == "row":
            wholePuzzle = self.__AllCells
        elif rowOrColumn == "column":
            for x in range(9):
                wholePuzzle.append(self.getColumn(x))
        PuzzleByMiniRows = []
        for eachAisle in wholePuzzle:
            SetOfMiniRows = []
            SetOfMiniRows.append(eachAisle[0:3])
            SetOfMiniRows.append(eachAisle[3:6])
            SetOfMiniRows.append(eachAisle[6:9])
            PuzzleByMiniRows.append(SetOfMiniRows)
        return PuzzleByMiniRows


# Check if miniAisle contains a potential that doesnt exist in the other 2 miniAisles of the aisle
#      if so, remove that potential from the other miniAisles on that cube  
    def checkAislesForMiniAislesWithUniquePotentials(self):
        """ Read checkCubesForRowsWithUniquePotentials() """
        sudokuByRowsAndColumns = []
        sudokuByRowsAndColumns.append(self.getPuzzleByMiniRows("row"))
        sudokuByRowsAndColumns.append(self.getPuzzleByMiniRows("column"))

        for sudokuByAisleOfAisles in sudokuByRowsAndColumns:
            for eachSubAisleOfAisle in range(3):
                AisleOffset = 3*eachSubAisleOfAisle
                for eachSubAisle in range(3):
                    oneRubik = sudokuByAisleOfAisles[AisleOffset+eachSubAisle]
                    potents = self.AislesOfPotentialsFromRubik(oneRubik)
                    aisle = -1
                    for eachPotentList in potents:
                        aisle+=1
                        # eachPotentList also represents each aisle of "eachSubAisle" 
                        potentsCopy = potents.copy()
                        potentsCopy.remove(eachPotentList)
                        UniquePotentials = list(set(eachPotentList) - (set(potentsCopy[0]) | set(potentsCopy[1]) )  )
                        if(len(UniquePotentials) > 0):
                            print("Found a Unique Potential at Aisle: {}, MegaColumn: {}. Potential(s) Found: {}".format(AisleOffset+eachSubAisle,aisle,UniquePotentials))
                            for x in range(3):
                                if x != eachSubAisle: # dont do this to the rubik we found obviously
                                    for eachNode in sudokuByAisleOfAisles[AisleOffset+x][aisle]:
                                        self.removePotentialsFromCell(eachNode,UniquePotentials)
                                        # print(eachNode.getValue())

# Check if miniAisle contains a potential that doesnt exist in the other 2 miniAisles of the SAME rubik
#      if so, remove that potential from the other miniAisles on that Aisle  
    def checkCubesForRowsWithUniquePotentials(self):
        """
        Should Calculate on 3 Rows or Aisles at a time. \n
        If the unique potential is found in the Capital Letter aisle,\n
        remove that potential from the corresponding lowercase aisle.\n
        The capital letter Rubik can move across the lowerase one \n
                         or \n
        [A,A,A,a,a,a,a,a,a]  [A,B,C,x,x,x,x,x,x] \n
        [B,B,B,b,b,b,b,b,b]  [A,B,C,x,x,x,x,x,x] \n
        [C,C,C,c,c,c,c,c,c]  [A,B,C,x,x,x,x,x,x] \n
        [x,x,x,x,x,x,x,x,x]  [a,b,c,x,x,x,x,x,x] \n
        [x,x,x,x,x,x,x,x,x]  [a,b,c,x,x,x,x,x,x] \n
        [x,x,x,x,x,x,x,x,x]  [a,b,c,x,x,x,x,x,x] \n
        [x,x,x,x,x,x,x,x,x]  [a,b,c,x,x,x,x,x,x] \n
        [x,x,x,x,x,x,x,x,x]  [a,b,c,x,x,x,x,x,x] \n
        [x,x,x,x,x,x,x,x,x]  [a,b,c,x,x,x,x,x,x] \n
        """
        ThreeByThreesByRow = self.getThreeByThreesByRows()
        ThreeByThreesByColumn = self.getThreeByThreesByColumns()
        sudokuByRowsAndColumns = []
        sudokuByRowsAndColumns.append(ThreeByThreesByRow)
        sudokuByRowsAndColumns.append(ThreeByThreesByColumn)
        for ThreeByThree in sudokuByRowsAndColumns:
            for eachAisleOfRubiks in range(3):
                AisleOffset = 3*eachAisleOfRubiks
                for eachRubik in range(3):
                    oneRubik = ThreeByThree[AisleOffset+eachRubik]
                    potents = self.AislesOfPotentialsFromRubik(oneRubik)
                    aisle = -1
                    for eachPotentList in potents:
                        aisle+=1
                        # eachPotentList also represents each aisle of "eachRubik" 
                        potentsCopy = potents.copy()
                        potentsCopy.remove(eachPotentList)
                        UniquePotentials = list(set(eachPotentList) - (set(potentsCopy[0]) | set(potentsCopy[1]) )  )
                        if(len(UniquePotentials) > 0):
                            print("Found a Unique Potential at Rubik: {}, Aisle: {}. Potential(s) Found: {}".format(AisleOffset+eachRubik,aisle,UniquePotentials))
                            for x in range(3):
                                if x != eachRubik: # dont do this to the rubik we found obviously
                                    for eachNode in ThreeByThree[AisleOffset+x][aisle]:
                                        self.removePotentialsFromCell(eachNode,UniquePotentials)
                                        # print(eachNode.getValue())


    def AislesOfPotentialsFromRubik(self,rubik):
        """receieves a rubik aka 3x3 in the form of:\n
        [[0,1,2],[3,4,5],[6,7,8]]\n
        and returns 3 Lists of Potentials"""

        ListOfPotentials = []
        for eachRow in rubik:
            potentials = []
            for eachCell in eachRow:
                potentials = list(set(potentials) | set(eachCell.getPotentialNumbers()))
            ListOfPotentials.append(potentials)
        return ListOfPotentials

    def getThreeByThreesByRows(self):
        """Different than getThreeByThree(request)
        returns 9 Lists of 3 Lists"""
        ListOf3x3s = []
        # For each set of Three Full Rows Or Columns
        for SetOfThreeRowsOrColumns in range(3):
            # Init Variables for each code to run on each 3x9
            aisle = 3*SetOfThreeRowsOrColumns #0,3,or 6
            for each3x3 in range(3):
                ThreeByThree = []
                parseStart = each3x3*3
                parseEnd = parseStart+3
                for eachMiniAisle in range(3):
                    ThreeByThree.append(self.getRow(aisle+eachMiniAisle)[parseStart:parseEnd])
                ListOf3x3s.append(ThreeByThree)
        return ListOf3x3s
        # HOW TO EASILY USE
        # ThreeByThrees = myBoard.getThreeByThreesByRows()
        # for x in ThreeByThrees:
        #     for y in x:
        #         print(y)
        #     print("~~~~~~~~~")

    def getThreeByThreesByColumns(self):
        """returns 9 Lists of 3 Lists"""
        ListOf3x3s = []
        # For each set of Three Full Rows Or Columns
        for SetOfThreeRowsOrColumns in range(3):
            # Init Variables for each code to run on each 3x9
            aisle = 3*SetOfThreeRowsOrColumns #0,3,or 6
            for each3x3 in range(3):
                ThreeByThree = []
                parseStart = each3x3*3
                parseEnd = parseStart+3
                for eachMiniAisle in range(3):
                    ThreeByThree.append(self.getColumn(aisle+eachMiniAisle)[parseStart:parseEnd])
                ListOf3x3s.append(ThreeByThree)
        return ListOf3x3s



    def cleanRows(self):
        for row in range(9):
            cellsOfInterest = []
            usedNums = self.numsInRow(row)
            for eachCell in self.__AllCells[row]:
                cellsOfInterest.append(eachCell)
                self.removePotentialsFromCell(eachCell,usedNums)
        self.findUniquePotentials(cellsOfInterest)
        self.findUniquePotentialMultiples(cellsOfInterest)

    def cleanColumns(self):
        for column in range(9):
            cellsOfInterest = []
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
        cellsSafeCopy = cells.copy()
        while True:
            # make sure that the list has more things in it
            if len(cellsSafeCopy) == 0:
                return
            # grab the first cell off the list
            myCell = cellsSafeCopy.pop(0)
            # print("myCell: {}".format(myCell))
            # print("cellsSafeCopy: {}".format(cellsSafeCopy))
            friends = [] #friends have duplicate Potential Numbers
            chosenPotentials = myCell.getPotentialNumbers()
            # if it only has one potential...ignore it and toss it
            if len(chosenPotentials)<=1:
                return
            elif len(chosenPotentials) ==2:
                for otherCell in cellsSafeCopy:
                    if otherCell.getPotentialNumbers() == chosenPotentials:
                        friends.append(otherCell)
                        cellsSafeCopy.remove(otherCell)
                if len(friends) == (len(chosenPotentials)-1):
                    #winner winner chicken dinner
                    for otherCell in cellsSafeCopy:
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
    
    def getRow(self,row):
        return self.__AllCells[row]
    
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
    def getThreeByThree(self,request):
        # request = which3x3 (0-8)
        result = []
        upperLeftRow = int((request)/3)*3
        upperLeftColumn = (request%3)*3
        # print("Row:", upperLeftRow)
        # print("Column:", upperLeftColumn)
        for x in range(3):
            for y in range(3):
                result.append(self.__AllCells[upperLeftRow+y][upperLeftColumn+x])
        return result
    def outputAsString(self):
        output = ""
        for row in self.__AllCells:
            for eachSquare in row:
                output+=str(eachSquare.getValue())
        return output

    def checkPuzzle(self):
        """Verifies if the puzzle has any mistakes.
        I am slightly concerned that there may be 
        two solutions to some of these puzzles"""
        AllNums = set(range(1,10))
        passed = True
        
        # Start by checking every row for every number
        currentRow = 0
        for eachRow in self.__AllCells:
            numsChecking = []
            for item in eachRow:
                numsChecking.append(item.getValue())
            uniqueNums = list(set(numsChecking) & set(AllNums))
            if len(uniqueNums) != 9:
                missingNums = list(set(AllNums)-set(uniqueNums))
                print("Puzzle failed on row: {}, missing: {}".format(currentRow,missingNums) )
                passed = False
            currentRow += 1
        return passed