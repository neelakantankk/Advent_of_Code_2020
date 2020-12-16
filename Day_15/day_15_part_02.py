import time
def main():
    input_string = "11,18,0,20,1,7,16"
    #input_string = "0,3,6"
    START = time.perf_counter()
    numbers = {int(i):index 
            for index,i in enumerate(input_string.split(","),start=1)}

    n = len(numbers)+1
    number_to_be_spoken = 0
    all_nums = [int(i) for i in input_string.split(",")]

    while n<30000000:
        all_nums.append(number_to_be_spoken)
        if number_to_be_spoken in numbers.keys():
            next_number = n - numbers[number_to_be_spoken]
            numbers[number_to_be_spoken] = n
            number_to_be_spoken = next_number
        else:
            numbers[number_to_be_spoken] = n
            number_to_be_spoken = 0
        n+=1

    print(number_to_be_spoken)
    END = time.perf_counter()
    print(f"Time Taken: {END - START}")



if __name__ == '__main__':
    main()
