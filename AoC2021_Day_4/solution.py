def ReadFileIntoList(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

input = ReadFileIntoList("C:/Users/hiren/source/repos/AoC2021/AoC2021_Day_4/input.txt")

import numpy as np
import pandas as pd

drawNumbers = [int(num) for num in input[0].split(',')]

boardsCollated = input[2:]
boards = [[]]
boardNumber = 0
for i in range(len(boardsCollated)):
    if boardsCollated[i] != '':
        boards[boardNumber].append([int(line) for line in boardsCollated[i].split(' ') if line != ''])
    if boardsCollated[i] == '':
        boards.append([])
        boardNumber += 1

def RecreateArrays():
    dfArrayToChange = []
    dfArrayToKeep = []
    for i in range(len(boards)):
        df = pd.DataFrame(boards[i])
        dfArrayToChange.append(df.copy())
        dfArrayToKeep.append(df.copy())
    return (dfArrayToChange,dfArrayToKeep)

def CheckDfForWinners(df):
    for i in df.index:
        checkArray = df.iloc[i].values
        isRowWinner = all(flag == '' for flag in checkArray) 
        checkArray = df.iloc[:,i].values
        isColumnWinner = all(flag == '' for flag in checkArray)
        if isRowWinner or isColumnWinner:
            return True
        return False

(dfArrayToChange,dfArrayToKeep) = RecreateArrays()
hasWinner = False
for numberToTickOff in drawNumbers:
    for j in range(len(dfArrayToChange)):
        df = dfArrayToChange[j]
        df.replace(to_replace=numberToTickOff,value='',inplace=True)
        hasWinner = CheckDfForWinners(df)
        #print(hasWinner)
        if hasWinner == True:
            print("Winner found")
            print(df)
            print(f"This array number {j}")
            print(f"This was the last number drawn: {numberToTickOff}")
            break
    if hasWinner == True:
        break
sumOfUnchecked = np.sum(np.sum(dfArrayToChange[j].replace(to_replace='',value=0)))
answer = sumOfUnchecked * numberToTickOff
print(f"Answer is {sumOfUnchecked} * {numberToTickOff} = {answer}")