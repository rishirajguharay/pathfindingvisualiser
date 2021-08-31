from queue import LifoQueue

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
def depth_first_search(draw, grid, start, end):

    open_set = LifoQueue()
    open_set.put(start)

    path = {node: None for row in grid for node in row}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


        current = open_set.get()

        if current == end:
            reconstruct_path(path, current, draw, start, end)
            return True

        for neighbour in current.neighbours:

            if path[neighbour]:
                continue

            if not neighbour == start:
                open_set.put(neighbour)
                neighbour.make_open()
                path[neighbour] = current

        draw()

        current.make_close()

    return False