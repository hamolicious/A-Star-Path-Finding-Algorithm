from __future__ import annotations
from vector import Vec2d


class Node:
	def __init__(self, pos: Vec2d) -> None:
		self.pos = Vec2d(pos)

		self.g = 0
		self.h = 0
		self.f = 0

		# wall or node
		self.parent = None

	def recalculate(self, start_node: Node, end_node: Node) -> None:
		self.g = self.pos.dist(start_node.pos)
		self.h = self.pos.dist(end_node.pos)
		self.f = self.g + self.h

	def __eq__(self, __o: Node) -> bool:
		return self.pos.dist(__o.pos) == 0
