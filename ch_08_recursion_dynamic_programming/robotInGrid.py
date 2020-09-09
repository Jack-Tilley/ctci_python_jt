grid = [
    [True, False, False],
    [True, True, False],
    [False, True, True]
]
r = len(grid) - 1
c = len(grid[0]) - 1
end = (0, 0)
start = (r, c)
pos = start
path = [start]
badsquares = []

def roboGrid(grid, pos, path, badsquares):

