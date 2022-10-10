#Initial Values
pers_name = input("Set the name ")
pers_hp = 100
max_pers_hp = 100
armor = 50
nr_hits = 1


def speciall(pers_hp, dmg0 = 10):
    global armor,  nr_hits

    if nr_hits == 10:
        armor = armor - dmg0
    else:
        pers_hp = pers_hp - dmg0
    return pers_hp





#Fucntion declaration
def attack(pers_hp, dmg = 5):
#calling a global variables
    global armor, nr_hits

#if we have armor
    if armor - dmg > 0:
# decrease armor level
        armor = armor - dmg
    else:
# decrease hp level
        pers_hp = pers_hp-dmg
    return pers_hp # return the value

def heal(pers_hp,live):
# calling a global variable
    global max_pers_hp

# condition to not add more hp then max
    if pers_hp + live > max_pers_hp:
        pers_hp = max_pers_hp
    else:
        pers_hp = pers_hp + live

    return pers_hp # return the value

#Call Functions
pers_hp = attack(pers_hp, 40)
print(pers_hp)

pers_hp = heal(pers_hp, 20)
print(pers_hp)

# Make a battle
for i in range(1,100):
#stop cycle if hp drop below 0
    if pers_hp > 0:
        pers_hp = attack(pers_hp)
    else:
        break

print("Live ", pers_hp)
print("Armor", armor)
print("Hit nr ", i)

print("You are dead")