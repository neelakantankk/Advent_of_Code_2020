import re

def parse_entry(entry):
    item = dict()
    for pair in entry.split(" "):
        item[pair[:3]] = pair[4:]

    return item

def is_valid_byr(byr):
    return len(byr) == 4 and (int(byr)>=1920 and int(byr)<=2002)

def is_valid_iyr(iyr):
    return len(iyr) == 4 and (int(iyr)>=2010 and int(iyr)<=2020)

def is_valid_eyr(eyr):
    return len(eyr) == 4 and (int(eyr)>=2020 and int(eyr)<=2030)

def is_valid_hgt(hgt):
    if hgt[-2:]=="cm":
        return int(hgt[:-2])>=150 and int(hgt[:-2])<=193
    elif hgt[-2:]=="in":
        return int(hgt[:-2])>=59 and int(hgt[:-2])<=76
    else:
        return False

def is_valid_hcl(hcl):
    return re.match(r"#[0-9a-f]{6}",hcl) is not None

def is_valid_ecl(ecl):
    valid_ecl = ['amb', 'blu','brn', 'gry', 'grn', 'hzl', 'oth']
    return ecl in valid_ecl

def is_valid_pid(pid):
    return len(pid)==9 and re.match(r"\d{9}",pid) is not None

validators = {
        'byr':is_valid_byr,
        'iyr':is_valid_iyr,
        'eyr':is_valid_eyr,
        'hgt':is_valid_hgt,
        'hcl':is_valid_hcl,
        'ecl':is_valid_ecl,
        'pid':is_valid_pid,
        }


def is_valid_entry(entry):
    flag = True
    for key,value in validators.items():
        flag = flag and value(entry[key])

    return flag

def main():
    with open("input","r") as infile:
        data = infile.read()

    entries = [line.replace("\n"," ").strip() for line in data.split("\n\n")]
    with open("temp","w") as ofile_temp:
        ofile_temp.write('\n'.join(entries))

    fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']

    valid_fields = list()

    for entry in entries:
        item = parse_entry(entry)
        if len(item.keys()) < 8:
            missing = list(set(fields) - set(item.keys()))
            if len(missing) == 1:
                if missing[0] != 'cid':
                    continue
            else:
                continue

        valid_fields.append(item)

    valid = 0
    for entry in valid_fields:
        if is_valid_entry(entry):
            valid+=1

    print(valid)

if __name__ == "__main__":
    main()
