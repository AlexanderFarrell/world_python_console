tile_types = [
    ['🔲', True],
    ['⬜️️', False],
    ['💎', True]
]
world = []
width = 32
height = 32


def create_world():
    for x in range(width):
        world.append([])
        for y in range(height):
            world[x].append(2)


def draw_world():
    for x in range(width):
        for y in range(height):
            print(tile_types[world[x][y]][0], end='')
        print()


create_world()
draw_world()