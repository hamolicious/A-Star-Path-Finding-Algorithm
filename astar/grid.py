from typing import Iterable
from vector import Vec2d

from .exceptions import OutOfGrid

from .cell import Cell
from .constants import CellType
from .node import Node
from .utils import xy_to_index, vec_in_bounds


class Grid:
	def __init__(self, width: int, height: int) -> None:
		self.size = Vec2d(width, height)

		self.__grid = self.__generate_grid()

	def __generate_grid(self) -> list[Cell]:
		output = []
		for i in range(self.size.h):
			for j in range(self.size.w):
				output.append(
					Cell(
						Vec2d(j, i),
						CellType.walkable,
					)
				)
		return output

	def get_cell_at(self, pos: Vec2d) -> Cell:
		if not vec_in_bounds(pos, self.size):
			raise OutOfGrid(f'Position [{pos.as_ints()}] is out of bounds of grid')

		index = xy_to_index(pos.x, pos.y, self.size.w)
		return self.__grid[index]

	def get_all_cells(self) -> Iterable[Cell]:
		return iter(self.__grid)
