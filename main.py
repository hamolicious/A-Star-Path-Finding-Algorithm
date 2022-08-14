from random import randint
import pygame
from vector import Vec2d

from astar import CellType, Grid, Neighbors, Node, PathFinder

pygame.init()
pygame.font.init()

screen_size = Vec2d(700, 700)
screen = pygame.display.set_mode(screen_size.as_ints())
pygame.display.set_caption('')

clock = pygame.time.Clock()
fps = 60

# create points a and b
a = Node([0, 0])
b = Node([15, 15])

grid = Grid(20, 20)

for cell in grid.get_all_cells():
	if randint(0, 100) < 20:
		cell.set_type(CellType.wall)

path_finder = PathFinder(grid, Neighbors.cardinal_only)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	screen.fill(0)

	if pygame.key.get_pressed()[pygame.K_SPACE]:
		# create points a and b
		a = Node([0, 0])
		b = Node([15, 15])

		grid = Grid(20, 20)

		for cell in grid.get_all_cells():
			if randint(0, 100) < 20:
				cell.set_type(CellType.wall)

		path_finder = PathFinder(grid, Neighbors.cardinal_and_diagonal)


	cell_size = screen_size.div(grid.size)
	for cell in grid.get_all_cells():
		if cell.get_type() == CellType.walkable:
			pygame.draw.rect(screen, [51, 51, 51], (
				cell.pos.mult(cell_size).as_ints(),
				cell_size.as_ints()
			), 2)
		else:
			pygame.draw.rect(screen, [71, 71, 71], (
				cell.pos.mult(cell_size).as_ints(),
				cell_size.as_ints()
			))

	pygame.draw.circle(screen, [0, 255, 0], a.pos.mult(cell_size).add(cell_size.div(2)).as_ints(), int(cell_size.w * 0.45))
	pygame.draw.circle(screen, [0, 0, 255], b.pos.mult(cell_size).add(cell_size.div(2)).as_ints(), int(cell_size.w * 0.45))

	path = path_finder.path_find(a, b)
	for p in path:
		pygame.draw.circle(screen, [255, 0, 0], p.mult(cell_size).add(cell_size.div(2)).as_ints(), int(cell_size.w * 0.30))

	pygame.display.update()
	clock.tick(fps)
