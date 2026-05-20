import enemyBattle

enemyTypeWorld1 = ["goblin", "boulderman", "slime"]
enemyStatHealthWorld1 = [5, 15, 10]
enemyStatBDamageWorld1 = [3, 1, 2]
enemyStatMinDamageWorld1 = [5, 1, 3]
enemyStatMaxDamgeWorld1 = [15, 10, 4]
maxPlayerHealth = 15

enemyBattle.fightEnemy.whatEnemy(enemyTypeWorld1,
    enemyStatHealthWorld1,
    enemyStatBDamageWorld1,
    enemyStatMinDamageWorld1,
    enemyStatMaxDamgeWorld1,
    maxPlayerHealth,
)

print(enemyBattle.playerHealth)
enemyBattle.fightEnemy.beginBattle(enemyBattle.enemy)
while enemyBattle.enemyAlive and enemyBattle.playerHealth > 0:
    enemyBattle.fightEnemy.theirTurn(enemyBattle.enemy)
    if not enemyBattle.enemyAlive or enemyBattle.playerHealth <= 0:
        break
    enemyBattle.fightEnemy.yourTurn(enemyBattle.enemy, 2, 1, 5)