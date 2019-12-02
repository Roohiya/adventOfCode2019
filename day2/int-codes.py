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