import enemyBattle
import bossMimic
import Movement
import MovementManager
import json
import sys
from pathlib import Path

class battle:
    enemyTypeWorld1 = ["goblin", "boulderman", "slime"]
    enemyStatHealthWorld1 = [5,15,10]
    enemyStatBDamageWorld1 = [3,1,2]
    enemyStatMinDamageWorld1 = [5,1,2]
    enemyStatMaxDamgeWorld1 = [15,10,4]
    
    def setPlayerStats(maxHealth, maxMana, minimumDamage, maximumDamage, extraDamage):
        global maxPlayerHealth
        global mana
        global minDamage
        global maxDamage
        global bonusDamage
        maxPlayerHealth = maxHealth
        mana = maxMana
        minDamage = minimumDamage
        maxDamage = maximumDamage
        bonusDamage = extraDamage

    def onDeath():
        FILE_PATH = Path("Save1.json")
        if FILE_PATH.is_file():
            print("You unfortunately died in battle. It is a shame, but something stirs within you.")
            print("A stored memory, something to go back to.")
            print("The ability to try again.")
            print("When you wake up again, you will have the ability to either return to a stored memory, or to let the world turn to dust. But for now, rest.")
            sys.exit()
        else:
            print("You fell in battle. Without the power of having a stored memory, your body stays there defeated. And thus, the world turns to dust.")

    def selectEnemyWorld (world):
        global maxPlayerHealth
        global mana
        global minDamage
        global maxDamage
        global bonusDamage
        if world == 1:
            enemyBattle.fightEnemy.whatEnemy(
                battle.enemyTypeWorld1,
                battle.enemyStatHealthWorld1,
                battle.enemyStatBDamageWorld1,
                battle.enemyStatMinDamageWorld1,
                battle.enemyStatMaxDamgeWorld1,
                maxPlayerHealth,
                mana,
                minDamage,
                maxDamage,
                bonusDamage
            )

    def runBattle ():
        enemyBattle.fightEnemy.beginBattle(enemyBattle.enemy)
        while enemyBattle.enemyAlive and enemyBattle.playerHealth > 0:
            if enemyBattle.enemyAlive: enemyBattle.fightEnemy.theirTurn(enemyBattle.enemy)
            else: return
            if enemyBattle.playerHealth > 0: enemyBattle.fightEnemy.yourTurn(enemyBattle.enemy)
            else: return
        if enemyBattle.playerHealth <= 0:
            battle.onDeath()
    def fightBoss(boss):
        global maxPlayerHealth
        global mana
        global minDamage
        global maxDamage
        global bonusDamage
        if boss == "Mimic":
            bossMimic.MIMIC.setup(
                playersHealth = maxPlayerHealth,
                playerBDamage = bonusDamage,
                playerMinDamage = minDamage,
                playerMaxDamage = maxDamage,
                playerMana = mana
                )
        while bossMimic.enemyAlive and bossMimic.playerHealth > 0:
            if bossMimic.enemyAlive: bossMimic.MIMIC.mimicsTurn()
            else: return
            if bossMimic.playerHealth > 0: bossMimic.MIMIC.PlayersTurn() 
            else: return
        if bossMimic.playerHealth <= 0:
            battle.onDeath()
    def changeStats(whatstat, amount):
        if whatstat == "H":
            global maxPlayerHealth
            maxPlayerHealth += amount
        if whatstat == "M":
            global mana
            mana += amount
        if whatstat == "MD":
            global minDamage
            global maxDamage
            minDamage += amount
            maxDamage += amount
        if whatstat == "BD":
            global bonusDamage
            bonusDamage += amount
    def save(x, y, world, beenToRooms, inventory, questlog):
        global maxPlayerHealth
        global mana
        global minDamage
        global maxDamage
        global bonusDamage
        print("Would you like to save? y/n")
        save = input("")
        if save == "y":
            print("Saving.")
            savedata = {
                "World": world,
                "Current X": x,
                "Current Y": y,
                "Current HP": maxPlayerHealth,
                "Current Mana": mana,
                "Current Minimum Damage": minDamage,
                "Current Maximum Damage": maxDamage,
                "Current Bonus Damage": bonusDamage,
                "Inventory": inventory,
                "Rooms the player has been to": beenToRooms,
                "Quest Log": questlog
            }
            FILE_PATH = "Save1.json"
            with open(FILE_PATH, "w") as file:
                json.dump(savedata, file, indent=4)
            print("Saved successsfully.")
        if save == "n":
            print("Remember, if you die, you can always reload a save!")