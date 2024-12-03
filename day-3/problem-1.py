import re
data = open('day-3/input.txt', 'r').read()

PATTERN = r"mul\(\d+,\d+\)"

def mul(a, b):
  return a * b

def restore(memory):
  match = re.search(PATTERN, memory)
  if (match):
    memory = memory.replace(match.group(), "", 1)
    return eval(match.group()) + restore(memory)
  else:
    return 0
  
print(restore(data))
