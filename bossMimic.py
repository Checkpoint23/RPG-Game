import random
import math
import startBattle

enemyAlive = True

class MIMIC():
    global enemyAlive
    def setup(playersHealth, playerMinDamage, playerMaxDamage, playerBDamage, playerMana):
        global playerHealth
        global yourMinDamage
        global yourMaxDamage
        global yourBDamage
        global mana
        global health
        global bonusHP
        playerHealth = playersHealth
        yourMinDamage = playerMinDamage
        yourMaxDamage = playerMaxDamage
        yourBDamage = playerBDamage
        mana = playerMana
        health = 35
        bonusHP = 0
    def PlayersTurn():
        global health
        global playerHealth
        global enemyAlive
        global mana
        global bonusHP
        bonusHP = 0 #defines it?
        print("It is your turn")
        print(f"The mimic has {health} health.")
        print(f"You have {playerHealth} health")
        print(f"You have {mana} mana")
        print(f"You can 1: Fight, 2: Use magic, 3: Block")
        choice = input("")
        while choice != "1" and choice != "2" and choice != "3":
            if choice != "1" and choice != "2" and choice != "3":
                print(f"You can 1: Fight, 2: Use magic, 3: Block")
                choice = input("")
        if choice == "1":
            damage = random.randint(yourMinDamage, yourMaxDamage) + yourBDamage
            health -= damage
            if health <= 0:
                print(f"You did {damage} damage, and killed the mimic!")
                enemyAlive = False
                return
            print(f"You did {damage} damage!")
            print(f"The mimic has {health} health left.")
        if choice == "2":
            print("Which spell do you want to use:")
            print("1: Fireball! Costs 15 mana, deals +5 bonus damage!")
            print("2: Heal! Costs 15 mana, gives you 25% extra of your current health")
            print(f"Type these numbers if you decide otherwise. Remember, you have {mana} mana.")
            print("3: Go back and attack.")
            print("4: Go back and block.")
            spell = input("")
            while spell != "1" and spell != "2" and spell!= "3" and spell != "4":
                if spell != "1" and spell != "2":
                    print("Which spell do you want to use:")
                    print("1: Fireball! Costs 15 mana, deals +5 bonus damage!")
                    print("2: Heal! Costs 15 mana, gives you 25% extra of your current health")
                    print(f"Type these numbers if you decide otherwise. Remember, you have {mana} mana.")
                    print("3: Go back and attack.")
                    print("4: Go back and block.")
                    spell = input("")
            if spell == "1":
                if mana >= 15:
                    damage = random.randint(yourMinDamage, yourMaxDamage) + yourBDamage + 5
                    health -= damage
                    mana -= 15
                    if health <= 0:
                        print(f"You did {damage} damage, and killed the mimic!")
                        enemyAlive = False
                        return
                    print(f"You did {damage} damage")
                    print(f"The mimic has {health} health left.")
                else:
                    print("You don't have enough mana.")
                    print(f"You only had {mana} mana, but you needed 15 mana.")
            if spell == "2":
                if mana >= 15:
                    increasedHealth = math.ceil(playerHealth/4)
                    playerHealth += increasedHealth
                    mana -= 15
                    print(f"You gained {increasedHealth} health, and now have {playerHealth} HP!")
                else:
                    print("You don't have enough mana!")
                    print(f"You only had {mana} mana, but you needed 15 mana.")
            if spell == 3:
                damage = random.randint(yourMinDamage, yourMaxDamage) + yourBDamage
                health -= damage
                if health <= 0:
                    print(f"You did {damage} damage, and killed the mimic!")
                    enemyAlive = False
                    return
                print(f"You did {damage} damage!")
                print(f"The Mimic has {health} health left.")
            if spell == 4:
                manaGain = (0.0000405 * ((mana-30) ** 3)) - (0.01 * ((mana-50) ** 2))
                manaGain -= 39
                manaGain -= manaGain * 2
                if mana >= 150:
                    manaGain = 9
                manaGain = math.floor(manaGain)
                mana += manaGain
                print(f"You gained {manaGain} mana!")
                if playerHealth < 5:
                    bonusHP = random.randint(1,3)
                else:
                    bonusHP = random.randint(1, math.floor(playerHealth/3))
                print(f"You will block up to {bonusHP} damage this round.")
        if choice == "3":
            manaGain = (0.0000405 * ((mana-30) ** 3)) - (0.01 * ((mana-50) ** 2))
            manaGain -= 39
            manaGain -= manaGain * 2
            if mana >= 150:
                manaGain = 9
            manaGain = math.floor(manaGain)
            mana += manaGain
            print(f"You gained {manaGain} mana!")
            if playerHealth < 5:
                bonusHP = random.randint(1,3)
            else:
                bonusHP = random.randint(1, math.floor(playerHealth/3))
            print(f"You will block up to {bonusHP} damage this round.")
    def mimicsTurn():
        global yourBDamage
        global health
        global playerHealth
        global bonusHP
        choice = random.randint(1,10)
        if choice == 1 or choice == 2:
            print("The mimic uses Bite!")
            damage = random.randint(1,4) + 2
            if bonusHP > 0:
                if bonusHP >= damage:
                    print("You blocked all damage!")
                    return
                else:
                    print(f"You blocked {bonusHP} damage")
                    damage -= bonusHP
            print(f"The mimic dealt {damage} damage!")
            playerHealth -= damage
        if choice == 3 or choice == 4:
            print("The mimic uses Lick!")
            damage = random.randint(1,4)
            if yourBDamage > 0:
                if bonusHP >= damage:
                    print("The lick failed to get through your block.")
                else:
                    yourBDamage -= 1
                    print("Your Bonus Damage decreased by 1!")
            else:
                print("It wasn't very effective without anything to debuff.")
            if bonusHP > 0:
                if bonusHP >= damage:
                    print("You blocked all damage!")
                    return
                else:
                    print(f"You blocked {bonusHP} damage")
                    damage -= bonusHP
            print(f"The mimic dealt {damage} damage!")
            playerHealth -= damage
        if choice == 5 or choice == 6:
            print("The Mimic used Vampiric bite!")
            damage = random.randint(1,4)
            health += damage
            playerHealth -= damage
        if choice == 7 or choice == 8:
            print("The mimic uses Pounce!")
            damage = random.randint(1,4)
            hitagain = random.randint(1,2)
            if hitagain == 1:
                print("The mimic restrains you and attacks again!")
                damage += random.randint(1,4)
                hitagain = random.randint(1,2)
                if hitagain == 1:
                    print("The mimic keeps your restrained and attacks again!")
                    damage += random.randint(1,4)
            else:
                print("You manage to get the mimic off of you.")
            if bonusHP > 0:
                if bonusHP >= damage:
                    print("You blocked all damage!")
                    return
                else:
                    print(f"You blocked {bonusHP} damage")
                    damage -= bonusHP
            print(f"The mimic dealt {damage} damage!")
            playerHealth -= damage
        if choice == 9:
            print("Mimic uses spit!")
            damage = 1
            if bonusHP > 0:
                print("You blocked all damage!")
                bonusHP = 0
            else:
                print(f"The mimic dealt {damage} damage!")
                playerHealth -= damage
        if choice == 10:
            print("The mimic missed their attack!")
        if playerHealth <= 0:
            startBattle.battle.onDeath()
            return
