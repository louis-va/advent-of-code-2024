from typing import List

positions = [
  {'X': [0, 0], 'M': [1, 0], 'A': [2, 0], 'S': [3, 0]},        # →
  {'X': [0, 0], 'M': [-1, 0], 'A': [-2, 0], 'S': [-3, 0]},     # ←
  {'X': [0, 0], 'M': [0, 1], 'A': [0, 2], 'S': [0, 3]},        # ↓
  {'X': [0, 0], 'M': [0, -1], 'A': [0, -2], 'S': [0, -3]},     # ↑
  {'X': [0, 0], 'M': [1, 1], 'A': [2, 2], 'S': [3, 3]},        # ↘
  {'X': [0, 0], 'M': [-1, 1], 'A': [-2, 2], 'S': [-3, 3]},     # ↙
  {'X': [0, 0], 'M': [1, -1], 'A': [2, -2], 'S': [3, -3]},     # ↗
  {'X': [0, 0], 'M': [-1, -1], 'A': [-2, -2], 'S': [-3, -3]},  # ↖
]

def is_in_bounds(row, col, grid):
  return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def search(grid: List[List[str]]) -> int:
  words = 0
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      for position in positions:
        if all(
          is_in_bounds(row + position[letter][0], col + position[letter][1], grid) and
          grid[row + position[letter][0]][col + position[letter][1]] == letter
          for letter in ["X", "M", "A", "S"]
        ):
          words += 1
  return words

data = open('day-4/input.txt', 'r').read().split('\n')
grid = [list(row.strip()) for row in data if row.strip()]

print(search(grid))
