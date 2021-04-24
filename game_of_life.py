import pygame
import sys
import math
import random

ROWS = 40
COLS = 40
OLD_GRID = []
NEW_GRID = []
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (220, 220, 220)
LENGTH = 800

class cell:

  def __init__(self, x, y, w, h, status):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.status = status
    self.has_neighbor_top = True
    self.has_neighbor_bottom = True
    self.has_neighbor_right = True
    self.has_neighbor_left = True
    self.nb_neighbors = 0

  def show(self):
    color = WHITE
    if self.status == 1:
      color = BLACK
    rect = pygame.Rect(self.x, self.y, (self.w - 1), (self.h - 1))
    pygame.draw.rect(SCREEN, color, rect)

  def set_neighbors(self, i, j, cols, rows):
    if i == 0:
      self.has_neighbor_top = False
    if i == (rows - 1):
      self.has_neighbor_bottom = False
    if j == 0:
      self.has_neighbor_left = False
    if j == (cols - 1):
      self.has_neighbor_right = False

  def update_nb_neighbors(self, grid, i, j):
    if self.has_neighbor_left:
      self.nb_neighbors += grid[i][j - 1].status
    if self.has_neighbor_right:
      self.nb_neighbors += grid[i][j + 1].status
    if self.has_neighbor_top:
      self.nb_neighbors += grid[i - 1][j].status
      if self.has_neighbor_left:
        self.nb_neighbors += grid[i - 1][j - 1].status
      if self.has_neighbor_right:
        self.nb_neighbors += grid[i - 1][j + 1].status
    if self.has_neighbor_bottom:
      self.nb_neighbors += grid[i + 1][j].status
      if self.has_neighbor_left:
        self.nb_neighbors += grid[i + 1][j - 1].status
      if self.has_neighbor_right:
        self.nb_neighbors += grid[i + 1][j + 1].status

def main():
  OLD_GRID = []
  global SCREEN, CLOCK
  pygame.init()
  SCREEN = pygame.display.set_mode((LENGTH, LENGTH))
  CLOCK = pygame.time.Clock()
  SCREEN.fill(GREY)
  h = LENGTH / ROWS
  w = LENGTH / COLS
  for i in range(ROWS):
    OLD_GRID.append([])
  for i in range(ROWS):
    for j in range(COLS):
      OLD_GRID[i].append(cell((w * i), (h * j), w, h, math.floor(random.randrange(0, 2))))
  while True:
    for i in range(ROWS):
      for j in range(COLS):
        OLD_GRID[i][j].show()
        OLD_GRID[i][j].set_neighbors(i, j, COLS, ROWS)
        OLD_GRID[i][j].update_nb_neighbors(OLD_GRID, i, j)
    NEW_GRID = OLD_GRID
    for i in range(ROWS):
      for j in range(COLS):
        if OLD_GRID[i][j].status == 0 and OLD_GRID[i][j].nb_neighbors == 3:
          NEW_GRID[i][j].status = 1
          NEW_GRID[i][j].nb_neighbors = 0
        else:
          if OLD_GRID[i][j].status == 1:
            if OLD_GRID[i][j].nb_neighbors < 2 or OLD_GRID[i][j].nb_neighbors > 3:
              NEW_GRID[i][j].status = 0
              NEW_GRID[i][j].nb_neighbors = 0
            else:
              NEW_GRID[i][j].status = OLD_GRID[i][j].status
              NEW_GRID[i][j].nb_neighbors = 0
          else:
            NEW_GRID[i][j].status = OLD_GRID[i][j].status
            NEW_GRID[i][j].nb_neighbors = 0
    OLD_GRID = NEW_GRID
    pygame.display.update()

main()