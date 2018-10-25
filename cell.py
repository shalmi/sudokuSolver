class cell:
    """Represents a single number space or cell in Sudoku"""
    __potentialNumbers = range(1,10)
    __currentValue=" "
    def getPotentialNumbers(self):
        return self.__potentialNumbers

    def setValue(self,value):
        self.__currentValue = value
        self.__potentialNumbers = []
    
    def getValue(self):
        return self.__currentValue

    def removeFromPotentials(self,numsToRemove):
        self.__potentialNumbers = list(set(self.__potentialNumbers) - set(numsToRemove))
        if len(self.__potentialNumbers) == 1:
            self.setValue(self.__potentialNumbers[0])

    def __repr__(self):
        return str(self.__currentValue)

    def __str__(self):
        return self.__currentValue