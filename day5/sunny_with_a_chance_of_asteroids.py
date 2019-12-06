import math

f = open('input.txt', 'r')

contents = ''

if f.mode == 'r':
  contents = f.read()

inputArr = list(map(int, contents.split(',')))

def intCode ():
  i = 0
  newArr = []
  inputArr[1] = 12
  inputArr[2] = 2

  while (i < len(inputArr)):
    if (inputArr[i] == 1):
      inputArr[inputArr[i+3]] = inputArr[inputArr[i+1]] + inputArr[inputArr[i+2]]
    elif (inputArr[i] == 2):
      inputArr[inputArr[i+3]] = inputArr[inputArr[i+1]] * inputArr[inputArr[i+2]]
    else:
      return

    i += 4

intCode()
print(inputArr)

def add(params, inputList):
  firstParam = params[0]
  secondParam = params[2]
  thirdParam = params[3]

  firstVal = inputList[inputList[firstParam]]
  secondVal = inputList[secondParam]

  inputList[inputList[thirdParam]] = firstVal + secondVal

def multiply(params, inputList):
  firstParam = params[0]
  secondParam = params[2]
  thirdParam = params[3]

  firstVal = inputList[inputList[firstParam]]
  secondVal = inputList[secondParam]

  inputList[inputList[thirdParam]] = firstVal * secondVal

i = 0
output = 0

while (i < len(inputArr)):
    if (inputArr[i] == 3):
      inputArr[i+1] = inputArr[inputArr[i+1]]
      i += 2
    elif (inputArr[i] == 4):
      output = inputArr[inputArr[i+1]]
      print(output)
      i += 2
    elif (str(inputArr[i])[-2:] == '02'):
      params = ('0' + str(inputArr[i])[2]).split()
      params.reverse()
      multiply(params, inputArr)
    elif (str(inputArr[i])[-2:] == '01'):
      params = ('0' + str(inputArr[i])[2]).split()
      params.reverse()
      add(params, inputArr)
    elif (str(inputArr[i])[-2:] == '99'):
      return


