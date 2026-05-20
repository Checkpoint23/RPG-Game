import random

enemyTypeWorld1 = ["goblin", "boulderman", "slime"]
enemyStatHealthWorld1 = [5, 15, 10]
enemyStatBDamageWorld1 = [3, 1, 2]
enemyStatMinDamageWorld1 = [5,1,2]
enemyStatMaxDamgeWorld1 = [15,10,4]

class fightEnemy:
    def whatEnemy (enemyList, enemyHealth, LenemyBDamage, LenemyMinDamage, LenemyMaxDamage, startingPlayerHealth):
        global enemy
        global health
        global enemyBDamage
        global enemyMinDamage
        global enemyMaxDamage
        global enemyAlive
        global playerHealth
        lenEnemy = (len(enemyList))
        idx = random.randint(1, lenEnemy) - 1
        enemy = enemyList[idx]
        health = enemyHealth[idx]
        enemyBDamage = LenemyBDamage[idx]
        enemyMinDamage = LenemyMinDamage[idx]
        enemyMaxDamage = LenemyMaxDamage[idx]
        enemyAlive = True
        playerHealth = startingPlayerHealth
        return enemy, health, enemyBDamage, enemyMinDamage, enemyMaxDamage, enemyAlive, playerHealth
    def beginBattle (enemy):
        print(f"{enemy} appeared")
    def yourTurn (enemy, yourBDamge, yourMinDamage, yourMaxDamage):
        global health
        global enemyAlive
        print("It is your turn")
        print(f"{enemy} has {health} health.")
        print(f"You can 1: Fight, 2: Use magic, 3: Block")
        choice = input("")
        if choice != "1" and choice != "2" and choice != "3":
            print("Invalid input")
        else:
            if choice == "1":
                damage = random.randint(yourMinDamage, yourMaxDamage) + yourBDamge
                health -= damage
                if health <= 0:
                    print(f"You did {damage} damage, and killed {enemy}")
                    enemyAlive = False
                    return
                print(f"You did {damage} damage!")
                print(f"{enemy} has {health} health left.")
            if choice == "2":
                print("this hasnt been implemented yet lmao")
            if choice == "3":
                print("this hasnt been implemented yet lmao")
    def theirTurn (enemy):
        global health
        global enemyBDamage
        global enemyMinDamage
        global enemyMaxDamage 
        global playerHealth
        print(f"It is {enemy}'s turn.")
        if enemy == "slime":
            attack = random.randint(1,3)
            if attack == 1:
                print("Slime uses bounce")
                enemyBDamage += + 1
                print("His bonus damage increases by 1.")
            if attack == 2:
                print("Slime uses absorb mass!")
                gainHealth = random.randint(1, 3)
                health += gainHealth
                print(f"Slime gained {gainHealth} health")
            if attack == 3:
                print("Slime uses blunt force!")
                damage = random.randint(enemyMinDamage, enemyMaxDamage) + enemyBDamage
                playerHealth -= damage
                print(f"Slime dealt {damage} Damage!")
                print(f"You have {playerHealth} hp left.")
        if enemy == "goblin":
            print("Goblin uses Goblin Shenanigins")
            if health >= 6:
                print("Goblin is dissapointed in you.")
                damage = random.randint(enemyMinDamage, enemyMaxDamage) + enemyBDamage + 1
                playerHealth -= damage
                print(f"Goblin deals {damage} damage!")
                print(f"You have {playerHealth} health left.")

            if health == 5:
                print("Goblin increases his health by 1!")
                health += 1
            if health == 4:
                print("Goblin dances around and does nothing!")
            if health == 3 or health == 2:
                print("Goblin attacks you with a knife")
                damage = random.randint(enemyMinDamage, enemyMaxDamage) + enemyBDamage
                playerHealth -= damage
                print(f"You have {playerHealth} hp left.")
            if health == 1:
                print("Goblin resets his health to 5!")
                health = 5
        if enemy == "boulderman":
            print("Boulderman uses Boulder!")

