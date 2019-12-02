import copy

f = open('input.txt', 'r')

contents = ''

if f.mode == 'r':
  contents = f.read()

inputArr = list(map(int, contents.split(',')))

def superIntCode ():
  for noun in range(100):
    for verb in range(100):
      inputArrayVal = intCode(inputArr, noun, verb)
      if (inputArrayVal[0] == 19690720):
        return 100 * noun + verb

def intCode (inputArray, noun, verb):
  i = 0

  bufferArray = copy.deepcopy(inputArray)
  bufferArray[1] = noun
  bufferArray[2] = verb

  while (i < len(bufferArray)):
    if (bufferArray[i] == 1):
      bufferArray[bufferArray[i+3]] = bufferArray[bufferArray[i+1]] + bufferArray[bufferArray[i+2]]
    elif (bufferArray[i] == 2):
      bufferArray[bufferArray[i+3]] = bufferArray[bufferArray[i+1]] * bufferArray[bufferArray[i+2]]
    else:
      break

    i += 4
  return bufferArray


result = superIntCode()
print(result)