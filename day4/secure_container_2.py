import copy
import sys

f = open('input.txt', 'r')

contents = ''

if f.mode == 'r':
  contents = f.read()

start = int(contents.split('-')[0])
end = int(contents.split('-')[1])

def check_sorted (num):
  return sorted(list(num)) == list(num)

def check_adjacent_chars (num):
  point = 1

  count = 1

  while point < len(num):
    if (num[point] == num[point-1]):
      count += 1
    else:
      if (count == 2):
        return True
      count = 1
    point += 1

  if (count == 2):
    return True
  return False

def secure_container ():
  count = 0

  for i in range(start, end+1):
    isSorted = check_sorted(str(i))
    hasSameAdjacentChars = check_adjacent_chars(str(i))

    if (isSorted and hasSameAdjacentChars):
      count += 1

  return count

result = secure_container()
print(result)
