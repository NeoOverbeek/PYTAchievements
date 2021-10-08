import random
import time

power_list = ['Teleportation','Psychic Abilities','Superspeed','Superstrength','Flight','Superintelligence']

Name = "Neo Overbeek"

Age = random.randint(16,34)
Jumpforce = random.randint(0,20)
Power = random.choice(power_list)
Power2 = random.randint(1,3)
Speed = random.randint(50,150)
Strenght = random.randint(50,150)
Intelligence = random.randint(50,150)
CookingLevel = random.randint(1,5)
Charisma = random.randint(1,10)

while True:
    if Power == "Superspeed":
        Speed = 500
    elif Power == "Superstrength":
        Strenght = 500
    elif Power == "Superintelligence":
        Intelligence = 500
    if Power2 == 2:
        print("Wow! You're extremely lucky! You have been born with an additional power!")
        Power2 = random.choice(power_list)
    time.sleep(2)
    print("If you want to know more about yourself type stats.")
    if input() == "stats":
        print("Name: " + Name)
        print("Age: " + str(Age))
        print("Power: " + Power)
        for x in power_list:
            if x == Power2:
                print("Second power: " + Power2)
        print("Speed: " + str(Speed))
        print("Strength: " + str(Strenght))
        print("Intelligence: " + str(Intelligence))
        print("Jumpforce: " + str(Jumpforce))
        print("Cooking: " + str(CookingLevel) + " Stars")
        print("Charisma: " + str(Charisma))
