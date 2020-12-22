import time

def play_game(player_1,player_2):
    all_rounds = {1:[],2:[]}
    recursive_hand = False
    while len(player_1) != 0 and len(player_2) != 0 and not recursive_hand:
        if tuple(player_1) in all_rounds[1] and tuple(player_2) in all_rounds[2]:
            recursive_hand = True
            return (1,player_1)
        else:
            all_rounds[1].append(tuple(player_1))
            all_rounds[2].append(tuple(player_2))

        card_player_1 = player_1.pop(0)
        card_player_2 = player_2.pop(0)

        if len(player_1) >= card_player_1 and len(player_2) >= card_player_2:
            round_winner,winning_hand = play_game(player_1[:card_player_1].copy(),player_2[:card_player_2].copy())
        elif card_player_1 > card_player_2:
            round_winner = 1
        else:
            round_winner = 2
        
        if round_winner == 1:
            player_1.append(card_player_1)
            player_1.append(card_player_2)
        else:
            player_2.append(card_player_2)
            player_2.append(card_player_1)


    if len(player_1) == 0:
        winner = (2,player_2)
    else:
        winner = (1,player_1)
    return winner

def main():
    filename = 'input'
    #filename = 'example'
    START = time.perf_counter()
    with open(filename,'r') as infile:
        entries = [line.strip() for line in infile.read().strip().split("\n\n")]


    player_1 = [int(i) for i in entries[0].split("\n")[1:]]
    player_2 = [int(i) for i in entries[1].split("\n")[1:]]

    player, winner = play_game(player_1,player_2)

    score = 0
    for index,i in enumerate(winner[::-1],start=1):
        score+= index*i

    print(score)
    END = time.perf_counter()
    print(f"Part 2 took {END - START} seconds")

if __name__ == '__main__':
    main()
