

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

def advent_day8_part1():
    f = open("instructions.txt", "r")
    inst = []
    for line in f:
        sline = line.split(" ")
        inst.append([sline[0], int(sline[1]), None])

    accumulator = 0
    should_continue = True
    current_index = 0
    while should_continue:
        instruction = inst[current_index]
        if instruction[2] == None:
            inst[current_index][2] = current_index
        else:
            #Visited this instruction before
            should_continue = False
            break

        if instruction[0] == "nop":
            current_index+=1
        elif instruction[0] == "acc":
            accumulator += instruction[1]
            current_index+=1
        elif instruction[0] == "jmp":
            current_index += instruction[1]
        else:
            print("shouldn't hit here.")

    print("accumulator value ", accumulator)


def attempt_solve(inst, solve_try_index):
    accumulator = 0
    correct_finish = False
    should_continue = True
    current_index = 0
    while should_continue:
        if current_index >= len(inst):
            # Desired end behavior for the problem is found!
            correct_finish = True
            break

        instruction = inst[current_index]
        if instruction[2] == solve_try_index:
            # Only exit when it is an instruction we have visited during this
            # round of attempting to solve the puzzle. Exit instead of looping
            # forever.
            should_continue = False
            break
        else:
            inst[current_index][2] = solve_try_index

        if instruction[0] == "nop":
            current_index+=1
        elif instruction[0] == "acc":
            accumulator += instruction[1]
            current_index+=1
        elif instruction[0] == "jmp":
            current_index += instruction[1]
        else:
            print("shouldn't hit here.")
    return accumulator, correct_finish

def advent_day8_part2():
    f = open("instructions.txt", "r")
    inst = []
    for line in f:
        sline = line.split(" ")
        inst.append([sline[0], int(sline[1]), None])

    for i in range(len(inst)):
        orig_instruction = inst[i][0]
        if inst[i][0] == "nop":
            inst[i][0] = "jmp"
        elif inst[i][0] == "jmp":
            inst[i][0] = "nop"
        acc, correct = attempt_solve(inst, i)
        if correct:
            print("accumulator value ", acc)
            break
        inst[i][0] = orig_instruction

def mins_and_maxes(subdata):
    lowest = float("inf")
    lower = float("inf")
    highest = float("-inf")
    higher = float("-inf")
    for dat in subdata:
        if dat < lowest:
            lower = lowest
            lowest = dat
        elif dat <= lower:
            lower = dat

        if dat > highest:
            higher = highest
            highest = dat
        elif dat >= higher:
            higher = dat
    return lowest, lower, higher, highest

def advent_day9_part1():
    f = open("xmasdata.txt", "r")
    current_inds = [0, 25] # first 25 items
    data = []
    for line in f:
        data.append(int(line.strip()))

    for i in range(25, len(data)):
        min1, min2, max2, max1 = mins_and_maxes(data[current_inds[0]:current_inds[1]])
        current_val = data[i]
        smallest = min1+min2
        largest = max2+max1
        # print("small ", smallest, " large ", largest, " current ", current_val)
        if current_val < smallest or current_val > largest:
            print("Value failed: ", current_val)
            break

        current_inds[0]+=1
        current_inds[1]+=1

def find_contiguous_range(data, invalid_num):
    current_index = 0
    curr_sum = 0
    for i in range(current_index, len(data)):
        curr_sum += data[i]
        if curr_sum == invalid_num:
            print("found it!")
            return [current_index, i]
        if curr_sum > invalid_num:
            # could be more smart and take the partial sums and subtract the 
            # removed number, add the new ones.
            while curr_sum > invalid_num:
                curr_sum -= data[current_index]
                current_index+=1
                if curr_sum == invalid_num:
                    print("found it now!")
                    return [current_index, i]
            continue


def advent_day9_part2():
    invalid_num = 2089807806
    f = open("xmasdata.txt", "r")
    data = []
    for line in f:
        data.append(int(line.strip()))

    ranges = find_contiguous_range(data, invalid_num)
    subdata = data[ranges[0]:ranges[1]]
    print("encryption weakness ", min(subdata)+max(subdata))

def advent_day10_part1():
    f = open("jolts.txt","r")
    jolts = [int(line.strip()) for line in f]
    jolts.append(0) # this is the charging port the adapters go in.
    jolts = sorted(jolts)
    one_jolt_count = 0
    three_jolt_count = 1 # My final adapter is 3 jolts higher, so start this at 1 to account for it.
    for i in range(0, len(jolts)-1):
        diff=jolts[i+1] - jolts[i]
        if diff == 1:
            one_jolt_count +=1
        elif diff == 3:
            three_jolt_count +=1
    print("difference of one: ", one_jolt_count)
    print("difference of three: ", three_jolt_count)
    print("Found: ", one_jolt_count * three_jolt_count)


def advent_day10_part2():
    f = open("jolts.txt","r")
    jolts = [int(line.strip()) for line in f]
    jolts.append(0) # this is the charging port the adapters go in.
    jolts = sorted(jolts)
    final = jolts[-1]
    ways_to_reach_i = [1] + [0] * (len(jolts)-1)
    print(len(ways_to_reach_i))
    for i in range(0, len(jolts)-1):
        j = i+1
        while j < len(jolts) and jolts[j]-jolts[i] <= 3:
            # Able to go from index i --> index j using 0,1,2,3 jolts
            # Therefore all the ways to reach i are also ways to reach j
            ways_to_reach_i[j] += ways_to_reach_i[i]
            j += 1

    print("Found: ", ways_to_reach_i[-1])

def empty(i, j, seats):
    return seats[i][j] =="L" or seats[i][j] == "."

def check_seats(i, j, rows, cols, seats):
    seat_count = 0
    possible_seats = 0
    if i-1 >=0:
        possible_seats += 1
        if empty(i-1, j, seats):
            seat_count+=1
        if j-1 >=0:
            possible_seats += 1
            if empty(i-1, j-1, seats):
                seat_count+=1
        if j+1 < cols:
            possible_seats += 1
            if empty(i-1, j+1, seats):
                seat_count+=1
    if i+1 <rows:
        possible_seats += 1
        if empty(i+1, j, seats):
            seat_count+=1
        if j-1 >=0:
            possible_seats += 1
            if empty(i+1, j-1, seats):
                seat_count+=1
        if j+1 < cols:
            possible_seats += 1
            if empty(i+1, j+1, seats):
                seat_count+=1
    if j-1 >=0:
        possible_seats += 1
        if empty(i, j-1, seats):
            seat_count+=1
    if j+1 < cols:
        possible_seats += 1
        if empty(i, j+1, seats):
            seat_count+=1
    return seat_count, possible_seats

def advent_day11_part1():
    f=open("seatchart.txt", "r")
    seats=[]
    for line in f:
        line = line.strip()
        row = []
        for char in line:
            row.append(char)
        seats.append(row)

    rows = len(seats)
    cols = len(seats[0])
    while True:
        updated_seats = [[0 for i in range(cols)] for i in range(rows)]
        print(len(updated_seats), len(seats), len(updated_seats[0]), len(seats[0]))
        seat_changed = False
        occ_count = 0
        for i in range(0, rows):
            for j in range(0, cols):
                updated_seats[i][j] = seats[i][j]
                if seats[i][j] == ".":
                    continue
                empty_count, possible_seats = check_seats(i,j, rows, cols, seats)
                occupied_count = possible_seats - empty_count
                if seats[i][j] == "L" and empty_count == possible_seats:
                    updated_seats[i][j] = "#"
                    seat_changed = True
                elif seats[i][j] == "#" and occupied_count >= 4:
                    updated_seats[i][j] = "L"
                    seat_changed = True
                if updated_seats[i][j] == "#":
                    occ_count+=1
        seats = updated_seats
        if not seat_changed:
            print("occupied: ", occ_count)
            break

def check_direction(start_i, start_j, inc_i, inc_j, rows, cols, seats):
    should_continue = True
    while should_continue:
        new_i= start_i + inc_i 
        new_j = start_j + inc_j
        if new_i >= 0 and new_i < rows and new_j >= 0 and new_j < cols:
            if seats[new_i][new_j] == ".":
                start_i = new_i
                start_j = new_j
                continue
            elif seats[new_i][new_j] == "#":
                return False
            else:
                return True
        else:
            return None

def check_all_directions(i, j, rows, cols, seats):
    empty_count = 0
    possible_seats = 0
    up = check_direction(i,j,+1, 0, rows, cols, seats)
    if up is not None:
        possible_seats += 1
    if up:
        empty_count += 1
    down = check_direction(i,j,-1, 0, rows, cols, seats)
    if down is not None:
        possible_seats += 1
    if down:
        empty_count += 1
    left = check_direction(i,j,0,-1, rows, cols, seats)
    if left is not None:
        possible_seats += 1
    if left:
        empty_count += 1
    right = check_direction(i,j,0,+1, rows, cols, seats)
    if right is not None:
        possible_seats += 1
    if right:
        empty_count += 1
    d1 = check_direction(i,j,-1,+1, rows, cols, seats)
    if d1 is not None:
        possible_seats += 1
    if d1:
        empty_count += 1
    d2 = check_direction(i,j,+1,+1, rows, cols, seats)
    if d2 is not None:
        possible_seats += 1
    if d2:
        empty_count += 1
    d3 = check_direction(i,j,+1,-1, rows, cols, seats)
    if d3 is not None:
        possible_seats += 1
    if d3:
        empty_count += 1
    d4 = check_direction(i,j,-1,-1, rows, cols, seats)
    if d4 is not None:
        possible_seats += 1
    if d4:
        empty_count += 1
    return  empty_count, possible_seats

def advent_day11_part2():
    f=open("seatchart.txt", "r")
    seats=[]
    for line in f:
        line = line.strip()
        row = []
        for char in line:
            row.append(char)
        seats.append(row)

    rows = len(seats)
    cols = len(seats[0])
    while True:
        updated_seats = [[0 for i in range(cols)] for i in range(rows)]
        print(len(updated_seats), len(seats), len(updated_seats[0]), len(seats[0]))
        seat_changed = False
        occ_count = 0
        for i in range(0, rows):
            for j in range(0, cols):
                updated_seats[i][j] = seats[i][j]
                if seats[i][j] == ".":
                    continue
                empty_count, possible_seats = check_all_directions(i,j, rows, cols, seats)
                occupied_count = possible_seats - empty_count
                if seats[i][j] == "L" and empty_count == possible_seats:
                    updated_seats[i][j] = "#"
                    seat_changed = True
                elif seats[i][j] == "#" and occupied_count >= 5:
                    updated_seats[i][j] = "L"
                    seat_changed = True
                if updated_seats[i][j] == "#":
                    occ_count+=1
        seats = updated_seats
        if not seat_changed:
            print("occupied: ", occ_count)
            break

def move_in_dir(ang, xy, num):
    if ang == "east":
        xy[0] += num
    elif ang == "west":
        xy[0] -= num
    elif ang == "north":
        xy[1] += num
    else:
        xy[1] -= num
    return xy

def new_ang(ang, let, num):
    if let == "R":
        ang = (ang + num) % 360
    else:
        t = (ang - num)
        if  t < 0:
            ang = 360 + t
        else:
            ang = t
    return ang


# print(new_ang(270, "R", 180))
# print(new_ang(90, "R", 180))
# print(new_ang(90, "L", 90))

def advent_day12_part1():
    f = open("directions.txt", "r")
    xy = [0,0]
    ang = 90
    mapp = {90:"east", 180 : "south", 270:"west", 0: "north"}
    for line in f:
        line = line.strip()
        let = line[0]
        num = int(line[1:])

        if let == "F":
            #continue in current direction.
            xy = move_in_dir(mapp[ang], xy, num)
        elif let == "N":
            xy = move_in_dir("north", xy, num)
        elif let == "S":
            xy = move_in_dir("south",xy, num)
        elif let == "E":
            xy = move_in_dir("east", xy, num)
        elif let == "W":
            xy = move_in_dir("west", xy, num)
        else:
            # L/R directions.
            ang = new_ang(ang, let, num)
        print(xy)
    print("L1 ", abs(xy[0])+abs(xy[1]))

def rotate_ninety(x,y, wpx, wpy, is_left=False):
    # no need to translate the waypoint because it is specified relative to 
    # the ship. therefore, the ship is viewed as origin.
    # simply rotate around (0,0)
    if is_left: #left = (-y, x)
        rotate_wp_x = -wpy
        rotate_wp_y = wpx
    else: # right = (y, -x)
        rotate_wp_x = wpy
        rotate_wp_y = -wpx
    return [rotate_wp_x, rotate_wp_y]

def move_in_waypoint_dir(num, xy, wp):
    xy[0] += num*wp[0]
    xy[1] += num*wp[1]
    return xy

def rotate_waypoint(num, let, wp, xy):
    # 180 degress = (-x, -y) 
    # right 90 degrees = (y, -x)
    # left 90 degrees = (-y, x)
    print(let, num, wp)
    times_to_apply = int(abs(num/90))
    print(times_to_apply)
    for i in range(times_to_apply):
        # apply rotation in direction
        if let == "L":
            wp = rotate_ninety(xy[0], xy[1], wp[0], wp[1], is_left=True)
        else:
            wp = rotate_ninety(xy[0], xy[1], wp[0], wp[1], is_left=False)
        print("wp", wp)
    return wp

def advent_day12_part2():
    f = open("directions.txt", "r")
    xy = [0,0]
    wp = [10, 1]
    for line in f:
        line = line.strip()
        let = line[0]
        num = int(line[1:])

        if let == "F":
            # move in direction of way point the "num" times.
            xy = move_in_waypoint_dir(num, xy, wp)
        elif let == "N":
            wp = move_in_dir("north", wp, num)
        elif let == "S":
            wp = move_in_dir("south",wp, num)
        elif let == "E":
            wp = move_in_dir("east", wp, num)
        elif let == "W":
            wp = move_in_dir("west", wp, num)
        else:
            # L/R directions.
            wp = rotate_waypoint(num, let, wp, xy)
        print(xy, wp)
    print("L1 ", abs(xy[0])+abs(xy[1]))


def advent_day13_part1():
    file = open("buses.txt","r")
    f = []
    for line in file:
        f.append(line)
    depart_time = int(f[0])
    buses = (f[1].strip()).split(",")
    earliest_id = None
    smallest_wait = float("inf")
    for bus in buses:
        if bus == "x":
            continue
        minutes_after = depart_time % int(bus)
        minutes_to_wait = int(bus) - minutes_after
        if minutes_to_wait < smallest_wait:
            smallest_wait = minutes_to_wait
            earliest_id = int(bus)
    print(smallest_wait * earliest_id)

# Returns modulo inverse of a with 
# respect to m using extended 
# Euclid Algorithm. Refer below  
# post for details: 
# https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/ 
def inv(a, m) :       
    m0 = m 
    x0 = 0
    x1 = 1
  
    if (m == 1) : 
        return 0
  
    # Apply extended Euclid Algorithm 
    while (a > 1) : 
        # q is quotient 
        q = a // m 
        t = m 
  
        # m is remainder now, process  
        # same as euclid's algo 
        m = a % m 
        a = t 
  
        t = x0 
        x0 = x1 - q * x0 

        x1 = t 
      
    # Make x1 positive 
    if (x1 < 0) : 
        x1 = x1 + m0 
    return x1 

def advent_day13_part2():
    file = open("buses.txt","r")
    f = []
    for line in file:
        f.append(line)
    buses = (f[1].strip()).split(",")
    bus_nums = []
    bus_ids_product = 1
    for ind,bus in enumerate(buses):
        if bus == "x":
            continue
        bus_nums.append((int(bus), ind))
        bus_ids_product = bus_ids_product * int(bus)
    # first bus must be departing at 0, so can divide by each bus
    # BRUTE FORCE SOLUTION: (too slow)
    # i = 1
    # while True: 
    #     depart_time = bus_ids_product - i*bus_nums[0][0]
    #     # depart_time = i*bus_nums[0][0]
    #     failed = False
    #     for bus in bus_nums:
    #         minutes_after = (depart_time + bus[1]) % int(bus[0])
    #         if minutes_after != 0:
    #             failed = True
    #             break
    #     if not failed:
    #         print("Departs at ", depart_time)
    #         break
    #     i += 1

    # not brute force:
    # pre-req: all bus id pairs must have gcd = 1
    # Chinese remainder theorem solving: x(depature) = rem (bus index) % num (bus id)
    # Solving based on: https://www.youtube.com/watch?v=ru7mWZJlRQg
    # for each number, first get its placeholder which has everything else multiplied
    # then check the mod of that number, which should be mod of that number to equal the bus index.
    t = np.array([1 for i in range(len(bus_nums))], dtype='int64')
    for i, bus in enumerate(bus_nums):
        orig = t[i]
        t = bus[0] * t
        t[i] = orig
    for ind, (bus_id, bus_index) in enumerate(bus_nums):
        val = np.sum(t) % bus_id
        # we want val = np.sum(t) % bus_id --> val % bus_id where val == bus index.
        if val == bus_index:
            # then we're good! 
            continue
        else:
            # else: need to get the mod to match the bus_index
            # e.g. go from x = val % dep_time to n*x = bus_index % bus_id 
            # n = (bus_id % dep_time) / (val % dep_time)
            i = inv(val, bus_id)
            t[ind] = t[ind] * bus_index * i
            # checks that the multiplier actually did what we wanted:
            # both of these should return values == bus_index
            print(t[ind] % bus_id)
            print(np.sum(t) % bus_id)

    summed = np.sum(t)
    # Now get the smallest valid version of "x" by taking the mod of the product of all
    # the departure times==bus id.
    print("Depature time: ",bus_ids_product - summed % bus_ids_product)

def advent_day14_part1():
    f=open("masks.txt","r")
    mask = ""
    addresses = {}
    for line in f:
        line = line.strip()
        if "mask" in line:
            mask = list(line.split("mask = ")[-1])
        else:
            # mem address: get everything before "]", then cut out "mem["
            address = int(line.split("]")[0][4:])
            num = line.split(" ")[-1]
            num = bin(int(num))[2:] # remove "0b" added when converted to bytes
            num_list = list(num)
            for i in range(36-len(num_list)):
                num_list.insert(0, 0) # pad with zeros to make 36 bits
            #apply mask to bits
            for i, val in enumerate(mask):
                if val == "X":
                    continue
                num_list[i] = int(val)
            # convert back to base 10
            bin_num = "".join([str(n) for n in num_list])
            base_ten_num = int(bin_num, 2) # converts from base 2 to base 10
            print("address", address, " num ", base_ten_num)
            addresses[address]=base_ten_num
    summ = 0
    for a in addresses:
        summ += addresses[a]
    print("Sum: ", summ)

def advent_day14_part2():
    f=open("masks.txt","r")
    mask = ""
    addresses = {}
    for line in f:
        line = line.strip()
        if "mask" in line:
            mask = list(line.split("mask = ")[-1])
        else:
            # mem address: get everything before "]", then cut out "mem["
            address = int(line.split("]")[0][4:])
            val = line.split(" ")[-1]
            val_at_address = int(val)

            num = bin(int(address))[2:] # remove "0b" added when converted to bytes
            num_list = list(num)
            for i in range(36-len(num_list)):
                num_list.insert(0, 0) # pad with zeros to make 36 bits
            #apply mask to the memory address ("Memory address decoder")
            for i, val in enumerate(mask):
                if val == "0":
                    continue
                elif val == "1":
                    num_list[i] = 1
                elif val == "X":
                    # floating bit, so try both permutations of it.
                    num_list[i] = (0,1)

            current_endings = [""]
            for i in range(len(num_list)):
                consider_i = len(num_list) - i - 1
                n = num_list[consider_i]
                if type(n) == tuple:
                    # permutation, need to track both strings
                    new_endings = []
                    for ending in current_endings:
                        new_endings.append("0"+ending)
                        new_endings.append("1"+ending)
                    current_endings = new_endings
                else:
                    for i in range(len(current_endings)):
                        current_endings[i] = str(n)+current_endings[i]
            for num in current_endings:
                # convert back to base 10
                base_ten_num = int(num, 2) # converts from base 2 to base 10
                addresses[base_ten_num] = val_at_address
    summ = 0
    for a in addresses:
        summ += addresses[a]
    print("Sum: ", summ)

def spoken_word_game(end_number):
    base_nums = [0,3,1,6,7,5]
    tracking = {} # number to index last spoken at
    last_spoken_number = 0
    for i in range(1, end_number+2): # want the 2020th number
        if i - 1 < len(base_nums):
            tracking[base_nums[i-1]] = i
            last_spoken_number = base_nums[i-1]
        elif i == end_number+1:
            print("For ", end_number," spoke ", last_spoken_number)
        else:
            if last_spoken_number in tracking:
                # spoken at i-1 index.
                # new number = new_index - old_index
                new_num = i-1 - tracking[last_spoken_number]
                tracking[last_spoken_number] = i - 1
                last_spoken_number = new_num
            else:
                # a new number gets 0. put the new number in the dict.
                tracking[last_spoken_number] = i - 1
                last_spoken_number = 0

def advent_day15_part1():
    spoken_word_game(2020)

def advent_day15_part2():
    spoken_word_game(30000000)

def check_ticket(ticket, codes, summ):
    for t in ticket:
        valid_count = 0
        for k in codes:
            if ((t >= codes[k][0][0] and t <= codes[k][0][1]) or 
                (t >= codes[k][1][0] and t <= codes[k][1][1])):
                valid_count+=1
        if valid_count == 0:
            summ += t
    return summ

def advent_day16_part1():
    f=open("tickets.txt","r")
    codes = {}
    my_ticket = []
    other_tickets = []
    invalid_vals_count = 0
    ticket_local = 0
    for line in f:
        line = line.strip()
        if "your ticket" in line:
            ticket_local = 1
            continue
        elif "nearby ticket" in line:
            ticket_local = 2
            continue
        elif line == "":
            continue
        elif ticket_local == 0:
            #populating values+ranges.
            vals = line.split(": ")
            key = vals[0]
            range_strs = vals[1].split(" or ")
            ranges = []
            for r_str in range_strs:
                minmax = r_str.split("-")
                ranges.append((int(minmax[0]), int(minmax[1])))
            codes[key] = ranges
        elif ticket_local == 1:
            # my ticket
            vals = line.split(",")
            my_ticket = [int(v) for v in vals]
            invalid_vals_count = check_ticket(my_ticket, codes, invalid_vals_count)
        elif ticket_local == 2:
            vals = line.split(",")
            ticket = [int(v) for v in vals]
            invalid_vals_count = check_ticket(ticket, codes, invalid_vals_count)
    print("invalid count: ", invalid_vals_count)

def is_ticket_valid(ticket, codes):
    for t in ticket:
        valid_count = 0
        for k in codes:
            if ((t >= codes[k][0][0] and t <= codes[k][0][1]) or 
                (t >= codes[k][1][0] and t <= codes[k][1][1])):
                valid_count+=1
        if valid_count == 0:
            return False
    return True

def get_set_of_good_values(ticket_val, codes):
    good = set()
    for code in codes:
        ranger = codes[code]
        if ((ticket_val >= ranger[0][0] and ticket_val <= ranger[0][1]) or 
            (ticket_val >= ranger[1][0] and ticket_val <= ranger[1][1])):
            # valid for this index!
            good.add(code)
    return good

def get_smallest_set(legal_codes_per_index, used_indices):
    current_min = float("inf")
    current_ind = -1
    for i in legal_codes_per_index:
        if i in used_indices:
            continue
        if len(legal_codes_per_index[i]) < current_min and len(legal_codes_per_index[i]) != 0:
            current_min = len(legal_codes_per_index[i])
            current_ind = i
    return current_ind

def greedy_matching_algo(legal_codes_per_index):
    matches = {}
    # set current index as the one with least amount of codes
    current_ind = get_smallest_set(legal_codes_per_index, matches.keys())
    while len(matches) != len(legal_codes_per_index):
        if len(legal_codes_per_index[current_ind]) > 0:
            # remove this code everywhere else once setting it as the value
            code = legal_codes_per_index[current_ind].pop()
            matches[current_ind] = code
            for i in legal_codes_per_index:
                try:
                    legal_codes_per_index[i].remove(code)
                except Exception:
                    pass
            current_ind = get_smallest_set(legal_codes_per_index, matches.keys())
    print(matches)
    return matches

def advent_day16_part2():
    f=open("tickets.txt","r")
    codes = {}
    my_ticket = []
    other_tickets = []
    ticket_local = 0
    for line in f:
        line = line.strip()
        if "your ticket" in line:
            ticket_local = 1
            continue
        elif "nearby ticket" in line:
            ticket_local = 2
            continue
        elif line == "":
            continue
        elif ticket_local == 0:
            #populating values+ranges.
            vals = line.split(": ")
            key = vals[0]
            range_strs = vals[1].split(" or ")
            ranges = []
            for r_str in range_strs:
                minmax = r_str.split("-")
                ranges.append((int(minmax[0]), int(minmax[1])))
            codes[key] = ranges
        elif ticket_local == 1:
            # my ticket
            vals = line.split(",")
            my_ticket = [int(v) for v in vals]
        elif ticket_local == 2:
            vals = line.split(",")
            ticket = [int(v) for v in vals]
            valid = is_ticket_valid(ticket, codes)
            if valid:
                # valid ticket.
                other_tickets.append(ticket)

    # "failed code" means: for each index, the code failed for one or more ticket
    # values (my ticket and other tickets).

    # Determine determine codes that work for each index of MY ticket. Any other codes are 
    # irrelevant and will be removed from the main dictionary of codes.
    exile_codes = set()
    for code in codes:
        ranger = codes[code]
        failed = 0
        for ticket_val in my_ticket:
            if not ((ticket_val >= ranger[0][0] and ticket_val <= ranger[0][1]) or 
                (ticket_val >= ranger[1][0] and ticket_val <= ranger[1][1])):
                failed+=1
        if failed == len(my_ticket):
            exile_codes.add(code)
    for code in exile_codes:
        codes.remove(code)

    # Per index of my ticket, determine which codes work for that index specifically.
    # create sets of valid codes for each index.
    my_ticket_good_codes = []
    for ticket_val in my_ticket:
        good = get_set_of_good_values(ticket_val, codes)
        my_ticket_good_codes.append(good)

    # now for each set of good codes for an index, check every other ticket and slowly prune 
    # down that list of good codes. If a code fails for one ticket, it can no longer be considered
    # as a good code for that index.
    legal_codes_per_index = {}
    for ind, legal_codes in enumerate(my_ticket_good_codes):
        for ticket in other_tickets:
            ticket_val = ticket[ind]
            still_works = set()
            for code in legal_codes:
                ranger = codes[code]
                if ((ticket_val >= ranger[0][0] and ticket_val <= ranger[0][1]) or 
                    (ticket_val >= ranger[1][0] and ticket_val <= ranger[1][1])):
                    # valid for this index!
                    still_works.add(code)
            legal_codes = still_works.intersection(legal_codes)
            if len(legal_codes) == 0:
                # this should never happen unless an invalid ticket is included in the mix.
                print("AHHHHHHHHHHHHH")
                print("Tickt: ", ticket)
                print("Index: ", ind)
                print("Still works ", len(still_works), " and ", len(legal_codes))
                print("after intersection", len(temp))
        legal_codes_per_index[ind] = legal_codes

    # Determine which code matches which index using a greedy algorithm that 
    # tries to set codes with indices when there are no other or very few choices.
    matches = greedy_matching_algo(legal_codes_per_index)

    # get the product of all of my ticket's values where the index has a code with the word
    # departure in it.
    pdt = 1
    for ind in matches:
        code = matches[ind]
        if "departure" in code:
            pdt = pdt * my_ticket[ind]
    print("Final product: ", pdt)

advent_day16_part2()