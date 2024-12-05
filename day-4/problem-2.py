from typing import List

def is_in_bounds(row, col, grid):
  return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def search(grid: List[List[str]]) -> int:
  words = 0
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if (
        is_in_bounds(row + 1, col + 1, grid) and
        is_in_bounds(row + 1, col - 1, grid) and
        is_in_bounds(row - 1, col + 1, grid) and
        is_in_bounds(row - 1, col - 1, grid)
      ):
        if (
          grid[row][col] == "A" and
          ((grid[row-1][col-1] + grid[row+1][col+1]) in {"MS", "SM"}) and
          ((grid[row-1][col+1] + grid[row+1][col-1]) in {"MS", "SM"})
        ):
          words += 1
  return words

data = open('day-4/input.txt', 'r').read().split('\n')
grid = [list(row.strip()) for row in data if row.strip()]

print(search(grid))
