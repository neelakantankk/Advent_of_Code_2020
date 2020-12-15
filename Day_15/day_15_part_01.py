def main():
    input_string = "11,18,0,20,1,7,16"
    #input_string = "0,3,6"
    numbers = {int(i):index 
            for index,i in enumerate(input_string.split(","),start=1)}

    n = len(numbers)+1
    number_to_be_spoken = 0

    while n<=2020:

        if number_to_be_spoken in numbers.keys():
            next_number = n - numbers[number_to_be_spoken]
            numbers[number_to_be_spoken] = n
            number_to_be_spoken = next_number
        else:
            numbers[number_to_be_spoken] = n
            number_to_be_spoken = 0
        n+=1
            



if __name__ == '__main__':
    main()
