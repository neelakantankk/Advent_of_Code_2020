def main():
    passwords = list()

    with open('input','r') as infile:
        for line in infile.readlines():
            passwords.append(line.strip().replace(":","").split(" "))

    num_pass = 0


    for entry in passwords:
        lower,upper = ((int(x) - 1) for x in entry[0].split("-"))

        char_at_lower_true = entry[2][lower] == entry[1]
        char_at_upper_true = entry[2][upper] == entry[1]

        if char_at_lower_true ^ char_at_upper_true:
            num_pass += 1
        
    
    print(num_pass)

if __name__ == '__main__':
    main()

