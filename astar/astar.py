from vector import Vec2d

from .constants import CellType, Neighbors
from .grid import Grid
from .node import Node
from .utils import vec_in_bounds


class PathFinder:
	def __init__(self, grid: Grid, neighbors_search_pattern: list[Vec2d]) -> None:
		self.grid = grid
		self.__neighbors_search_pattern = neighbors_search_pattern

	def __get_node_lowest_f(self, arr: list[Node]) -> Node:
		arr.sort(
			key=lambda x : x.f
		)
		return arr[0]

	def __backtrack_from(self, node: Node) -> list[Vec2d]:
		path = []

		while node is not None:
			path.append(node.pos)
			node = node.parent

		return path[::-1]

	def path_find(self, start_node: Node, end_node: Node) -> list[Vec2d]:
		open_list = []
		closed_list = []

		open_list.append(start_node)

		while len(open_list) > 0:
			current_node = self.__get_node_lowest_f(open_list)

			open_list.remove(current_node)
			closed_list.append(current_node)

			if current_node == end_node:
				return self.__backtrack_from(current_node)

			children = []
			for pos in self.__neighbors_search_pattern:
				new_pos = current_node.pos.add(pos)

				if not vec_in_bounds(new_pos, self.grid.size):
					continue

				if self.grid.get_cell_at(new_pos).get_type() == CellType.wall:
					continue

				new_node = Node(new_pos)
				new_node.parent = current_node
				children.append(new_node)

			for child in children:
				if child in closed_list:
					continue

				child.recalculate(start_node, end_node)

				if child not in open_list:
					open_list.append(child)

		return []



