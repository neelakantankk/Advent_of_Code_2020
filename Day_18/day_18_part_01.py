import time

def do_op(op,op1,op2):
    if op == "+":
        return op1 + op2
    else:
        return op1 * op2

def parse_line(line):
    data_stack = list()
    op_stack = list()
    index = 0
    end = len(line)
    
    while index<end:
        if line[index] == "+":
            op_stack.append("+")
        elif line[index] == "*":
            op_stack.append("*")
        elif line[index] == ")":
            return (index+1,data_stack.pop())
        elif line[index] == "(":
            to_add,result = parse_line(line[index+1:])
            if op_stack != []:
                op = op_stack.pop()
                op1 = data_stack.pop()
                result = do_op(op,op1,result)
            data_stack.append(result)
            index+=to_add
        else:
            if op_stack == []:
                data_stack.append(int(line[index]))
            else:
                op = op_stack.pop()
                op1 = data_stack.pop()
                op2 = int(line[index])
                data_stack.append(do_op(op,op1,op2))
        index += 1

    if op_stack == []:
        return data_stack.pop()
    else:
        op = op_stack.pop()
        op1 = data_stack.pop()
        op2 = data_stack.pop()
        return do_op(op,op1,op2)

def main():
    filename = 'input'
    #filename = 'example'

    START = time.perf_counter_ns()
    with open(filename,'r') as infile:
        lines = [line.strip().replace(" ",'') for line in infile.readlines()]

    sum_of_values = 0
    for line in lines:
        sum_of_values += parse_line(line)
    print(sum_of_values)
    END = time.perf_counter_ns()
    print(f"Part 1 took {END - START} nanoseconds")

if __name__ == '__main__':
    main()
