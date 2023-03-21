import heapq
import matplotlib.pyplot as plt
import os
from tqdm import tqdm

# define functions

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

# a "-1" denotes a condition 
# that is not maintainable

# format - angle:[{altitude:[{kias:mils}]}]

mk82_mils = {
    10:[{700:[{520:45}]}],

    15:[{1000:[{400:87},{450:57},{475:52},{500:42},{550:32}]},
        {1500:[{400:113},{450:92},{475:77},{500:65},{550:51}]},
        {2000:[{400:140},{450:107},{475:98},{500:83},{550:69}]},
        {3000:[{400:200},{450:146},{475:134},{500:122},{550:101}]}],

    20:[{1000:[{400:62},{450:44},{475:32},{500:30},{550:24}]},
        {1500:[{400:85},{450:61},{475:52},{500:48},{530:45},{550:38}]},
        {2000:[{400:112},{450:87},{475:75},{500:68},{550:54}]},
        {2500:[{530:68}]},
        {3000:[{400:154},{450:118},{475:105},{500:92},{550:82}]},
        {3500:[{555:92}]},
        {4000:[{400:185},{450:145},{475:133},{500:121},{550:102}]}],
    
    25:[{3000:[{560:60},{590:55}]}],

    30:[{1500:[{400:-1},{450:38},{475:30},{500:25},{550:18}]},
        {2000:[{400:-1},{450:54},{460:45},{475:43},{500:36},{550:30}]},
        {2500:[{575:35}]},
        {3000:[{400:-1},{450:78},{475:65},{500:62},{520:60},{550:51},{570:45}]},
        {4000:[{400:-1},{450:100},{475:87},{500:79},{550:65}]},
        {5000:[{400:-1},{450:118},{475:108},{500:97},{550:78}]}],

    35:[{3000:[{560:40}]},
        {3200:[{580:40}]}],
    
    40:[{3000:[{470:70}]},
        {3500:[{500:50}]},
        {4000:[{540:45}]},
        {6000:[{525:70}]}],
    
    45:[{3000:[{400:-1},{450:-1},{475:-1},{500:23},{550:19}]},
        {4000:[{400:-1},{450:-1},{475:-1},{500:35},{550:28}]},
        {5000:[{400:-1},{450:-1},{475:-1},{500:49},{550:38}]},
        {9000:[{520:90}]}],
    
    50:[{5000:[{500:45}]}],
    
    60:[{4000:[{400:-1},{450:-1},{475:-1},{500:5},{550:2}]},
        {5000:[{400:-1},{450:-1},{475:-1},{500:10},{550:7}]},
        {6000:[{400:-1},{450:-1},{475:-1},{500:18},{550:14}]},
        {7000:[{540:25}]},
        {10000:[{500:50}]}]
}

snake_mils = {
    0:[{100:[{530:40}]},
       {200:[{515:60},{570:55},{600:55},{520:65}]},
       {300:[{610:80}]},
       {350:[{540:105}]}],

    5:[{300:[{555:50},{450:80},{545:45}]},
       {350:[{560:45}]},
       {500:[{560:85},{540:95}]},
       {700:[{530:155}]}],

    10:[{500:[{560:50}]},
        {800:[{610:90}]},
        {900:[{560:125}]}],

    15:[{1000:[{550:124}]},
        {1200:[{570:120}]}],

    20:[{1000:[{600:60}]}]
}

#----------------------------------------------------------------
# user inputs

flag = False
# ask user for target/release values
release_kias = int(input("Release kias: ")) # knots at time of release

if release_kias == -1: # use -1 as test value
    flag = True

if not flag:
    trgt_hgt = float(input("target height above sea level in ft: ")) # target height in feet for precision
    release_hgt = float(input("release height in ft: ")) # release height in feet for precision
    ords = {"mk82", "snake"}
    while True:
        ord_type = input("ordanance type (mk82 or snake): ")
        if ord_type not in ords:
            print ("Invalid ordanance type, try again.")
        else:
            break

    while True:
        release_ang = int(input("Release angle in degrees (divisable by 5): "))
        if 0 <= release_ang <= 90 and release_ang%5 == 0:
            break
        else:
            print("Invalid release angle, try again.")
    
    hgt_abv_trgt = release_hgt-trgt_hgt # height above target
else:
    print("entering test values!")
    hgt_abv_trgt = 3833
    ord_type = "mk82"
    release_kias = 510
    release_ang = 13


os.system('cls')
print("ordanance : " + str(ord_type) + " | " + "speed : " + str(release_kias) + " kias" + " | " + "height above target : " + str(hgt_abv_trgt) + " | " + "angle : " + str(release_ang) + "°")

#----------------------------------------------------------------
# computation of mils

modifier = 0.00 # variation in nums to apply to mils

if ord_type == "mk82":
    angle = mk82_mils[find_nearest_num(release_ang, mk82_mils.keys())]
    alt = find_nearest_num(hgt_abv_trgt, angle)
else:
    print("snake")


#----------------------------------------------------------------
# output

