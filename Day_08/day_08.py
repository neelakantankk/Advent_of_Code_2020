def main():

    with open('input.txt','r') as infile:
        instructions = [(inst,int(value)) for inst,value in (
            tuple(line.strip().split(" ")) for line in infile.readlines())]

    def execute(instructions):
        acc = 0
        index = 0
        index_of_executed_instructions = []

        while index<len(instructions):
            if index in index_of_executed_instructions:
                return ('loop',acc)
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
        return ('term',acc)

    index_of_op = 0
    while True:
        old_inst = instructions[index_of_op]
        if old_inst[0] == 'jmp':
            new_inst = ('nop',old_inst[1])
            instructions[index_of_op] = new_inst
        elif old_inst[0] == 'nop':
            new_inst = ('jmp',old_inst[1])
            instructions[index_of_op] = new_inst
        result = execute(instructions)
        if result[0] == 'term':
            print(result[1])
            break
        instructions[index_of_op] = old_inst
        index_of_op += 1

if __name__ == '__main__':
    main()