def parse_entry(entry):
    item = dict()
    for pair in entry.split(" "):
        item[pair[:3]] = pair[4:]

    return item



def main():
    with open("input","r") as infile:
        data = infile.read()

    entries = [line.replace("\n"," ") for line in data.split("\n\n")]
    with open("temp","w") as ofile_temp:
        ofile_temp.write('\n'.join(entries))

    fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']

    valid = 0

    for entry in entries:
        item = parse_entry(entry)
        if len(item.keys()) < 8:
            missing = list(set(fields) - set(item.keys()))
            if len(missing) == 1:
                if missing[0] != 'cid':
                    continue
            else:
                continue

        valid +=1

    print(valid)



if __name__ == "__main__":
    main()
