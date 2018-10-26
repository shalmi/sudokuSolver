print("Program Start")

from sudokuBoard import board

puzzleStart = "....4.1.3...5..2...327.68.56.........8.....36.51.......7.2.13..52...8......657..."
solution = "865942173147583269932716845693874521784125936251369784476291358529438617318657492"

puzzleStart = ".4...8.9...3.75....8.2..4..8.......99.438....52..1.......15.....1.94.37......3..."
solution = "142638597693475182785291463831564729974382651526719834369157248218946375457823916"

puzzleStart = "..4...2...9.71.5..61..5..4.4.6.....587...6...9...8..6.7....8.1........8....2....."
solution = "354869271298714536617352948436127895875936124921485763763598412542671389189243657"


myBoard = board(puzzleStart)
myBoard.setSolution(solution)
myBoard.printTable()
for x in range(10):
    before = myBoard.outputAsString()
    myBoard.cleanPotentialNumbers()
    if (before == myBoard.outputAsString()):
        print("Stopped evolving after "+str(x)+" generations!")
        break


print("!!!!!!!!!!!!!!!!!!!")
myBoard.printTable()
print(myBoard.outputAsString())
print(solution)
print(myBoard.outputAsString() == solution)
# print( myBoard.getNumsInThreeByThree(8) )
# print(myBoard.getCell(1,1))
print(myBoard.checkPuzzle())