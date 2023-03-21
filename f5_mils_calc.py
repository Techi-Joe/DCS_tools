import heapq
import matplotlib.pyplot as plt
import os

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

#   ang:[{alt:[{kias:mils}]}]
mk82_mils = {
    10:[{700:[{520:45}]}],

    15:[{1000:[{400:87},{450:57},{475:52},{500:42},{550:32}]},
        {1500:[{400:113},{450:92},{475:77},{500:65},{550:51}]},
        {2000:[{400:140},{450:107},{475:98},{500:83},{550:69}]},
        {3000:[{400:200},{450:146},{475:134},{500:122},{550:101}]}],

    20:[{1000:[{400:62},{450:44},{475:32},{500:30},{550:24}]},
        {1500:[{400:85},{450:61},{475:52},{500:48},{550:38}]},
        {2000:[{400:112},{450:87},{475:75},{500:68},{550:54}]},
        {3000:[{400:154},{450:118},{475:105},{500:92},{550:82}]},
        {4000:[{400:185},{450:145},{475:133},{}]}],

    30:[],
    
    40:[],
    
    45:[],
    
    50:[],
    
    60:[]
             }

snake_mils = {}

hydra_mils = {}

#----------------------------------------------------------------
# user inputs

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
    release_ang = int(input("Release angle in degrees (multiples of 5): "))
    if 0 <= release_ang <= 90 and release_ang%5 == 0:
        break
    else:
        print("Invalid release angle, try again.")

#----------------------------------------------------------------
# math

#----------------------------------------------------------------
# output

os.system('cls')
print("ordanance : " + str(ord_type) + " | " + "")