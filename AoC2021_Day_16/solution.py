import numpy as np

hexDict = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
}

def GetBinaryList(testFile = False):
    input = '620080001611562C8802118E34'
    binList = []
    for letter in input:
        nibble = hexDict[letter]
        for bit in nibble:
            binList.append(bit)
    return np.array(binList)

def GetLiteralValue(currentPosn, binList):
    reachedEnd = False
    binString = []
    while(not reachedEnd):
        if binList[currentPosn] == 1:
            section = binList[currentPosn+1:currentPosn+5]
            binString.append(section)
            currentPosn += 5
        else:
            section = binList[currentPosn+1:currentPosn+5]
            binString.append(section)
            currentPosn += 5
            reachedEnd = True
    padding = 4 - (((5 * len(binString)) + 6) % 4)
    if padding == 4:
        padding = 0
    currentPosn += padding
    return int(''.join(section),2), currentPosn

def GetVersionAndTypeId(currentPosn, binList):
    version = int(''.join(binList[currentPosn:currentPosn + 3]),2)
    currentPosn += 3
    typeId = int(''.join(binList[currentPosn:currentPosn + 3]),2)
    currentPosn += 3
    return version, typeId, currentPosn

def GetVersionTotal(currentPosn, binList):
    totalVersion = 0
    version, typeId, currentPosn = GetVersionAndTypeId(currentPosn, binList)
    totalVersion += version
    if typeId == 4: #Literal value
        value, currentPosn = GetLiteralValue(currentPosn, binList)
    else:
        lengthTypeId = binList[currentPosn]
        currentPosn += 1
        if lengthTypeId == '0':
            bitLength = int(''.join(binList[currentPosn:currentPosn+15]),2)
            currentPosn += 15
            endLimit = currentPosn + bitLength
            while(currentPosn < endLimit):
                version, currentPosn = GetVersionTotal(currentPosn,binList)
                totalVersion += version
        else:
            numberOfSubPackets = int(''.join(binList[currentPosn:currentPosn+11]),2)
            currentPosn += 11
            for i in range(numberOfSubPackets):
                version, currentPosn = GetVersionTotal(currentPosn,binList)
                totalVersion += version
    return totalVersion, currentPosn

binList = GetBinaryList(True)
currentPosn = 0
GetVersionTotal(currentPosn,binList)