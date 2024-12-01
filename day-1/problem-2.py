data = open('day-1/input.txt', 'r').read().split('\n')

left_column = []
right_column = []
similarity_score = 0

for line in data:
  if line:
    arr = line.split('   ')
    left_column.append(int(line.split('   ')[0]))
    right_column.append(int(line.split('   ')[1]))

for l_id in left_column:
  occurence = 0
  for r_id in right_column:
    if l_id == r_id:
      occurence += 1
  similarity_score += l_id * occurence

print(similarity_score)