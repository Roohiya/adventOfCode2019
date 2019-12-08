import math

f = open('input.txt', 'r')

contents = ''

if f.mode == 'r':
  contents = f.read()

inputArr = list(map(int,contents.split(',')))

def add(mode1, mode2, inputList, index):
  print('add', mode1, mode2)
  # params = inputList[index+1:index+4]
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
  print('multiple', mode1, mode2)
  # params = inputList[index+1:index+4]
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
  print('===', modes)
  return [int(mode) for mode in [modes[2], modes[1], modes[0], modes[3:]]]

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

  return output

print('inputArr', len(inputArr))
result = intCode(inputArr, 1)
print(result)
