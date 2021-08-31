from queue import PriorityQueue

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


def dijkstra(draw, grid, start, end):
    open_set = PriorityQueue()

    count = 0

    distance_score = {node: float("inf") for row in grid for node in row}

    path = {node: None for row in grid for node in row}

    distance_score[start] = 0
    open_set.put((distance_score[start], count, start))

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        current = open_set.get()[2]

        if current == end:
            reconstruct_path(path, current, draw, start, end)
            return True

        for neighbour in current.neighbours:
            if path[neighbour]:
                continue

            if distance_score[current] + 1 < distance_score[neighbour]:
                distance_score[neighbour] = distance_score[current] + 1

                count += 1
                open_set.put((distance_score[neighbour], count, neighbour))
                path[neighbour] = current
                neighbour.make_open()

        draw()

        current.make_end()

    return False
