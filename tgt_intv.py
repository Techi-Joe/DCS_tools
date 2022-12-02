tgt_len = 1500
#int(input("what is the target length (ft)? "))
ord = 3
#int(input("how much ordinance are you carrying? "))
hspd = 500 # horizontal speed in ft/s
intvs = [0.06, 0.1, 0.14]
comp_intvs = []

# note: for now all in ft

tru_intv = tgt_len/hspd/ord

for intv in intvs:
    comp_intvs.append(tru_intv-intv)
print(comp_intvs)
print(tru_intv)

# TODO: find loweset comp_intvs
