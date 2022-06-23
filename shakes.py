import random


def classes():
    all_classes = {'mage': {'dodge': 0,
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
    return all_classes


def your_stats(your_class):
    stats = {'level': 183,
             'strength': 5000,
             'dexterity': 5000,
             'intelligence': 5000,
             'constitution': 4303,
             'luck': 1929,
             'weapon dmg': 478,
             'weapon min dmg': 468,
             'weapon max dmg': 488,
             'armor': 4383
             }
    if your_class == 'assassin':
        stats.update({'secondary weapon dmg': 478,
                      'secondary weapon min dmg': 468,
                      'secondary weapon max dmg': 488
                      })
    if your_class == 'druid':
        stats.update({'mask': input('Select your druid mask (warrior, scout, none): ')})
    print('\n')
    return stats


def enemy_stats(enemy_class):
    stats = {'level': 183,
             'strength': 5000,
             'dexterity': 5000,
             'intelligence': 5000,
             'constitution': 4303,
             'luck': 1929,
             'weapon dmg': 478,
             'weapon min dmg': 468,
             'weapon max dmg': 488,
             'armor': 4383
             }
    if enemy_class == 'assassin':
        stats.update({'secondary weapon dmg': 478,
                      'secondary weapon min dmg': 468,
                      'secondary weapon max dmg': 488
                      })
    if enemy_class == 'druid':
        stats.update({'mask': input('Select enemy druid mask (warrior, scout, none): ')})
    return stats


def stat_setter(this_class_name, this_class, this_stats, oponent_stats):
    min_dmg = 0
    max_dmg = 0
    second_min_dmg = 0
    second_max_dmg = 0
    mask = 0
    if this_class_name == 'druid':
        mask = this_stats['mask']
        if mask == 'warrior':
            this_class['main stat'] = 'strength'
            this_class['hp counter'] = 5
            placeholder = this_stats['strength']
            this_stats['strength'] = this_stats['intelligence']
            this_stats['intelligence'] = placeholder
        if mask == 'scout':
            this_class['main stat'] = 'dexterity'
            this_class['hp counter'] = 4
            this_class['max reduction'] = 25
            placeholder = this_stats['dexterity']
            this_stats['dexterity'] = this_stats['intelligence']
            this_stats['intelligence'] = placeholder
    hp = this_stats['constitution'] * this_class['hp counter'] * (this_stats['level'] + 1)
    defense = oponent_stats['strength'] / 2
    evasion = oponent_stats['dexterity'] / 2
    resistance = oponent_stats['intelligence'] / 2
    if this_class['main stat'] == 'intelligence':
        min_dmg = this_stats['weapon min dmg'] * ((this_stats['intelligence'] - resistance) / 10 + 1)
        max_dmg = this_stats['weapon max dmg'] * ((this_stats['intelligence'] - resistance) / 10 + 1)
    if this_class['main stat'] == 'strength':
        min_dmg = this_stats['weapon min dmg'] * ((this_stats['strength'] - defense) / 10 + 1)
        max_dmg = this_stats['weapon max dmg'] * ((this_stats['strength'] - defense) / 10 + 1)
    if this_class['main stat'] == 'dexterity':
        min_dmg = this_stats['weapon min dmg'] * ((this_stats['dexterity'] - evasion) / 10 + 1)
        max_dmg = this_stats['weapon max dmg'] * ((this_stats['dexterity'] - evasion) / 10 + 1)
    if this_class_name == 'assassin':
        second_min_dmg = this_stats['secondary weapon min dmg'] * ((this_stats['dexterity'] - resistance) / 10 + 1)
        second_max_dmg = this_stats['secondary weapon max dmg'] * ((this_stats['dexterity'] - resistance) / 10 + 1)
    damage_reduction = this_stats['armor'] / oponent_stats['level']
    if this_class_name == 'battle mage':
        damage_reduction += 40
    if damage_reduction > this_class['max reduction']:
        damage_reduction = this_class['max reduction']
    crit_chance = this_stats['luck'] * 5 / (oponent_stats['level'] * 2)
    if crit_chance > 50:
        crit_chance = 50
    stats = {'hp': hp,
             'min dmg': min_dmg,
             'max dmg': max_dmg,
             'secondary min dmg': second_min_dmg,
             'secondary max dmg': second_max_dmg,
             'damage_reduction': damage_reduction,
             'crit_chance': crit_chance,
             'mask': mask
             }
    return stats


def attack(min_dmg, max_dmg, damage_reduction, crit_chance, this_class_name, oponent_class, your_mask, oponent_mask):
    random_dmg = random.randint(round(min_dmg), round(max_dmg))
    dmg = random_dmg / (100 / damage_reduction)
    if your_mask == 'none':
        dmg = dmg / 3
    crit_range = random.randint(0, 99)
    crit = 0
    if crit_range < crit_chance:
        dmg *= 2
        crit = 1
    if this_class_name != 'mage':
        if oponent_mask == 'warrior':
            oponent_class['dodge'] = 25
        if oponent_mask == 'scout':
            oponent_class['dodge'] = 50
        n = random.randint(0, 99)
        if n < oponent_class['dodge'] and crit == 0:
            return 0
    return round(dmg)


def class_selection(all_classes):
    while 1:
        loop_stopper = 0
        your_class_name = enter_class('your', all_classes)
        your_class = 0
        for i in all_classes:
            if your_class_name == i:
                your_class = all_classes[i]
                loop_stopper += 1
        enemy_class_name = enter_class('enemy', all_classes)
        enemy_class = 0
        for i in all_classes:
            if enemy_class_name == i:
                enemy_class = all_classes[i]
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


def enter_class(who, all_classes):
    print("Enter " + who + " class: ")
    loop_counter = 1
    for i in all_classes:
        print(str(loop_counter) + ') ' + i.capitalize())
        loop_counter += 1
    user_input = input().lower()
    return user_input


def fight(selected_classes):
    your_character_stats = your_stats(selected_classes['your_class_name'])
    enemy_character_stats = enemy_stats(selected_classes['enemy_class_name'])
    your_character = stat_setter(selected_classes['your_class_name'],
                                 selected_classes['your_class'],
                                 your_character_stats,
                                 enemy_character_stats)
    enemy_character = stat_setter(selected_classes['enemy_class_name'],
                                  selected_classes['enemy_class'],
                                  enemy_character_stats,
                                  your_character_stats)
    your_hp = your_character['hp']
    enemy_hp = enemy_character['hp']
    your_revives = 1
    enemy_revives = 1
    round = 1
    dmg_scaling = 1.2
    if selected_classes['your_class_name'] == 'battle mage' and selected_classes['enemy_class']['magic'] != 1:
        enemy_hp -= min(int(your_hp / 3), int(enemy_hp / 3))
        print('FIRE BAAAAAAAALLLLLLLL')
    if selected_classes['enemy_class_name'] == 'battle mage' and selected_classes['your_class']['magic'] != 1:
        your_hp -= min(int(your_hp / 3), int(enemy_hp / 3))
        print('FIRE BAAAAAAAALLLLLLLL')
    while 1:
        print('\n___________Round ' + str(round) + '____________\n')
        print('your hp:' + str(your_hp) + '\n' + 'enemy hp: ' + str(enemy_hp) + '\n')
        attack_counter = 2
        while attack_counter == 1 or attack_counter == 2:
            your_attack = attack(your_character['min dmg'],
                                 your_character['max dmg'],
                                 your_character['damage_reduction'],
                                 your_character['crit_chance'],
                                 selected_classes['your_class_name'],
                                 selected_classes['enemy_class'],
                                 your_character['mask'],
                                 enemy_character['mask'])
            enemy_hp -= int(your_attack * dmg_scaling)
            if selected_classes['your_class_name'] == 'assassin':
                your_attack = attack(your_character['secondary min dmg'],
                                     your_character['secondary max dmg'],
                                     your_character['damage_reduction'],
                                     your_character['crit_chance'],
                                     selected_classes['your_class_name'],
                                     selected_classes['enemy_class'],
                                     your_character['mask'],
                                     enemy_character['mask'])
                enemy_hp -= int(your_attack * dmg_scaling)
                attack_counter -= 0
            elif selected_classes['your_class_name'] == 'berserker':
                attack_counter = random.randint(0, 1)
            else:
                attack_counter = 0
        if selected_classes['enemy_class_name'] == 'demon hunter' and enemy_hp <= 0 and enemy_revives == 1:
            n = random.randint(0, 3)
            if n == 0:
                enemy_hp = enemy_character['hp']
                enemy_revives = 0
        dmg_scaling += 0.2
        if enemy_hp <= 0:
            n = random.randint(0, 3)
            if selected_classes['enemy_class_name'] == 'demon hunter' and enemy_revives == 1 and n == 0:
                enemy_hp = enemy_character['hp']
                enemy_revives = 0
                print('ENEMY REVIVED!!!!!!!!!!!!!!!!!!!!!!!!!')
            else:
                print('your hp afterwards: ' + str(your_hp))
                print('enemy hp afterwards: ' + str(enemy_hp))
                print('You won!!!')
                return
        attack_counter = 2
        while attack_counter == 1 or attack_counter == 2:
            enemy_attack = attack(enemy_character['min dmg'],
                                  enemy_character['max dmg'],
                                  enemy_character['damage_reduction'],
                                  enemy_character['crit_chance'],
                                  selected_classes['enemy_class_name'],
                                  selected_classes['your_class'],
                                  enemy_character['mask'],
                                  your_character['mask'])
            your_hp -= int(enemy_attack * dmg_scaling)
            if selected_classes['enemy_class_name'] == 'assassin':
                enemy_attack = attack(enemy_character['secondary min dmg'],
                                      enemy_character['secondary max dmg'],
                                      enemy_character['damage_reduction'],
                                      enemy_character['crit_chance'],
                                      selected_classes['enemy_class_name'],
                                      selected_classes['your_class'],
                                      enemy_character['mask'],
                                      your_character['mask'])
                your_hp -= int(enemy_attack * dmg_scaling)
                attack_counter = 0
            elif selected_classes['enemy_class_name'] == 'berserker':
                attack_counter = random.randint(0, 1)
            else:
                attack_counter = 0
        dmg_scaling += 0.2
        if your_hp <= 0:
            n = random.randint(0, 3)
            if selected_classes['your_class_name'] == 'demon hunter' and your_revives == 1 and n == 0:
                your_hp = enemy_character['hp']
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
    all_classes = classes()
    selected_classes = class_selection(all_classes)
    fight(selected_classes)


if __name__ == '__main__':
    main()
