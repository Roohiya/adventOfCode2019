import copy
import sys

f = open('input-test.txt', 'r')

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
  centralPort1 = [0, 0]
  centralPort2 = [0, 0]

  for point in wire1:
    direction = point[:1]
    steps = int(point[1:])

    if (direction == 'R'):
      for step in range(steps):
        fullKey = ','.join(list(map(str, centralPort1)))
        if (fullKey not in coords):
          coords[fullKey] = 1
        centralPort1[0] += 1
    elif (direction == 'L'):
      for step in range(steps):
        fullKey = ','.join(list(map(str, centralPort1)))
        if (fullKey not in coords):
          coords[fullKey] = 1
        centralPort1[0] -= 1
    elif (direction == 'U'):
      for step in range(steps):
        fullKey = ','.join(list(map(str, centralPort1)))
        if (fullKey not in coords):
          coords[fullKey] = 1
        centralPort1[1] += 1
    elif (direction == 'D'):
      for step in range(steps):
        fullKey = ','.join(list(map(str, centralPort1)))
        if (fullKey not in coords):
          coords[fullKey] = 1
        centralPort1[1] -= 1

  for point in wire2:
    direction = point[:1]
    steps = int(point[1:])

    if (direction == 'R'):
      for step in range(steps):
        fullKey = ','.join(list(map(str, centralPort2)))
        if (fullKey in coords):
          coords[fullKey]+= 1
        centralPort2[0] += 1
    elif (direction == 'L'):
      for step in range(steps):
        fullKey = ','.join(list(map(str, centralPort2)))
        if (fullKey in coords):
          coords[fullKey] += 1
        centralPort2[0] -= 1
    elif (direction == 'U'):
      for step in range(steps):
        fullKey = ','.join(list(map(str, centralPort2)))
        if (fullKey in coords):
          coords[fullKey] += 1
        centralPort2[1] += 1
    elif (direction == 'D'):
      for step in range(steps):
        fullKey = ','.join(list(map(str, centralPort2)))
        if (fullKey in coords):
          coords[fullKey] += 1
        centralPort2[1] -= 1

  intersection = []
  what = []
  for key, value in coords.items():
    if (value > 1):
      what.append(key)
      intersection.append(sum(list(map(abs, list(map(int, key.split(',')))))))

  return sorted(intersection)[1]

result = crossedWires()
print(result)
