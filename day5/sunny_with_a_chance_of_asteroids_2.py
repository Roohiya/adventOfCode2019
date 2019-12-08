import math

f = open('input.txt', 'r')

contents = ''

if f.mode == 'r':
  contents = f.read()

inputArr = list(map(int,contents.split(',')))

def add(mode1, mode2, inputList, index):
  firstVal = 0
  secondVal = 0

  if (mode1 == 0):
    firstVal = inputList[inputList[index+1]]
  else:
    firstVal = inputList[index+1]

  if (mode2 == 0): # position mode
    secondVal = inputList[inputList[index+2]]
  else:
    secondVal = inputList[index+2]

  inputList[inputList[index+3]] = firstVal + secondVal

def multiply(mode1, mode2, inputList, index):
  firstVal = 0
  secondVal = 0

  if (mode1 == 0):
    firstVal = inputList[inputList[index+1]]
  else:
    firstVal = inputList[index+1]

  if (mode2 == 0): # position mode
    secondVal = inputList[inputList[index+2]]
  else:
    secondVal = inputList[index+2]

  inputList[inputList[index+3]] = firstVal * secondVal

def retrieveModes (modes):
  return [int(mode) for mode in [modes[2], modes[1], modes[0], modes[3:]]]

def jump_if_true (mode1, mode2, inputList, index):
    if (mode1 == 0):
        firstParam = inputList[inputList[index+1]]
    else:
        firstParam = inputList[index+1]

    if (mode2 == 0):
        secondParam = inputList[inputList[index+2]]
    else:
        secondParam = inputList[index+2]

    if (firstParam != 0):
        return secondParam

    return None

def jump_if_false (mode1, mode2, inputList, index):
    if (mode1 == 0):
        firstParam = inputList[inputList[index+1]]
    else:
        firstParam = inputList[index+1]

    if (mode2 == 0):
        secondParam = inputList[inputList[index+2]]
    else:
        secondParam = inputList[index+2]

    if (firstParam == 0):
        return secondParam

    return None

def less_than (mode1, mode2, inputList, index):
    if (mode1 == 0):
        firstParam = inputList[inputList[index+1]]
    else:
        firstParam = inputList[index+1]

    if (mode2 == 0):
        secondParam = inputList[inputList[index+2]]
    else:
        secondParam = inputList[index+2]

    if (firstParam < secondParam):
        inputList[inputList[index+3]] = 1
    else:
        inputList[inputList[index+3]] = 0

def equal (mode1, mode2, inputList, index):
    if (mode1 == 0):
        firstParam = inputList[inputList[index+1]]
    else:
        firstParam = inputList[index+1]

    if (mode2 == 0):
        secondParam = inputList[inputList[index+2]]
    else:
        secondParam = inputList[index+2]

    if (firstParam == secondParam):
        inputList[inputList[index+3]] = 1
    else:
        inputList[inputList[index+3]] = 0

def intCode(inputArr, inputCode):
  i = 0
  output = 0

  trailing = ':05'

  while (inputArr[i] != 99):
    mode1, mode2, mode3, opCode = retrieveModes(f"{inputArr[i]:05}")

    if (opCode == 1):
      # print('1', inputArr)
      add(mode1, mode2, inputArr, i)
      i+=4
    if (opCode == 2):
      # print('2', inputArr)
      multiply(mode1, mode2, inputArr, i)
      i+=4
    if (opCode == 3):
      # print('3', inputArr)
      inputArr[inputArr[i+1]] = inputCode
      i+=2
    if (opCode == 4):
      # print('4', inputArr)
      output = inputArr[inputArr[i+1]]
      i+=2
    if (opCode == 5):
        index = jump_if_true(mode1, mode2, inputArr, i)
        if (index is not None):
            i = index
        else:
            i += 3
    if (opCode == 6):
        index = jump_if_false(mode1, mode2, inputArr, i)
        if (index is not None):
            i = index
        else:
            i += 3
    if (opCode == 7):
        less_than(mode1, mode2, inputArr, i)
        i += 4
    if (opCode == 8):
        equal(mode1, mode2, inputArr, i)
        i += 4

  return output

print('inputArr', len(inputArr))
result = intCode(inputArr, 5)
print(result)
