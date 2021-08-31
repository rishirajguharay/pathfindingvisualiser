from Spot import Spot
from collections import deque
import pygame


def reconstruct_path(path, current, draw, start, end):
    while current in path:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        current = path[current]
        current.make_path()
        draw()
        if current == start:
            break
    end.make_end()
    start.make_start()

def algorithm(draw, grid, start, end):
    Q = deque()
    Q.append(start)
    path = {node: None for x in grid for node in x}
    while Q:
        for event in pygame.event.get():
            if event.type == pygame.quit():
                quit()
        current = Q.popleft()
        if current == end:
            reconstruct_path(path, current, draw, start, end)
            return True
        for neighbor in current.neighbors:
            if path[neighbor]:
                continue
            if not neighbor == start:
                Q.append(neighbor)
                neighbor.make_open()
                path[neighbor] = current

        draw()
        current.make_end()
    return False
