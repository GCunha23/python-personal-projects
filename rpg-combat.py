"""
Author: Gonçalo Cunha (GitHub: GCunha23)
Date Created: 11/01/2025
Last Modified: 17/01/2025

Description:
A turn based combat mini-game.
"""

import random

# CHARACTERS' STATS

ThowattzStats = {
    "HP":100,
    "Attack":1.0,
    "Defense":0
}

RootorbStats = {
    "HP":100,
    "Attack":1.0,
    "Defense":0
}


# CHARACTER LIST

characters = {
    "Thowattz":ThowattzStats,
    "Rootorb":RootorbStats
}


# CHARACTERS' MOVES

moves = {
    "Thowattz":{
        "Volt Spear":{"type":"damage", "value":20},
        "Static Energy":{"type":"condition","effect":"paralyze"},
        "Magnetic Field":{"type":"status","stat":"Defense","value":5},
        "Recharge":{"type":"status","stat":"Attack","value":0.5}
    },
    "Rootorb":{
        "Wood Shards":{"type":"damage", "value":15},
        "Splinter":{"type":"damage-over-time","value":5,"turns":3},
        "Healing Roots":{"type":"heal","value":20},
        "Leaf Shield":{"type":"status","stat":"Defense","value":5}
    }
}


# START MENU

print(r"""
      
+==============================================================+
|   ____  ____   ____    ____                _           _     |
|  |  _ \|  _ \ / ___|  / ___|___  _ __ ___ | |__   __ _| |_   |
|  | |_) | |_) | |  _  | |   / _ \| '_ ` _ \| '_ \ / _` | __|  |
|  |  _ <|  __/| |_| | | |__| (_) | | | | | | |_) | (_| | |_   |
|  |_| \_\_|    \____|  \____\___/|_| |_| |_|_.__/ \__,_|\__|  |
|                                                              |
+==============================================================+
      
""")


# MAIN MENU

def mainMenu():

    while True:
        menuInput = input("""A: Play Game 
B: Quit
                          
Pick an option: """).upper()
        print()
        if menuInput == "A":
            playerCharacter, computerCharacter = characterSelection()
            battle(playerCharacter,computerCharacter)
            break
        elif menuInput == "B":
            print("Thank you for playing! Goodbye!")
            exit()
        else:
            print("Invalid choice. Please choose 'A' or 'B'.")
            print()


# CHARACTER SELECTION

def characterSelection():
    print("Choose your character:")
    print("A: Thowattz (Electric-type)")
    print("B: Rootorb (Grass-type)")
    
    print()

    while True:
        characterPick = input("Pick a character: ").upper()
        if characterPick == "A":
            playerCharacter = "Thowattz"
            computerCharacter = "Rootorb"
            break
        elif characterPick == "B":
            playerCharacter = "Rootorb"
            computerCharacter = "Thowattz"
            break
        else:
            print("Invalid choice. Please choose 'A' or 'B'.")

    print()

    print(f"You chose {playerCharacter}!")
    print(f"The computer will use {computerCharacter}!")

    return playerCharacter, computerCharacter


# BATTLE

def battle(playerCharacter, computerCharacter):
    playerStats = characters[playerCharacter].copy()
    computerStats = characters[computerCharacter].copy()

    # Initialize status effects
    playerParalyzed = False
    computerParalyzed = False
    playerDoT = {"active": False, "value": 0, "turns": 0}
    computerDoT = {"active": False, "value": 0, "turns": 0}

    print()
    print(f"The battle begins! {playerCharacter} vs. {computerCharacter}")
    print()

    while playerStats["HP"] > 0 and computerStats["HP"] > 0:
        # Display current HP
        print()
        print(f"Your {playerCharacter} - HP: {playerStats['HP']}")
        print(f"Opponent's {computerCharacter} - HP: {computerStats['HP']}")
        print()

        # === Player's Turn ===
        # Check if Player is paralyzed
        if playerParalyzed:
            if random.random() < 0.5:  # 50% chance to skip turn
                print(f"{playerCharacter} is paralyzed and cannot move!")
                playerParalyzed = False  # Paralysis ends after one skipped turn
            else:
                print(f"{playerCharacter} fought through paralysis!")
        else:
            # Display moves
            print()
            print("Available moves:")
            for i, move in enumerate(moves[playerCharacter], 1):
                print(f"{i}. {move}")

            # Handle input
            moveChoice = int(input("Choose your move (enter the number): ")) - 1
            chosenMove = list(moves[playerCharacter].keys())[moveChoice]
            print()
            print(f"{playerCharacter} used {chosenMove}!")

            # Apply player's move effects
            moveEffect = moves[playerCharacter][chosenMove]
            if moveEffect["type"] == "damage":
                damage = max(0, moveEffect["value"] * playerStats["Attack"] - computerStats["Defense"])
                computerStats["HP"] -= damage
                print(f"{computerCharacter} took {damage:.1f} damage!")
            elif moveEffect["type"] == "heal":
                heal = moveEffect["value"]
                playerStats["HP"] = min(playerStats["HP"] + heal, 100)
                print(f"{playerCharacter} healed {heal} HP!")
            elif moveEffect["type"] == "status":
                stat = moveEffect["stat"]
                value = moveEffect["value"]

                if stat == "Defense":
                    if playerStats[stat] >= 20: # Check if Defense is already at the cap
                        print(f"{playerCharacter}'s {stat} can't go any higher!")
                    else:
                        playerStats[stat] = min(playerStats[stat] + value, 20) # Cap Defense at 20
                        print(f"{playerCharacter}'s {stat} increased by {value}!")
                else:
                    playerStats[stat] += value
                    print(f"{playerCharacter}'s {stat} increased by {value}!")
            elif moveEffect["type"] == "condition" and moveEffect["effect"] == "paralyze":
                computerParalyzed = True
                print(f"{computerCharacter} is paralyzed and might not move!")
            elif moveEffect["type"] == "damage-over-time":
                computerDoT = {"active": True, "value": moveEffect["value"], "turns": moveEffect["turns"]}
                print(f"{computerCharacter} will take {moveEffect['value']} damage for {moveEffect['turns']} turns!")

        # Apply DoT to player
        if playerDoT["active"]:
            playerStats["HP"] -= playerDoT["value"]
            playerDoT["turns"] -= 1
            print(f"{playerCharacter} took {playerDoT['value']} damage from DoT!")
            if playerDoT["turns"] <= 0:
                playerDoT["active"] = False

        # Check if computer is defeated
        if computerStats["HP"] <= 0:
            print()
            print(f"You defeated {computerCharacter}! You win!")
            break

        # === Computer's Turn ===
        # Check if Computer is paralyzed
        if computerParalyzed:
            if random.random() < 0.5:  # 50% chance to skip turn
                print(f"{computerCharacter} is paralyzed and cannot move!")
                computerParalyzed = False  # Paralysis ends after one skipped turn
            else:
                print(f"{computerCharacter} fought through paralysis!")
        else:
            # Randomly pick a move
            computerMove = random.choice(list(moves[computerCharacter].keys()))
            print(f"{computerCharacter} used {computerMove}!")

            # Apply computer's move effects
            compMoveEffect = moves[computerCharacter][computerMove]
            if compMoveEffect["type"] == "damage":
                damage = max(0, compMoveEffect["value"] * computerStats["Attack"] - playerStats["Defense"])
                playerStats["HP"] -= damage
                print(f"{playerCharacter} took {damage:.1f} damage!")
            elif compMoveEffect["type"] == "heal":
                heal = compMoveEffect["value"]
                computerStats["HP"] = min(computerStats["HP"] + heal, 100)
                print(f"{computerCharacter} healed {heal} HP!")
            elif compMoveEffect["type"] == "status":
                stat = compMoveEffect["stat"]
                value = compMoveEffect["value"]

                if stat == "Defense":
                    if computerStats[stat] >= 20: # Check if Defense is already at the cap
                        print(f"{computerCharacter}'s {stat} can't go any higher!")
                    else:
                        computerStats[stat] = min(computerStats[stat] + value, 20) # Cap Defense at 20
                        print(f"{computerCharacter}'s {stat} increased by {value}!")
                else:
                    playerStats[stat] += value
                    print(f"{playerCharacter}'s {stat} increased by {value}!")
            elif compMoveEffect["type"] == "condition" and compMoveEffect["effect"] == "paralyze":
                playerParalyzed = True
                print(f"{playerCharacter} is paralyzed and might not move!")
            elif compMoveEffect["type"] == "damage-over-time":
                playerDoT = {"active": True, "value": compMoveEffect["value"], "turns": compMoveEffect["turns"]}
                print(f"{playerCharacter} will take {compMoveEffect['value']} damage for {compMoveEffect['turns']} turns!")

        # Apply DoT to computer
        if computerDoT["active"]:
            computerStats["HP"] -= computerDoT["value"]
            computerDoT["turns"] -= 1
            print(f"{computerCharacter} took {computerDoT['value']} damage from DoT!")
            if computerDoT["turns"] <= 0:
                computerDoT["active"] = False

        # Check if player is defeated
        if playerStats["HP"] <= 0:
            print()
            print(f"{computerCharacter} defeated your {playerCharacter}. You lose.")
            break

        print("""

========== End of turn ==========
              
              """)

    print()
    print("Battle Over!")
    print("Thank you for playing!")


# RUN GAME
mainMenu()