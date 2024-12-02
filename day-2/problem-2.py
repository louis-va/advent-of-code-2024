data = open('day-2/input.txt', 'r').read().split('\n')

safe_reports = 0

def is_increasing(array):
  for x in range(len(array)-1):
    if array[x] < array[x+1]:
      return False
  return True

def is_decreasing(array):
  for x in range(len(array)-1):
    if array[x] > array[x+1]:
      return False
  return True

def is_differing_safely(array):
  for x in range(len(array)-1):
    if abs(array[x] - array[x+1]) <= 0 or abs(array[x] - array[x+1]) > 3:
      return False
  return True

def is_report_safe(levels):
  for x in range(len(levels)):
    arr = levels[:x] + levels[x + 1:]
    if (is_increasing(arr) or is_decreasing(arr)) and is_differing_safely(arr):
      return True
  return False

for report in data:
  if report:
    levels = list(map(int, report.split()))
    if is_report_safe(levels):
      safe_reports += 1

print(safe_reports)