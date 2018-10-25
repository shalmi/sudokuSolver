print("Program Start")

from sudokuBoard import board

puzzleStart = "....4.1.3...5..2...327.68.56.........8.....36.51.......7.2.13..52...8......657..."
# puzzleStart = ".9..4.1.3...5..2...327.68.561........8.....36.51.......7.2.13..52...8....4.657..."

# puzzleStart = "....4.1.3...5..2..1327468.56.........8.....36.51.......7.2.13..52...8......657..."

solution = "865942173147583269932716845693874521784125936251369784476291358529438617318657492"


myBoard = board(puzzleStart)
myBoard.printTable()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()
myBoard.cleanPotentialNumbers()


print("!!!!!!!!!!!!!!!!!!!")
myBoard.printTable()
# print( myBoard.getNumsInThreeByThree(8) )
