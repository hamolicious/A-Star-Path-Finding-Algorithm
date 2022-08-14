from vector import Vec2d


class CellType:
	wall = 'wall'
	walkable = 'walkable'

class Neighbors:
	cardinal_only = [
		Vec2d( 0, -1),
		Vec2d( 1,  0),
		Vec2d( 0,  1),
		Vec2d(-1,  0),
	]

	cardinal_and_diagonal = [
		Vec2d( 0, -1),
		Vec2d( 1, -1),
		Vec2d( 1,  0),
		Vec2d( 1,  1),
		Vec2d( 0,  1),
		Vec2d(-1,  1),
		Vec2d(-1,  0),
		Vec2d(-1, -1),
	]

