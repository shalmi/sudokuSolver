class cell:
    """Represents a single number space or cell in Sudoku"""
    __potentialNumbers = range(1,10)
    __currentValue=" "
    __row = -1
    __column = -1
    __answer = -1
    __answerKeyExists = False

    def __init__(self,row,column):
        self.__row = row
        self.__column = column
    
    def getPotentialNumbers(self):
        return self.__potentialNumbers

    def getCoordinates(self):
        return self.__row,self.__column
    
    def setValue(self,value):
        if self.__answerKeyExists:
            if value != self.__answer:
                print("ERROR!!! Proposed Value for cell[{}][{}] is {} but the right answer is {} ".format(self.__row,self.__column,value,self.__answer))
                while(True):
                    pass
        self.__currentValue = value
        self.__potentialNumbers = [value,]

    def isFound(self):
        return (self.__currentValue != " ")

    def setAnswerKey(self,value):
        self.__answer = value
        self.__answerKeyExists = True

    def getValue(self):
        return self.__currentValue

    def removeFromPotentials(self,numsToRemove):
        """ Removes the "numsToRemove" from the list of potentials.\n
        numsToRemove must be a list.\n
        returns True if the cell is decided. False if more work is needed"""
        self.__potentialNumbers = list(set(self.__potentialNumbers) - set(numsToRemove))
        if len(self.__potentialNumbers) == 1:
            self.setValue(self.__potentialNumbers[0])
            return True
        return False

    def __repr__(self):
        return str(self.__currentValue)

    def __str__(self):
        output = "currentValue: "+str(self.__currentValue)+"\n"
        output += "potentialValues: {}\n".format(self.__potentialNumbers)
        output += "row: {}, col: {}".format(self.__row,self.__column)
        return output
    
    # def printOut(self):
