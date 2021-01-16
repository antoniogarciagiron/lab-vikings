from vikingsClasses import War
from vikingsClasses import Viking
from vikingsClasses import Saxon
from vikingsClasses import Soldier

import random

names_list=['Olaf', 'Vicky', 'Ragnar', 'Harald', 'Sigurd']
vikingraid=War()
print('Viking forces (S, H): ')
for n in names_list:
    vikingraid.addViking(Viking(n, random.randint(1,10), random.randint(1,10)))
    print(vikingraid.vikingArmy[-1].name, vikingraid.vikingArmy[-1].health, vikingraid.vikingArmy[-1].strength)
saxon_army_size=int(input('How many saxons are defending the castle? '))
print('Saxon forces (S, H): ')
for i in range(saxon_army_size):
    vikingraid.addSaxon(Saxon(random.randint(1,5), random.randint(1,5)))
    print(f"Saxon{i+1} ", vikingraid.saxonArmy[-1].health, vikingraid.saxonArmy[-1].strength)

print("-"*60)
print("A castle in the coast of Essex, during a cold winter night...")
print(vikingraid.vikingArmy[0].battleCry())
fight=True
print("-"*60)
turn=1
while fight:
    print(f"Turn {turn}")
    turn+=1
    if (len(vikingraid.vikingArmy) != 0) and (len(vikingraid.saxonArmy) != 0):
        print(vikingraid.vikingAttack())
    if (len(vikingraid.vikingArmy) != 0) and (len(vikingraid.saxonArmy) != 0):
        print(vikingraid.saxonAttack())
    print(vikingraid.showStatus())
    if (len(vikingraid.saxonArmy) == 0) or (len(vikingraid.vikingArmy) == 0):
        fight=False
    print("-"*60)
    