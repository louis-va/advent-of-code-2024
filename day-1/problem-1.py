data = open('day-1/input.txt', 'r').read().split('\n')

left_column = []
right_column = []
total_distance = 0

for line in data:
  if line:
    arr = line.split('   ')
    left_column.append(int(line.split('   ')[0]))
    right_column.append(int(line.split('   ')[1]))

left_column.sort()
right_column.sort()

for x in range(len(left_column)):
  distance = abs(left_column[x] - right_column[x])
  total_distance += distance

print(total_distance)