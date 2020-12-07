

import sys
import numpy as np
import math

def get_expense_report():
    f=open("expensereport.txt",'r')
    exp = []
    for ex_val in f:
        ex_val = float(ex_val)
        if ex_val <= 2020:
            exp.append(ex_val)
    return exp

def advent_day1_part1():
    exp = get_expense_report()
    for ind, ex_val1 in enumerate(exp):
        for ex_val2_ind in range(ind, len(exp)):
            ex_val2 = exp[ex_val2_ind]
            # print("Sum is %s"%(ex_val1+ex_val2))
            if ex_val1 + ex_val2 == 2020:

                print("Value 1 %s and value 2 %s multiplied yields %s"% (ex_val1, ex_val2, ex_val1*ex_val2))
                return ex_val1*ex_val2

def advent_day1_part2():
    exp = get_expense_report()
    for ind, ex_val1 in enumerate(exp):
        if ex_val1 > 2020:
            continue
        for ex_val2_ind in range(ind, len(exp)):
            ex_val2 = exp[ex_val2_ind]

            if ex_val1 + ex_val2 > 2020:
                continue
            for ex_val3_ind in range(ex_val2_ind, len(exp)):
                ex_val3 = exp[ex_val3_ind]
                if ex_val1+ex_val2+ex_val3 == 2020:
                    print("Value 1 %s and value 2 %s and value 3 %s multiplied yields %s"% (ex_val1, ex_val2, ex_val3, ex_val1*ex_val2*ex_val3))
                    return int(ex_val1*ex_val2*ex_val3)

def advent_day2_part1():
    f = open("passwords.txt", 'r')
    valid_count = 0
    for line in f:
        space_split = line.split(" ")
        min_max = space_split[0].split("-")
        min_val = int(min_max[0])
        max_val = int(min_max[1])
        let = space_split[1].split(":")[0]
        let_count = space_split[2].count(let)
        if let_count >= min_val and let_count <= max_val:
            valid_count+=1
    print("valid count: ", valid_count)

def advent_day2_part2():
    f = open("passwords.txt", 'r')
    valid_count = 0
    for line in f:
        space_split = line.split(" ")
        min_max = space_split[0].split("-")
        ind1 = int(min_max[0]) - 1
        ind2 = int(min_max[1]) - 1
        let = space_split[1].split(":")[0]
        if (space_split[2][ind1] == let and space_split[2][ind2] != let) or (space_split[2][ind1] != let and space_split[2][ind2] == let):
            valid_count+=1
    print("valid count: ", valid_count)

def traverse(x_run, y_run, mapp):
    current_x = 0
    tree_count = 0
    tree = "#"
    for current_y in range(0, len(mapp), y_run):
        # literally just walk 3,1 and if there is a tree increment the count
        if mapp[current_y][current_x] == tree:
            tree_count+=1
        current_x = (current_x+x_run) % len(mapp[0]) # loop back to traverse full dataset.

    print("tree count ", tree_count)
    return tree_count

def advent_day3_part1(x_run, y_run):
    tree = "#"
    f =open("treeslopes.txt","r")
    mapp=[]
    for fl in f:
        mapp.append(list(fl)[:-1]) # Cut the last character because that is the new line symbol. 
    print("map", len(mapp), len(mapp[0]))
    print(mapp[0])
    traverse(3,1,mapp)

def advent_day3_part2():
    f =open("treeslopes.txt","r")
    mapp=[]
    for fl in f:
        mapp.append(list(fl)[:-1]) # Cut the last character because that is the new line symbol. 

    count1 = traverse(1,1,mapp)
    count2 = traverse(3,1,mapp)
    count3 = traverse(5,1,mapp)
    count4 = traverse(7,1,mapp)
    count5 = traverse(1,2,mapp)
    multiplied_count = int(count1*count2*count3*count4*count5)
    print("multiplied tree count ", multiplied_count)

def check_valid(passport):
    # do check on collected set
    valid_passport = True
    for v in passport.values():
        if not v:
            valid_passport = False
            break

    return valid_passport

def advent_day4_part1():
    f=open("passports.txt","r")
    valid_count = 0
    passport = {"byr": False,"iyr":False,"eyr":False,"hgt":False,"hcl":False,"pid":False,"ecl":False} # cid is optional, not included.
    for line in f:
        if line.strip() == "":
            if check_valid(passport):
                valid_count += 1

            # reset dictionary
            for k in passport:
                passport[k] = False
            continue

        # passport line
        keyvalpair=line.split(" ")
        for kv in keyvalpair:
            k = kv.split(":")[0]
            if k in passport:
                passport[k] = True

    # Check the last one.
    if check_valid(passport):
        valid_count += 1

    print("valid passports: ", valid_count)

def hcl_check(v):
    if len(v) != 7:
        return False
    if v[0] != "#":
        return False
    valid = {"0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"}
    for i in range(1,6):
        if v[i] not in valid:
            return False
    return True

def hgt_check(v):
    chars = list(v)
    height = ""
    measurement = ""
    for c in chars:
        try:
            int(c)
            height += c
        except ValueError:
            measurement+=c
    if measurement == "cm":
        if int(height) >= 150 and int(height) <= 193:
            return True
    if measurement == "in":
        if int(height) >= 59 and int(height) <= 76:
            return True
    return False

def advent_day4_part2():
    f=open("passports.txt","r")
    valid_count = 0
    ecl_set = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    passport = {"byr": False,"iyr":False,"eyr":False,"hgt":False,"hcl":False,"pid":False,"ecl":False} # cid is optional, not included.
    for line in f:
        if line.strip() == "":
            if check_valid(passport):
                valid_count += 1

            # reset dictionary
            for k in passport:
                passport[k] = False
            continue

        # passport line
        keyvalpair=line.split(" ")
        # print(keyvalpair)
        for kv in keyvalpair:
            kvsplit = kv.split(":")
            k = kvsplit[0]
            v = kvsplit[1].strip()
            # print("key", k,"value ", v)
            if k not in passport:
                continue
            if k == "byr":
                if len(v) == 4 and int(v) >= 1920 and int(v) <= 2002:
                    passport[k] = True
                else:
                    print("invalid byr ", v)
            if k == "iyr":
                if len(v) == 4 and int(v) >= 2010 and int(v) <= 2020:
                    passport[k] = True
                else:
                    print("invalid iyr ", v)
            if k == "eyr":
                if len(v) == 4 and int(v) >= 2020 and int(v) <= 2030:
                    passport[k] = True
                else:
                    print("invalid eyr ", v)
            if k == "pid":
                if len(v) == 9:
                    passport[k] = True
                else:
                    print("invalid pid ", v, len(v))
            if k == "ecl":
                if v in ecl_set:
                    passport[k] = True
                else:
                    print("invalid ecl ", v)
            if k == "hcl":
                if hcl_check(v):
                    passport[k] = True
                else:
                    print("invalid hcl ", v)
            if k == "hgt":
                if hgt_check(v):
                    passport[k] = True
                else:
                    print("invalid hgt ", v)
    # Check the last one.
    if check_valid(passport):
        valid_count += 1
        
    print("valid passports: ", valid_count)

def find_spot(seat_range_inc, low_half_letter, upp_half_letter, seq):
    seat_range=seat_range_inc
    for letter in seq[:-1]:
        half_seat_range = (seat_range[1] - seat_range[0]) / 2.0
        if letter == low_half_letter:
            seat_range = [seat_range[0], seat_range[0] + math.floor(half_seat_range)]
        elif letter == upp_half_letter:
            seat_range = [seat_range[0] + math.ceil(half_seat_range), seat_range[1]]
    if seq[-1] == low_half_letter:
        return seat_range[0]
    else:
        return seat_range[1]

def seat_id(row, col):
    return row * 8 + col

def advent_day5_part1():
    seats = open("seats.txt","r")
    max_id = -1
    rows = [0,127]
    cols=[0,7]
    for seat in seats:
        r =find_spot(rows, "F","B", seat[:7])
        c=find_spot(cols, "L", "R", seat[7:])
        idd = seat_id(r,c)
        max_id = max(max_id, idd)
    print("max seat id ", max_id)

def advent_day5_part2():
    seats = open("seats.txt","r")
    rows = [0,127]
    cols=[0,7]
    ids = []
    for seat in seats:
        r=find_spot(rows, "F","B", seat[:7])
        c=find_spot(cols, "L", "R", seat[7:])
        idd = seat_id(r,c)
        ids.append(idd)

    ids = sorted(ids)
    for i in range(len(ids)-1):
        c_id = ids[i]
        above = ids[i+1]
        if c_id == above - 2:
            # Gap of 1, therefore the missing seat is here.
            print("Seat id: ", c_id + 1)
            return c_id+1

def advent_day6_part1():
    f = open("groups.txt", "r")
    yes_count = 0
    current_yeses = set()
    for line in f:
        s_line = line.strip()
        if s_line == "":
            yes_count += len(current_yeses)
            
            # reset set
            current_yeses = set()
            continue

        for let in s_line:
            current_yeses.add(let)
    yes_count += len(current_yeses)
    print("Yes count: ", yes_count)

def advent_day6_part2():
    f = open("groups.txt", "r")
    yes_count = 0
    group_size = 0
    current_yeses = dict()
    for line in f:
        s_line = line.strip()
        if s_line == "":
            for let in current_yeses:
                if current_yeses[let] == group_size:
                    yes_count += 1
            
            # reset set
            current_yeses = dict()
            group_size = 0
            continue

        group_size += 1
        for let in s_line:
            if let in current_yeses:
                current_yeses[let] += 1
            else:
                current_yeses[let] = 1

    for let in current_yeses:
        if current_yeses[let] == group_size:
            yes_count += 1
    print("Yes count: ", yes_count)

def advent_day7_part1():
    f=open("bagrules.txt","r")
    bag_layer_one = {}
    for line in f:
        line = line.strip()
        sline = line.split(" ")
        main_bag = sline[0]+sline[1]
        container=""
        for x in range(4, len(sline)):
            container+= sline[x]
            container+= " "
        if "no other bags" in container:
            bag_layer_one[main_bag] = []
            continue

        scontainer = container.split(",")
        bag_contains_list = []
        for sc in scontainer:
            split_sc = sc.split(" ")
            if split_sc[0] == "":
                # This accounts for the space leading the lines after commans.
                del split_sc[0]
            count = int(split_sc[0])
            bagtype = split_sc[1]+split_sc[2]
            bag_contains_list.append(bagtype)#(bagtype, count))
        bag_layer_one[main_bag] = bag_contains_list

    # Find all the bags that contain gold directly
    starter = "shinygold"
    bag_count = 0 
    next_desired = [starter]
    seen = set()
    while len(next_desired) > 0:
        desired = next_desired.pop()
        seen.add(desired)
        for bag in bag_layer_one:
            # print("bag ", bag," contains ", bag_layer_one[bag])
            if desired in bag_layer_one[bag]:
                # contains the desired bag, which contains the gold.
                if bag not in seen:
                    bag_count += 1
                    next_desired.append(bag)
    print("Bag Count ", bag_count)

def this_bag_contains(desired, bag_layer_one):
    if bag_layer_one[desired] == []:
        # Return Now with no bags left!
        return 0
    else:
        # Get bag count.
        res = 0
        for b in bag_layer_one[desired]:
            res += b[1] # add just the bags contained within desired
             # Add each contained bags contents, multiplied by the number of times that contained 
             # bag appears.
            res += b[1] * this_bag_contains(b[0], bag_layer_one)
        return res

def advent_day7_part2():
    f=open("bagrules.txt","r")
    bag_layer_one = {}
    for line in f:
        line = line.strip()
        sline = line.split(" ")
        main_bag = sline[0]+sline[1]
        container=""
        for x in range(4, len(sline)):
            container+= sline[x]
            container+= " "

        if "no other bags" in container:
            bag_layer_one[main_bag] = []
            continue
            
        scontainer = container.split(",")
        bag_contains_list = []
        for sc in scontainer:
            split_sc = sc.split(" ")
            if split_sc[0] == "":
                # This accounts for the space leading the lines after commans.
                del split_sc[0]
            count = int(split_sc[0])
            bagtype = split_sc[1]+split_sc[2]
            bag_contains_list.append((bagtype, count))
        bag_layer_one[main_bag] = bag_contains_list

    # Find all the bags that contain gold directly
    starter = ("shinygold", 0)
    bag_count = this_bag_contains("shinygold", bag_layer_one)
    print("Bag count ", bag_count)


advent_day7_part2()