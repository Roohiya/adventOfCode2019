import math

f = open('input.txt', 'r')

contents = ''

if f.mode == 'r':
  contents = f.read()

inputArr = list(map(int, contents.split('\n')))

def getSumOfFuel():
  totalFuel = 0

  for item in inputArr:
    totalFuel += math.floor(item / 3) - 2

  return totalFuel

result = getSumOfFuel()
print('result', result)