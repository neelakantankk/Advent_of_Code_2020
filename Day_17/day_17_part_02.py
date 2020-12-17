from itertools import product
import time

def main():
    #filename='example'
    filename = 'input'
    START = time.perf_counter_ns()
    state = dict()
    with open(filename,'r') as infile:
        for x,line in enumerate(infile.readlines()):
            for y,cube in enumerate(line.strip()):
                if cube == "#":
                    state[(x,y,0,0)] = cube
    for cycle in range(1,7):

        new_state = dict()
        x_s = [x for x,y,z,w in state.keys()]
        y_s = [y for x,y,z,w in state.keys()]
        z_s = [z for x,y,z,w in state.keys()]
        w_s = [w for x,y,z,w in state.keys()]
        min_x = min(x_s)-1
        max_x = max(x_s)+1
        min_y = min(y_s)-1
        max_y = max(y_s)+1
        min_z = min(z_s)-1
        max_z = max(z_s)+1
        min_w = min(w_s)-1
        max_w = max(w_s)+1
        
        for w in range(min_w, max_w+1):
            for z in range(min_z, max_z+1):
                for x in range(min_x,max_x+1):
                    for y in range(min_y,max_y+1):
                        pos = (x,y,z,w)
                        cube = state.get(pos,".")
                        neighbors = {val for val in product({x,x-1,x+1},{y,y-1,y+1},{z,z-1,z+1},{w,w-1,w+1})} - {pos}
                        active = [val for val in neighbors if state.get(val,".") == "#"]
                        if cube == "#" and (len(active)==2 or len(active)==3):
                            new_state[pos] = "#"
                        elif state.get(pos,".") == "." and len(active) == 3:
                            new_state[pos] = "#"
        state = new_state.copy()

    active = {pos:val for pos,val in state.items() if val == "#"}
    print(len(active))
    END = time.perf_counter_ns()
    print(f"Part 2 took {END - START} nanoseconds")

if __name__ == '__main__':
    main()
