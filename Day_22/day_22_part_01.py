import time

def main():
    filename = 'input'
    #filename = 'example'

    START = time.perf_counter_ns()

    with open(filename,'r') as infile:
        entries = [line.strip() for line in infile.read().strip().split("\n\n")]


    player_1 = [int(i) for i in entries[0].split("\n")[1:]]
    player_2 = [int(i) for i in entries[1].split("\n")[1:]]

    while len(player_1) != 0 and len(player_2) != 0:
        card_player_1 = player_1.pop(0)
        card_player_2 = player_2.pop(0)

        if card_player_1 > card_player_2:
            player_1.append(card_player_1)
            player_1.append(card_player_2)
        else:
            player_2.append(card_player_2)
            player_2.append(card_player_1)

    if len(player_1) == 0:
        winner = player_2
    else:
        winner = player_1

    score = 0
    for index,i in enumerate(winner[::-1],start=1):
        score+= index*i

    print(score)
    END = time.perf_counter_ns()
    print(f"Part 1 took {END - START} nanoseconds")

if __name__ == '__main__':
    main()
