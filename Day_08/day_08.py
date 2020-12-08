def main():
    with open('input.txt','r') as infile:
        instructions = [(inst,int(value)) for inst,value in (
            tuple(line.strip().split(" ")) for line in infile.readlines())]

    acc = 0
    index = 0
    index_of_executed_instructions = []

    while True:
        if index in index_of_executed_instructions:
            break
        inst,value = instructions[index]
        if inst == 'nop':
            index_of_executed_instructions.append(index)
            index += 1
        elif inst == 'acc':
            acc += value
            index_of_executed_instructions.append(index)
            index += 1
        elif inst == 'jmp':
            index_of_executed_instructions.append(index)
            index += value

    print(acc)

if __name__ == '__main__':
    main()