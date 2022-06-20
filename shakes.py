import random


class Class:
    allClasses = {'mage': {'dodge': 0,
                           'max reduction': 10,
                           'main stat': 'intelligence',
                           'hp counter': 2,
                           'magic': 1},
                  'warrior': {'dodge': 25,
                              'max reduction': 50,
                              'main stat': 'strength',
                              'hp counter': 5,
                              'magic': 0},
                  'scout': {'dodge': 50,
                            'max reduction': 25,
                            'main stat': 'dexterity',
                            'hp counter': 4,
                            'magic': 0},
                  'battle mage': {'dodge': 0,
                                  'max reduction': 50,
                                  'main stat': 'strength',
                                  'hp counter': 5,
                                  'magic': 1},
                  'berserker': {'dodge': 0,
                                'max reduction': 25,
                                'main stat': 'strength',
                                'hp counter': 4,
                                'magic': 0},
                  'assassin': {'dodge': 0,
                               'max reduction': 25,
                               'main stat': 'dexterity',
                               'hp counter': 4,
                               'magic': 0},
                  'demon hunter': {'dodge': 0,
                                   'max reduction': 50,
                                   'main stat': 'dexterity',
                                   'hp counter': 4,
                                   'magic': 0},
                  'druid': {'dodge': 0,
                            'max reduction': 50,
                            'main stat': 'intelligence',
                            'hp counter': 2,
                            'magic': 0}
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


def stat_setter(this_class_name, this_class, this_stats, oponent_stats):
    hp = this_stats.constitution * this_class['hp counter'] * (this_stats.level + 1)
    mindmg = 0
    maxdmg = 0
    if this_class['main stat'] == 'intelligence':
        mindmg = this_stats.weaponmindmg * ((this_stats.intelligence - oponent_stats.resistance) / 10 + 1)
        maxdmg = this_stats.weaponmaxdmg * ((this_stats.intelligence - oponent_stats.resistance) / 10 + 1)
    if this_class['main stat'] == 'strength':
        mindmg = this_stats.weaponmindmg * ((this_stats.strength - oponent_stats.defense) / 10 + 1)
        maxdmg = this_stats.weaponmaxdmg * ((this_stats.strength - oponent_stats.defense) / 10 + 1)
    if this_class['main stat'] == 'dexterity':
        mindmg = this_stats.weaponmindmg * ((this_stats.dexterity - oponent_stats.evasion) / 10 + 1)
        maxdmg = this_stats.weaponmaxdmg * ((this_stats.dexterity - oponent_stats.evasion) / 10 + 1)
    damage_reduction = this_stats.armor / oponent_stats.level
    if this_class_name == 'battle mage':
        damage_reduction += 40
    if damage_reduction > this_class['max reduction']:
        damage_reduction = this_class['max reduction']
    crit_chance = this_stats.luck * 5 / (oponent_stats.level * 2)
    if crit_chance > 50:
        crit_chance = 50
    stats = {'hp': hp,
             'mindmg': mindmg,
             'maxdmg': maxdmg,
             'damage_reduction': damage_reduction,
             'crit_chance': crit_chance
             }
    return stats


def attack(mindmg, maxdmg, damage_reduction, crit_chance, this_class):
    random_dmg = random.randint(round(mindmg), round(maxdmg))
    dmg = random_dmg / (100 / damage_reduction)
    crit_range = random.randint(0, 99)
    crit = 0
    if crit_range < crit_chance:
        dmg *= 2
        crit = 1
    n = random.randint(0, 99)
    if n < this_class['dodge'] and crit == 0:
        return 0
    else:
        return round(dmg)


def class_selection():
    while 1:
        loop_stopper = 0
        your_class_name = enter_class('your')
        your_class = 0
        for i in Class.allClasses:
            if your_class_name == i:
                your_class = Class.allClasses[i]
                loop_stopper += 1
        enemy_class_name = enter_class('enemy')
        enemy_class = 0
        for i in Class.allClasses:
            if enemy_class_name == i:
                enemy_class = Class.allClasses[i]
                loop_stopper += 1
        selected_classes = {'your_class_name': your_class_name,
                            'your_class': your_class,
                            'enemy_class_name': enemy_class_name,
                            'enemy_class': enemy_class
                            }
        if loop_stopper == 2:
            print(your_class_name.capitalize() + ' vs ' + enemy_class_name.capitalize())
            return selected_classes
        print('You must have miss clicked, try again :)\n')


def enter_class(who):
    print("Enter " + who + " class: ")
    loop_counter = 1
    for i in Class.allClasses:
        print(str(loop_counter) + ') ' + i.capitalize())
        loop_counter += 1
    user_input = input().lower()
    return user_input


def fight(selected_classes):
    your_stats = stat_setter(selected_classes['your_class_name'],
                             selected_classes['your_class'],
                             YourStats,
                             EnemyStats)
    enemy_stats = stat_setter(selected_classes['enemy_class_name'],
                              selected_classes['enemy_class'],
                              EnemyStats,
                              YourStats)
    your_hp = your_stats['hp']
    enemy_hp = enemy_stats['hp']
    your_revives = 1
    enemy_revives = 1
    round = 1
    dmg_scaling = 1.2
    if selected_classes['your_class_name'] == 'battle mage' and selected_classes['enemy_class']['magic'] != 1:
        enemy_hp -= min(int(your_hp / 3), int(enemy_hp / 3))
        print('FIREBAAAAAAAALLLLLLLL')
    if selected_classes['enemy_class_name'] == 'battle mage' and selected_classes['your_class']['magic'] != 1:
        your_hp -= min(int(your_hp / 3), int(enemy_hp / 3))
        print('FIREBAAAAAAAALLLLLLLL')
    while 1:
        print('\n___________Round ' + str(round) + '____________\n')
        print('your hp:' + str(your_hp) + '\n' + 'enemy hp: ' + str(enemy_hp) + '\n')
        attack_counter = 2
        while attack_counter == 1 or attack_counter == 2:
            your_attack = attack(your_stats['mindmg'],
                                 your_stats['maxdmg'],
                                 your_stats['damage_reduction'],
                                 your_stats['crit_chance'],
                                 selected_classes['your_class'])
            enemy_hp -= int(your_attack * dmg_scaling)
            if selected_classes['your_class_name'] == 'assassin':
                attack_counter -= 1
            elif selected_classes['your_class_name'] == 'berserker':
                attack_counter = random.randint(0, 1)
            else:
                attack_counter = 0
        if selected_classes['enemy_class_name'] == 'demon hunter' and enemy_hp <= 0 and enemy_revives == 1:
            n = random.randint(0, 3)
            if n == 0:
                enemy_hp = enemy_stats['hp']
                enemy_revives = 0
        dmg_scaling += 0.2
        if enemy_hp <= 0:
            n = random.randint(0, 3)
            if selected_classes['enemy_class_name'] == 'demon hunter' and enemy_revives == 1 and n == 0:
                enemy_hp = enemy_stats['hp']
                enemy_revives = 0
                print('ENEMY REVIVED!!!!!!!!!!!!!!!!!!!!!!!!!')
            else:
                print('your hp afterwards: ' + str(your_hp))
                print('enemy hp afterwards: ' + str(enemy_hp))
                print('You won!!!')
                return
        attack_counter = 2
        while attack_counter == 1 or attack_counter == 2:
            enemy_attack = attack(enemy_stats['mindmg'],
                                  enemy_stats['maxdmg'],
                                  enemy_stats['damage_reduction'],
                                  enemy_stats['crit_chance'],
                                  selected_classes['enemy_class'])
            your_hp -= int(enemy_attack * dmg_scaling)
            if selected_classes['enemy_class_name'] == 'assassin':
                attack_counter -= 1
            elif selected_classes['enemy_class_name'] == 'berserker':
                attack_counter = random.randint(0, 1)
            else:
                attack_counter = 0
        dmg_scaling += 0.2
        if your_hp <= 0:
            n = random.randint(0, 3)
            if selected_classes['your_class_name'] == 'demon hunter' and your_revives == 1 and n == 0:
                your_hp = enemy_stats['hp']
                your_revives = 0
                print('YOU REVIVED!!!!!!!!!!!!!!!!!!!!!!!!!')
            else:
                print('your hp afterwards: ' + str(your_hp))
                print('enemy hp afterwards: ' + str(enemy_hp))
                print('Enemy won :((')
                return
        print('your hp afterwards: ' + str(your_hp))
        print('enemy hp afterwards: ' + str(enemy_hp))
        round += 1


def main():
    selected_classes = class_selection()
    fight(selected_classes)


if __name__ == '__main__':
    main()
