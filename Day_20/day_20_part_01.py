import pprint
import time
from functools import reduce

def main():
    filename = "input"
    #filename = "example"
    START = time.perf_counter_ns()
    with open(filename,'r') as infile:
        entries = [entry.strip() for entry in infile.read().strip().split("\n\n")]

    tiles = {int(tile.split(" ")[1]):pattern.strip() for tile,pattern in (entry.split(":") for entry in entries)}

    tile_edges = dict()
    for tile,pattern in tiles.items():
        lines = pattern.split("\n")
        top_edge = lines[0]
        bottom_edge = lines[-1]
        left_edge = ''.join(l[0] for l in lines)
        right_edge = ''.join(l[-1] for l in lines)
        left_flipped = ''.join(reversed(left_edge))
        right_flipped = ''.join(reversed(right_edge))
        top_flipped = ''.join(reversed(top_edge))
        bottom_flipped = ''.join(reversed(bottom_edge))
        tile_edges[tile] = [top_edge,bottom_edge,left_edge,right_edge,left_flipped, right_flipped, top_flipped, bottom_flipped]
    all_tiles = set(tiles.keys())

    corner_tiles = []
    diffs = set()
    for tile,edges in tile_edges.items():
        number_of_unmatched_edges = 0
        all_other_tiles = all_tiles - {tile}
        all_other_edges = set()
        for key in all_other_tiles:
            all_other_edges.update(tile_edges[key])
        current_edges = set(edges)
        diff = current_edges - all_other_edges
        diffs.add(len(diff))
        if len(diff) == 4:
            corner_tiles.append(tile)

    print(reduce(lambda x,y: x*y,corner_tiles))
    END = time.perf_counter_ns()

    print(f"Part 1 took {END - START} nanoseconds")

if __name__ == '__main__':
    main()


