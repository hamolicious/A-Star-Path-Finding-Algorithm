from vector import Vec2d


def xy_to_index(x: int, y: int, width: int) -> int:
	return int(x + width * y);

def vec_in_bounds(pos: Vec2d, bounds: Vec2d) -> bool:
	return \
		pos.x > 0 and pos.x < bounds.w and \
		pos.y > 0 and pos.y < bounds.h

