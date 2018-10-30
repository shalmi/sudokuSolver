print("Program Start")

from sudokuBoard import board

# simple
puzzleStart = "....4.1.3...5..2...327.68.56.........8.....36.51.......7.2.13..52...8......657..."
solution = "865942173147583269932716845693874521784125936251369784476291358529438617318657492"

#easy
puzzleStart = ".4...8.9...3.75....8.2..4..8.......99.438....52..1.......15.....1.94.37......3..."
solution = "142638597693475182785291463831564729974382651526719834369157248218946375457823916"

# intermediate 1 53% working now 100 :D YAY
puzzleStart = "..4...2...9.71.5..61..5..4.4.6.....587...6...9...8..6.7....8.1........8....2....."
solution = "354869271298714536617352948436127895875936124921485763763598412542671389189243657"

# #intermediate 2 %40.7 now 42% YAY
puzzleStart = "5..12........7.5.3..7..6...1.2...7....9....16.3....4.5.......9.3..41....2.4.3...."
solution = "543128967618974523927356148182645739459783216736291485871562394365419872294837651"

# #advanced  48%
# puzzleStart = ".8...9..7.9..153.....3...89..14..8.5...............73..7812.4....9....7.4..9..5.1"
# solution = "384269157297815346615347289731492865846753912952681734578126493129534678463978521"


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
output = myBoard.outputAsString()
print(output)
print(solution)
print("{}% correct".format((81-output.count(" "))/81.0))
print(myBoard.outputAsString() == solution)
# print( myBoard.getNumsInThreeByThree(8) )
# print(myBoard.getCell(1,1))
print(myBoard.checkPuzzle())
# myBoard.checkCubesForRowsWithUniquePotentials()
# a = myBoard.getThreeByThreesByRows()
# for x in a:
#     print(x)
# myBoard.checkAislesForMiniAislesWithUniquePotentials()
print(myBoard.getCell(4,1))