import pygame
from nodeClass import Node
from math import sqrt
from random import randint, choice

pygame.init()

size = [700, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('')

clock = pygame.time.Clock()
fps = 30

# create points a and b
a, b = None, None

xs = []
ys = []

for i in range(0, 700, 20):
    for j in range(0, 700, 20):
        xs.append(j)
        ys.append(i)

a = pygame.math.Vector2(choice(xs), choice(ys))
b = pygame.math.Vector2(choice(xs), choice(ys))

# generate a node grid
grid = []
for i in range(0, 700, 20):
    for j in range(0, 700, 20):
        if randint(0, 10) > 6 and j != a.x and i != a.y and j != b.x and i != b.y:
            grid.append(Node(j, i, 'wall', a, b))
        else:
            grid.append(Node(j, i, 'hidden', a, b))

# init open and closed lists
open_nodes = []
closed_nodes = []

# find starting grid
for cell in grid:
    if cell.g == 0:
        start_node = grid.index(cell)

# add starting node to open list 
open_nodes.append(grid[start_node])
grid[start_node].mode = 'open'

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()

    if len(open_nodes) == 0:
        done = True

    # show nodes
    for cell in grid:
        cell.show(screen)

    # show a and b points
    pygame.draw.rect(screen, [255, 255, 0], (a.x, a.y, 20, 20))
    pygame.draw.rect(screen, [255, 0, 255], (b.x, b.y, 20, 20))

    # look for lowest f cost
    lowestF = 10**10
    lowestH = 10**10
    for node in open_nodes:
        if node.f < lowestF:
            lowestF = node.f
            lowestH = node.h
            current_node = node

        if lowestF == node.f:
            if node.h < lowestH:
                lowestF = node.f
                lowestH = node.h
                current_node = node

    # switch lists 
    open_nodes.remove(current_node)
    closed_nodes.append(current_node)
    current_node.mode = 'closed'

    # look for neighbours
    temp = []
    for node in grid:
        if node.x == current_node.x + 20 and node.y == current_node.y:
            temp.append(node)

        if node.x == current_node.x - 20 and node.y == current_node.y:
            temp.append(node)

        if node.x == current_node.x and node.y == current_node.y + 20:
            temp.append(node)

        if node.x == current_node.x and node.y == current_node.y - 20:
            temp.append(node)

        # hash out these to allow only 4 directional movement
        # if node.x == current_node.x + 20 and node.y == current_node.y + 20:
        #     temp.append(node)

        # if node.x == current_node.x + 20 and node.y == current_node.y - 20:
        #     temp.append(node)

        # if node.x == current_node.x - 20 and node.y == current_node.y + 20:
        #     temp.append(node)

        # if node.x == current_node.x - 20 and node.y == current_node.y - 20:
        #     temp.append(node)

    # add neighbour to open list if not there and parent this node to the current node
    for node in temp:
        if closed_nodes.count(node) == 0 and node.mode != 'wall':
            if open_nodes.count(node) == 0:
                open_nodes.append(node)
                node.mode = 'open'

            node.parent = current_node

    # if node end is found, break
    if current_node.x == b.x and current_node.y == b.y:
        done = True

    pygame.display.update()
    clock.tick(fps)

path = []
x, y = current_node.x, current_node.y
while True:
    path.append((x + 10, y + 10))
    x, y = current_node.parent.x, current_node.parent.y

    current_node = current_node.parent

    if x == a.x and y == a.y:
        break
path.append((a.x + 10, a.y + 10))
path.reverse()

step = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()

    mousePos = pygame.mouse.get_pos()

    # show nodes
    for cell in grid:
        cell.show(screen)
        cell.update(mousePos)

    # draw path
    for i in range(0, len(path) - 1):
        pygame.draw.line(screen, [0, 0, 200], path[i], path[i + 1], 5)

    # show a and b points
    pygame.draw.rect(screen, [255, 255, 0], (a.x, a.y, 20, 20))
    pygame.draw.rect(screen, [255, 0, 255], (b.x, b.y, 20, 20))

    pygame.draw.circle(screen, [255, 255, 255], (int(path[step][0]), int(path[step][1])), 5)

    if step != len(path) - 1:
        step += 1
    else:
        step = 0

    pygame.display.update()
    clock.tick(fps)
