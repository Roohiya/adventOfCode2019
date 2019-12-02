import math

f = open('input.txt', 'r')

contents = ''

if f.mode == 'r':
  contents = f.read()

inputArr = list(map(int, contents.split('\n')))

def getRecursiveFuelSum(item, sumFuel):
  if (item <= 0):
    return sumFuel

  fuelAmount = math.floor(item / 3) - 2

  if fuelAmount > 0:
    sumFuel += fuelAmount

  return getRecursiveFuelSum(fuelAmount, sumFuel)

def getSumOfFuel():
  mainSum = 0

  for item in inputArr:
    mainSum += getRecursiveFuelSum(item, 0)

  return mainSum

result = getSumOfFuel()
print('result', result)

