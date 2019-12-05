import copy
import sys
import time
start = time.time()

f = open('input.txt', 'r')

contents = ''

if f.mode == 'r':
  contents = f.read()

def crossedWires():
  wiresArr = contents.split('\n')
  wire1 = wiresArr[0].split(',')
  wire2 = wiresArr[1].split(',')
  wires = []
  wires.append(wire1)
  wires.append(wire2)

  coords = {}
  coordsDist = {}
  centralPort1 = [0, 0]
  centralPort2 = [0, 0]
  count = -1

  for point in wire1:
    direction = point[:1]
    steps = int(point[1:])

    if (direction == 'R'):
      for step in range(steps):
        fullKey = ','.join(list(map(str, centralPort1)))
        if (fullKey not in coords):
          coords[fullKey] = 1
          coordsDist[fullKey] = 0
        count += 1
        coordsDist[fullKey] = count
        centralPort1[0] += 1
    elif (direction == 'L'):
      for step in range(steps):
        fullKey = ','.join(list(map(str, centralPort1)))
        if (fullKey not in coords):
          coords[fullKey] = 1
          coordsDist[fullKey] = 0
        count += 1
        coordsDist[fullKey] = count
        centralPort1[0] -= 1
    elif (direction == 'U'):
      for step in range(steps):
        fullKey = ','.join(list(map(str, centralPort1)))
        if (fullKey not in coords):
          coords[fullKey] = 1
          coordsDist[fullKey] = 0
        count += 1
        coordsDist[fullKey] = count
        centralPort1[1] += 1
    elif (direction == 'D'):
      for step in range(steps):
        fullKey = ','.join(list(map(str, centralPort1)))
        if (fullKey not in coords):
          coords[fullKey] = 1
          coordsDist[fullKey] = 0
        count += 1
        coordsDist[fullKey] = count
        centralPort1[1] -= 1

  coordsDist2 = {}
  count2 = -1

  for point in wire2:
    direction = point[:1]
    steps = int(point[1:])

    if (direction == 'R'):
      for step in range(steps):
        fullKey = ','.join(list(map(str, centralPort2)))
        if (fullKey in coords):
          coords[fullKey]+= 1
          coordsDist2[fullKey] = 0
        count2 += 1
        coordsDist2[fullKey] = count2
        centralPort2[0] += 1
    elif (direction == 'L'):
      for step in range(steps):
        fullKey = ','.join(list(map(str, centralPort2)))
        if (fullKey in coords):
          coords[fullKey] += 1
          coordsDist2[fullKey] = 0
        count2 += 1
        coordsDist2[fullKey] = count2
        centralPort2[0] -= 1
    elif (direction == 'U'):
      for step in range(steps):
        fullKey = ','.join(list(map(str, centralPort2)))
        if (fullKey in coords):
          coords[fullKey] += 1
          coordsDist2[fullKey] = 0
        count2 += 1
        coordsDist2[fullKey] = count2
        centralPort2[1] += 1
    elif (direction == 'D'):
      for step in range(steps):
        fullKey = ','.join(list(map(str, centralPort2)))
        if (fullKey in coords):
          coords[fullKey] += 1
          coordsDist2[fullKey] = 0
        count2 += 1
        coordsDist2[fullKey] = count2
        centralPort2[1] -= 1

  intersection = []
  keys = []
  for key, value in coords.items():
    if (value > 1):
      keys.append(key)

  minTotalSteps = sys.maxsize
  for key in keys:
    step1 = coordsDist[key]
    step2 = coordsDist2[key]

    totalSteps = step1 + step2
    if (totalSteps < minTotalSteps and totalSteps != 0):
      minTotalSteps = totalSteps

  return minTotalSteps

result = crossedWires()
print('It took', time.time()-start, 'seconds.')
print(result)
