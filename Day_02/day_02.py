def main():
    passwords = list()

    with open('input','r') as infile:
        for line in infile.readlines():
            passwords.append(line.strip().replace(":","").split(" "))

    num_pass = 0


    for entry in passwords:
        lower,upper = (int(x) for x in entry[0].split("-"))
        count = entry[2].count(entry[1])
        if count >= lower and count <= upper:
            print(entry[2])
            num_pass +=1
    
    print(num_pass)

if __name__ == '__main__':
    main()

