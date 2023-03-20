import heapq

#define functions

# This function takes an input and compares it against the
# comparison data to find the closest match
def find_nearest_num(input, comparison_data):
    return heapq.nsmallest(1, comparison_data, key=lambda x: abs(x-input))[0]

# this function compares two numbers
# and returns the deviation between them as a float
def deviation(input, original_num):
    return (original_num-input)/(original_num)

#----------------------------------------------------------------

# database of mils

#   ang:{alt:{kias:{mils}}
mk82_mils = {
    10:{700:{520:{45}}},
    15:{{1000:{{400:{87}},{450:{57}},{475:{52}},{500:{42}},{550:{32}}}},{1500:{{400:{113}},{450:{92}},{475:{77}},{500:{65}},{550:{51}}}},{2000},{3000}},
    20:{},
    25:{},
    30:{},
    35:{},
    40:{},
    45:{},
    50:{},
    60:{}
             }

snake_mils = {}

hydra_mils = {}


#----------------------------------------------------------------


# ask user for target/release values
release_kias = int(input("Release kias: ")) # knots at time of release
trgt_hgt = float(input("target height above sea lvl in ft: ")) # target height in feet for precision
release_hgt = float(input("release height in ft: ")) # release height in feet for precision
ords = {"mk82", "snake", "hydra"}
while True:
    ord_type = input("ordanance type (mk82, snake, hydra): ")
    if ord_type not in ords:
        print ("Invalid ordanance type, try again.")
    else:
        break

while True:
    release_ang = int(input("Release angle in degrees: "))
    if 0 <= release_ang <= 90:
        break
    else:
        print("Invalid release angle, try again.")

#----------------------------------------------------------------

if ord_type == "mk82":
    print(ord_type)
elif ord_type == "snake":
    print(ord_type)
else:
    print(ord_type)