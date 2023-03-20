trgt_hgt = float(input("target height above sea lvl in ft: ")) # target height in feet for precision
release_hgt = float(input("release height in ft: ")) # release height in feet for precision
ords = {"mk82", "snake", "hydra"}
while True:
    ord_type = input("ordanance type (mk82, snake, hydra): ")
    if ord_type not in ords:
        print ("Invalid ordanance type, try again.")
    else:
        break

release_ang = int(input("Release angle in degrees: "))



if ord_type == "mk82":
    print("mk82 type")
elif ord_type == "snake":
    print("snake type")
else:
    print("hydra type")