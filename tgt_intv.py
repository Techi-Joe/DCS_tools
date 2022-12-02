tgt_len = float(input("what is the target length (ft)? ")) / 6076.118 # convert to nm
ord = int(input("how much ordinance are you carrying? "))
hspd = (float(input("what is your speed (knots)? ")) /60) /60
intvs = [0.06, 0.1, 0.14]
comp_intvs = {}

tru_intv = tgt_len/hspd/ord

# create a dictionary of all the values and compare them
# dissallow numbers that comapre negatively
# check if anything is put in dict at all

flag = False
for intv in intvs:
    if (tru_intv-intv >= 0):
        comp_intvs[tru_intv-intv] = intv
        flag = True
if not flag:
    comp_intvs = {0.00: min(intvs)}
        
print("\nperfect drop interval: " + str(tru_intv))
print("best possible drop interval: " + str(comp_intvs[min(comp_intvs)]))
if (comp_intvs[min(comp_intvs)] > tru_intv):
    print("*note: not all ordinance can be used in one run-in")