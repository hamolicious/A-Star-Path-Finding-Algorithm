from vector import Vec2d


class Cell:
	def __init__(self, pos: Vec2d, type_of_cell: str) -> None:
		self.pos = Vec2d(pos)
		self.__type = type_of_cell

	def get_type(self) -> str:
		return self.__type

	def set_type(self, new_type) -> None:
		self.__type = new_type


