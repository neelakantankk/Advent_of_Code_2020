import time
from pprint import pprint

def main():
    filename = 'input'
    with open(filename,'r') as infile:
        jolts = [int(line.strip()) for line in infile.readlines()]

    #PART 1
    START = time.perf_counter_ns()
    
    jolts.append(0)

    jolts_sorted = sorted(jolts)
    jolts_sorted.append(jolts_sorted[-1]+3)

    diffs = {1:0, 2:0, 3:0}

    for index,jolt in enumerate(jolts_sorted[:-1]):
        diff = jolts_sorted[index+1] - jolt
        diffs[diff]+=1


    print(diffs[1] * diffs[3])
    END = time.perf_counter_ns()
    print(f"Time taken for Part 1: {END - START} nanoseconds")

    #PART 2
    START = time.perf_counter_ns()
    graph = {}
    for jolt in jolts_sorted:
        diffs = [(jolt+x) for x in (1,2,3)]
        diffs = [y for y in jolts_sorted if y in diffs]
        graph[jolt] = diffs

    solution = {0:1}
    for key,value in graph.items():
        if value == []:
            break
        for val in value:
            if val in solution.keys():
                solution[val]+=solution[key]
            else:
                solution[val]=solution[key]
    
    print(solution[jolts_sorted[-1]])
    END = time.perf_counter_ns()

    print(f"Time taken for part 2: {END - START} nanoseconds")

if __name__ == '__main__':
    main()

