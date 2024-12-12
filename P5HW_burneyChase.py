# Chase Burney
# 11 - 19 - 24
# P5HW
# Creating a text based game using functions.
import random
import time

# Character/Enemy Creation:

def create_character():
    char = {
            "name": input("Enter your character's name: "),
            "health": 0,
            "mana": 0,
            "defense": 0,
            "dodge": 0,
            "damage": 0,
            "class": "Placeholder"
        }
    debug = "p"
    while debug != "y" and debug != "n":
        debug = input("Debug mode active? (y/n): ")
        if debug == "y":
            char["health"] = int(input("Enter your character's health: "))
            char["mana"] = int(input("Enter your character's mana: "))
            char["defense"] = int(input("Enter your character's defense: "))
            char["dodge"] = int(input("Enter your character's dodge: "))
            char["damage"] = int(input("Enter your character's damage: "))
        elif debug == "n":
            char["health"] = generate_stat()
            char["mana"] = generate_stat()
            char["defense"] = generate_stat()
            char["dodge"] = generate_stat()
            char["damage"] = generate_stat()
        else:
            print("Invalid Value")
    classType = 0
    validClass = ["1", "2", "3", "4", "42"]
    while classType != "1" and classType != "2" and classType != "3" and classType != "4" and classType != "42":
        classType = input("Enter your character's class.  \n1. Barbarian\n2. Mage\n3. Rogue\n4. Knight\nSelection: ")
        if classType == "1":
            char["class"] = "barbarian"
            char["defense"] = char["defense"] * 1.25
            char["dodge"] = char["dodge"] * 0.75
        elif classType == "2":
            char["class"] = "mage"
            char["mana"] = char["mana"] * 1.25
            char["damage"] = char["damage"] * 0.75
        elif classType == "3":
            char["class"] = "rogue"
            char["dodge"] = char["dodge"] * 1.25
            char["defense"] = char["defense"] * 0.75
        elif classType == "4":
            char["class"] = "knight"
            char["damage"] = char["damage"] * 1.25
            char["mana"] = char["mana"] * 0.75
        elif classType == "42":
            char["class"] = "hitchhiker"
            char["health"] = char["health"] * 10
            char["mana"] = char["mana"] * 10
            char["defense"] = char["defense"] * 10
            char["dodge"] = char["dodge"] * 10
            char["damage"] = char["damage"] * 10
        else:
            print("Invalid Value")
    char["health"] = round(char["health"], 2)
    char["mana"] = round(char["mana"], 2)
    char["defense"] = round(char["defense"], 2)
    char["dodge"] = round(char["dodge"], 2)
    char["damage"] = round(char["damage"], 2)
    print(char)
    print()
    return char;

def create_enemy():
    char = {
            "name": "",
            "adj": "",
            "health": 0,
            "mana": 0,
            "defense": 0,
            "dodge": 0,
            "damage": 0,
            "class": "Placeholder"
        }
    enemyName = ["Kobold", "Kobold", "Kobold", "Goblin", "Goblin", "Goblin", "Wolf", "Wolf", "Wolf", "Human", "Human", "Human", "Demon", "Demon", "Demon", "Abomination",]
    adjList = ["wild", "feral", "hostile", "violent", "corrupted"]
    char["name"] = random.choice(enemyName)
    char["adj"] = random.choice(adjList)
    char["health"] = generate_stat()
    char["mana"] = generate_stat()
    char["defense"] = generate_stat()
    char["dodge"] = generate_stat()
    char["damage"] = generate_stat()

    classType = random.randint(1, 4)
    if classType == 1:
        char["class"] = "barbarian"
        char["defense"] = char["defense"] * 1.25
        char["dodge"] = char["dodge"] * 0.75
    elif classType == 2:
        char["class"] = "mage"
        char["mana"] = char["mana"] * 1.25
        char["damage"] = char["damage"] * 0.75
    elif classType == 3:
        char["class"] = "rogue"
        char["dodge"] = char["dodge"] * 1.25
        char["defense"] = char["defense"] * 0.75
    else:
        char["class"] = "knight"
        char["damage"] = char["damage"] * 1.25
        char["mana"] = char["mana"] * 0.75



    if char["name"] == "Abomination":
        char["health"] = char["health"] * 2
        char["mana"] = char["mana"] * 2
        char["defense"] = char["defense"] * 2
        char["dodge"] = char["dodge"] * 2
        char["damage"] = char["damage"] * 2
    
    if char["adj"] == "corrupted":
        char["health"] = char["health"] * 1.4
        char["mana"] = char["mana"] * 1.4
        char["defense"] = char["defense"] * 1.4
        char["dodge"] = char["dodge"] * 1.4
        char["damage"] = char["damage"] * 1.4
    
    char["health"] = round(char["health"], 2)
    curHealth = char["health"]
    char["mana"] = round(char["mana"], 2)
    char["defense"] = round(char["defense"], 2)
    char["dodge"] = round(char["dodge"], 2)
    char["damage"] = round(char["damage"], 2)
    print()
    return char;

def generate_stat():
    normValue = random.randint(30,100)
    normBonus = random.randint(0, 10)
    if normValue <= 90 and normValue >= 81:
        if normBonus >= 6:
            normValue = normValue * 1.10
    elif normValue <= 80 and normValue >= 61:
        if normBonus >= 3:
            normValue = normValue * 1.20
    elif normValue <= 60 and normValue >= 51:
        if normBonus >= 3:
            normValue = normValue * 1.35
    else:
        normValue = normValue * 1.50

    return normValue


###---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---
###---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---
###---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---
###---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---
###---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---

# Player menu will create gameplay following the intro:

def playerMenu(pChar, pGold):
    option = 0
    count = 1
    battleStatus = "n"
    validOpt = ["1","2","3","4","42"]
    while option != "4":
        option = input("What do you wish to do: \n1. Inspect\n2. Inventory\n3. Battle\n4. Retire\nSelection: ")
        if option == "1":
            battleStatus, pGold = inspectMenu(pChar, count, battleStatus, pGold)
        elif option == "2":
            battleStatus = inventoryMenu(pChar, pGold, battleStatus)
        elif option == "3":
             battleStatus, pGold = battleMenu(pChar, pGold)
        elif option == "4":
            print("The Hero(es) have retired\nending the game...")
        elif option == "42":
            print("You watch as the energy of the universe ebbs and flows, you are more perceptive than most heroes.")
            battleStatus = "42"
        elif option != validOpt :
            print("Invalid Selection")

#####################################################################################################################

def inspectMenu(pChar, count, battleStatus, pGold):
    print()
    choice = ""
    while choice == "":
        print()
        print("What do you wish to inspect?")
        choice = input("1. Yourself\n2. Area\nSelection: ")
        if choice == "1":
            battleStatus = playerInspect(pChar, battleStatus)
        elif choice == "2":
            battleStatus, pGold = areaInspect(count, battleStatus, pGold)
        else:
            print("Invalid Selection")
    print()
    return battleStatus, pGold

def playerInspect(pChar, battleStatus):
    print("Player Stats: ")
    print(pChar)
    print()
    if battleStatus == "n":
        print("You feel neutral.")
    elif battleStatus == "g":
        print("After your recent win you feel great.")
    elif battleStatus == "b":
        print("After your recent loss you feel saddened")
    else:
        print("The Python wizard is baffled how you got here, he wishes you the best of luck.")
    battleStatus = "n"
    return battleStatus;

def areaInspect(count, battleStatus, pGold):
    count = count + 1
    if count == 10:
        print('You find a tablet which states, "The meaning of the universe is 42", maybe you should try inputting that somewhere..?')
    else:
        if battleStatus == "n" or battleStatus == "g":
            area = random.randint(1, 3)
        if battleStatus == "b":
            area = random.randint(3, 5)
        if battleStatus == "42":
            area = 6
        if area == 1:
            print("The surrounding area seems calm. \nThe Danger level of this area is low.")
        if area == 2:
            print("The surrounding area seems rustled. \nThe danger level of this area is moderatly low.")
        if area == 3:
            print("Battles are heard faintly in the distance. \nThe danger level of this area is average.")
        if area == 4:
            print("Battle cries of warriors and the howls of creatures are heard all around. \nThe danger level of this area is moderately high.")
        if area == 5:
            print("It is eerily quiet, you see the remains of battle but no combatants, chills run down your back, you feel a foreboding presence is looming. \nThe Danger level of this area is extremely high.")
        if area == 5:
            print("For the moment the world seems at peace, beast are nearby but they seem to ignore you for now.\n The danger level of this area is none.")
    goldChance = random.randint(1, 100)
    if goldChance >= 70:
        newGold = random.randint(1, 10)
        pGold = pGold + newGold
        print("You found " + str(newGold) + " gold coins.")
    battleStatus = "n"
    return battleStatus, pGold;

    
#####################################################################################################################

def inventoryMenu(pChar, pGold, battleStatus):
    print()
    curGold = str(pGold)
    print(pChar["name"] + " has " + curGold + " coins.")
    print()
    battleStatus = "n"
    return battleStatus

#####################################################################################################################

def battleMenu(pChar, pGold):
    print()
    battle = input("Do you wish to start an encounter? (y/n): ")
    if battle == "y":
        battleStatus, pGold = encounterMenu(pChar, pGold)
    print()
    return battleStatus, pGold;

#####################################################################################################################

def encounterMenu(pChar, pGold):
    enemy = create_enemy()
    battleE = enemy
    battleP = pChar
    print(battleP["name"] + " encounters a " + enemy["adj"] + " " + enemy["name"])
    print(enemy)
    print()
    escpChance = False
    while battleE["health"] > 0 and battleP["health"] > 0 and escpChance == False:
        if battleE["health"] > 0 and battleP["health"] > 0 and escpChance == False:
            print(battleP["name"] + "'s turn: ")
            battChoice = 0
            while battChoice < 1 or battChoice > 3:
                battChoice = int(input("What do you wish to do?\n1. Physical Attack\n2. Magic Attack\n3. Escape\nSelection: "))
                if battChoice == 3:
                    if battleP["dodge"] >= battleE["dodge"]:
                        dodgeBonus = random.randint(3,10)
                    else:
                        dodgeBonus = random.randint(1,10)
                    if dodgeBonus > 5:
                        escpChance = True
                        print("The Hero has escaped...")
                    else:
                        print("The Hero fails to escape...")
                elif battChoice == 1 or battChoice == 2:
                    battleE, Dmg = battleChoice(battChoice,battleP,battleE)
                    Dmg = str(Dmg)
                    battleP["health"] = round(battleP["health"])
                    battleE["health"] = round(battleE["health"])
                    print(f"The " + battleP["name"] + " dealt " + Dmg + " damage to " + enemy["adj"] + " " + enemy["name"] + ".")
                else:
                     print("Invalid Input")
            if escpChance == False:
                print()
                curHP = str(battleP["health"])
                curHE = str(battleE["health"])
                if curHP <= "0":
                    curHP = "0"
                    battleP["health"] = 0
                if curHE <= "0":
                    curHE = "0"
                    battleE["health"] = 0
                print(battleP["name"] + " has " + curHP + " hp.")
                print()
                print(battleE["name"] + " has " + curHE + " hp.")
                print()
        else:
            print()
            
        if battleE["health"] > 0 and battleP["health"] > 0 and escpChance == False:
            print(battleE["name"] + "'s turn: ")
            enemyChoice = random.randint(1, 2)
            battleP, eDmg = battleChoice(enemyChoice,battleE,battleP)
            eDmg = str(eDmg)
            battleP["health"] = round(battleP["health"])
            battleE["health"] = round(battleE["health"])
            print(f"The " + enemy["adj"] + " " + enemy["name"] + " dealt " + eDmg + " damage to " + battleP["name"] + ".")
            print()
            curHP = str(battleP["health"])
            curHE = str(battleE["health"])
            if curHP <= "0":
                curHP = "0"
                battleP["health"] = 0
            if curHE <= "0":
                curHE = "0"
                battleE["health"] = 0
            print(battleP["name"] + " has " + curHP + " hp.")
            print()
            print(battleE["name"] + " has " + curHE + " hp.")
            print()
        else:
            print()
    if battleP["health"] >= 0 and battleE["health"] <= 0:
        print("The Hero is victorious!")
        print()
        battleStatus = "g"
        pGold = pGold + 5
    elif battleP["health"] <= 0 and battleE["health"] >= 0:
        print("The " + enemy["adj"] + " " + enemy["name"] + " is victorious!")
        print()
        battleStatus = "b"
        pGold = pGold - 5
    elif escpChance == True:
        battleStatus = "n"
    else:
        print("error")
        battleStatus = "n"
    return battleStatus, pGold;

#####################################################################################################################

def battleChoice(option,fOne,fTwo):
    if option == 1:
        phyDmg = ((fOne["damage"] * 0.2) - (fTwo["defense"] * 0.10))
        fTwo["health"] = fTwo["health"] - phyDmg
        return fTwo, phyDmg
    elif option == 2:
        magDmg = (((fOne["damage"] * 0.1) + (fOne["mana"] * 0.1) - (fTwo["defense"] * 0.10)))
        fTwo["health"] = fTwo["health"] - magDmg
        return fTwo, magDmg
    else:
        print("how did you get here?")

#####################################################################################################################
            
def main():
    print("Starting game....")
    print()
    pChar = create_character()
    pGold = random.randint(10, 50)
    playerMenu(pChar, pGold)

if __name__ == "__main__":
    main()
    
