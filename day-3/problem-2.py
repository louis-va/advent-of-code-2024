import re
data = open('day-3/input.txt', 'r').read()

MUL_PATTERN = r"mul\(\d+,\d+\)"
DONT_DO_PATTERN = r"don't\(\).*?do\(\)"

def mul(a, b):
  return a * b

def restore(memory):
  match = re.search(MUL_PATTERN, memory)
  if (match):
    memory = memory.replace(match.group(), "", 1)
    return eval(match.group()) + restore(memory)
  else:
    return 0
  
def disable_instructions(memory):
  matches = re.findall(DONT_DO_PATTERN, memory)
  if (matches):
    for match in matches:
      memory = memory.replace(match, "", 1)
  return memory
  
print(restore(disable_instructions(data)))
