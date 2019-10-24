import pygame
from nodeClass import Node
from math import sqrt
from random import randint, choice
import button
import start_end_nodes

pygame.init()
pygame.font.init()

size = [1300, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('')

clock = pygame.time.Clock()
fps = 60

# create points a and b
a = start_end_nodes.Node(20, 20, 0)
b = start_end_nodes.Node(660, 660, 1)

# generate a node grid
grid = []
snap = []
for i in range(0, 700, 20):
    for j in range(0, 700, 20):
        grid.append(Node(j, i, 'hidden', a, b))
        snap.append(pygame.Rect(j, i, 20, 20))

# init open and closed lists
open_nodes = []
closed_nodes = []

# find starting grid
for cell in grid:
    if cell.g == 0:
        start_node = grid.index(cell)

done = False

#region Buttons

    # assign a font
font = pygame.font.SysFont('ariel', 30)

    # exec button
btn_start = button.Button([51,51,51], [70,70,70], 800, 20, 200, 50, font, 'Start')

btn_inc = button.Button([51,51,51], [70,70,70], 800, 100, 100, 50, font, '      /\\')
btn_dec = button.Button([51,51,51], [70,70,70], 800, 170, 100, 50, font, '      \\/')
#endregion

    # delay
counter = 0
step = 0
    #ui manager

doOnce = 0

def uiDraw(screen):
    screen.fill(0)

    pygame.draw.rect(screen, [51, 51, 51], (0, 0, 700, 700), 1)
    pygame.draw.line(screen, [51, 51, 51], (710, 90), (1280, 90), 2)

    btn_start.show(screen)
    btn_dec.show(screen)
    btn_inc.show(screen)

    screen.blit(font.render('Delay {}'.format(counter), 1, [255, 255, 255]), (710, 135))

    a.show(screen)
    b.show(screen)

start = False

locations = []

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()

    if not start:
        uiDraw(screen)

            # mouse pos
        pos = pygame.mouse.get_pos()
            # mouse key presses
        pressed = pygame.mouse.get_pressed()
            # keyboard key presses
        key = pygame.key.get_pressed()

        uiDraw(screen)

        #region Buttons
        btn_start.onHover(pos)
        if btn_start.onPressed(pos, pressed):
            start = True

        btn_inc.onHover(pos)
        if btn_inc.onPressed(pos, pressed):
            counter += 1
        
        btn_dec.onHover(pos)
        if btn_dec.onPressed(pos, pressed):
            counter -= 1
        #endregion

        if a.update(pos, pressed, snap) == False and b.update(pos, pressed, snap) == False:
            if pressed == (1, 0, 0):
                index = pygame.Rect(pos[0], pos[1], 1, 1).collidelist(snap)

                if snap[index][0] != a.x or snap[index][0] != b.x or snap[index][1] != a.y or snap[index][1] != b.y:
                    locations.append(snap[index])

        temp = []
        for loc in locations:
            pygame.draw.rect(screen, [100, 100, 100], loc, 0)

            if (loc[0] == a.x and loc[1] == a.y) or (loc[0] == b.x and loc[1] == b.y):
                pass
            else:
                temp.append(loc)
        locations = temp

    if start and doOnce == 0:
        for node in grid:
            node.recalculate(a, b)

            for loc in locations:
                if node.x == loc[0] and node.y == loc[1]:
                    node.mode = 'wall'
        
            if node.g == 0:
                start_node = grid.index(node)

        if counter < 0:
            counter = 0

        # add starting node to open list 
        open_nodes.append(grid[start_node])
        grid[start_node].mode = 'open'

        doOnce += 1

    if start:
        if step == counter:
            #region A* Path
            if len(open_nodes) == 0:
                break

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
            #endregion
            step = 0
        else:
            step += 1

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
