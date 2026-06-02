import enemyBattle
import bossMimic

class battle:
    enemyTypeWorld1 = ["goblin", "boulderman", "slime"]
    enemyStatHealthWorld1 = [5,15,10]
    enemyStatBDamageWorld1 = [3,1,2]
    enemyStatMinDamageWorld1 = [5,1,2]
    enemyStatMaxDamgeWorld1 = [15,10,4]
    maxPlayerHealth = 15
    mana = 15
    
    def selectEnemyWorld (world):
        if world == 1:
            enemyBattle.fightEnemy.whatEnemy(
                battle.enemyTypeWorld1,
                battle.enemyStatHealthWorld1,
                battle.enemyStatBDamageWorld1,
                battle.enemyStatMinDamageWorld1,
                battle.enemyStatMaxDamgeWorld1,
                battle.maxPlayerHealth,
                battle.mana
            )

    def runBattle ():
        enemyBattle.fightEnemy.beginBattle(enemyBattle.enemy)
        while enemyBattle.enemyAlive and enemyBattle.playerHealth > 0:
            if enemyBattle.enemyAlive: enemyBattle.fightEnemy.theirTurn(enemyBattle.enemy)
            else: return
            if enemyBattle.playerHealth > 0: enemyBattle.fightEnemy.yourTurn(enemyBattle.enemy, 2, 1, 5)
            else: return
    
    def fightBoss(boss):
        if boss == "Mimic":
            bossMimic.MIMIC.setup(
                playersHealth=battle.maxPlayerHealth,
                playerBDamage = 2,
                playerMinDamage = 1,
                playerMaxDamage = 5,
                playerMana= battle.mana
                )
        while bossMimic.enemyAlive and bossMimic.playerHealth > 0:
            if bossMimic.enemyAlive: bossMimic.MIMIC.mimicsTurn()
            else: return
            if bossMimic.playerHealth > 0: bossMimic.MIMIC.PlayersTurn() 
            else: return