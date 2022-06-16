import random


class Class:
    allClasses = ['mage', 'warrior', 'scout']
    mage = {
        'dodge': 0
    }
    warrior = {
        'dodge': 25
    }
    scout = {
        'dodge': 50
    }


class YourStats:
    level = 183
    strength = 1321
    defense = strength / 2
    dexterity = 5971
    evasion = dexterity / 2
    intelligence = 1410
    resistance = intelligence / 2
    weapondmg = 478
    weaponmindmg = 468
    weaponmaxdmg = 488
    constitution = 4303
    luck = 1929
    armor = 4383
    levelplusone = level + 1
    hp = constitution * 4 * levelplusone


class EnemyStats:
    level = 183
    strength = 1321
    defense = strength / 2
    dexterity = 5971
    evasion = dexterity / 2
    intelligence = 1410
    resistance = intelligence / 2
    weapondmg = 478
    weaponmindmg = 468
    weaponmaxdmg = 488
    constitution = 4303
    luck = 1929
    armor = 4383
    levelplusone = level + 1
    hp = constitution * 4 * levelplusone


def yourattack():
    dexsub = YourStats.dexterity - EnemyStats.defense
    dexslashtenplusone = dexsub / 10 + 1
    mindmg = YourStats.weaponmindmg * dexslashtenplusone
    maxdmg = YourStats.weaponmaxdmg * dexslashtenplusone
    randomdmg = random.randint(round(mindmg), round(maxdmg))
    damagereduction = YourStats.armor / EnemyStats.level
    if damagereduction > 25:
        damagereduction = 25
    reduction = 100 / damagereduction
    enemylvltimestwo = EnemyStats.level * 2
    crit = 0
    critchance = YourStats.luck * 5 / enemylvltimestwo
    if critchance > 50:
        critchance = 50
    x = random.randint(0, 99)
    if x < critchance:
        crit = 1
    dmg = randomdmg / reduction
    if crit == 1:
        dmg = dmg * 2
    n = random.randint(0, 99)
    if n < Class.warrior['dodge'] and crit == 0:
        dmg = 0
        return dmg
    else:
        return round(dmg)


def enemyattack():
    dexsub = EnemyStats.dexterity - YourStats.defense
    dexslashtenplusone = dexsub / 10 + 1
    mindmg = EnemyStats.weaponmindmg * dexslashtenplusone
    maxdmg = EnemyStats.weaponmaxdmg * dexslashtenplusone
    randomdmg = random.randint(round(mindmg), round(maxdmg))
    damagereduction = EnemyStats.armor / YourStats.level
    if damagereduction > 25:
        damagereduction = 25
    reduction = 100 / damagereduction
    yourlvltimestwo = EnemyStats.level * 2
    crit = 0
    critchance = EnemyStats.luck * 5 / yourlvltimestwo
    if critchance > 50:
        critchance = 50
    x = random.randint(0, 99)
    if x < critchance:
        crit = 1
    dmg = randomdmg / reduction
    if crit == 1:
        dmg = dmg * 2
    n = random.randint(0, 99)
    if n < Class.warrior['dodge'] and crit == 0:
        dmg = 0
        return dmg
    else:
        return round(dmg)


def yourclasscontrol(yourclasschar):
    for i in Class.allClasses:
        if i == yourclasschar:
            return yourclasschar


def enemyclasscontrol(enemyclasschar):
    for i in Class.allClasses:
        if i == enemyclasschar:
            return enemyclasschar


def yourclass():
    print("Enter your class: ")
    loopcounter = 1
    for i in Class.allClasses:
        print(str(loopcounter) + ') ' + i.capitalize())
        loopcounter += 1
    userinput = input().lower()
    return userinput


def enemyclass():
    print("Enter your enemy class: ")
    loopcounter = 1
    for i in Class.allClasses:
        print(str(loopcounter) + ') ' + i.capitalize())
        loopcounter += 1
    userinput = input().lower()
    return userinput


yourcharclass = yourclass()
enemycharclass = enemyclass()
yourselectedclass = yourclasscontrol(yourcharclass)
enemyselectedclass = enemyclasscontrol(enemycharclass)
print(yourselectedclass + ' vs ' + enemyselectedclass)


def fight():
    yourhp = YourStats.hp
    enemyhp = EnemyStats.hp
    round = 1
    while yourhp > 0 and enemyhp > 0:
        print('\n___________Round ' + str(round) + '____________\n')
        print('your hp:' + str(yourhp) + '\n' + 'enemy hp: ' + str(enemyhp) + '\n')
        youratt = yourattack()
        enemyhp -= youratt
        if enemyhp <= 0:
            print('your hp afterwards: ' + str(yourhp))
            print('enemy hp afterwards: ' + str(enemyhp))
            print('You won!!!')
            return
        enemyatt = enemyattack()
        yourhp -= enemyatt
        if yourhp <= 0:
            print('your hp afterwards: ' + str(yourhp))
            print('enemy hp afterwards: ' + str(enemyhp))
            return
        print('your hp afterwards: ' + str(yourhp))
        print('enemy hp afterwards: ' + str(enemyhp))
        round += 1
    print('')


fight()
