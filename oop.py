class Monster:
    """def __len__(self):
        return self.health
        # CALL:  len(Monster)

    def __abs__(self):
        return self.energy
        # CALL:  abs(Monster)

    def __call__(self, *args, **kwargs):
        print('Called')
        # CALL:  Monster()()

    def __add__(self, other):
        return self.health + other
        # CALL:  Monster + n

    def __str__(self):
        return f'A monster with {self.health} HP and {self.energy} energy'
        # CALL:  print(Monster) or str(Monster)"""

    def __init__(self, func, health, energy, **kwargs):
        self.func = func
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)

        # private attribute:  self._id = 5

    def update_energy(self, amount):
        self.energy += amount

    def get_damage(self, amount):
        self.health -= amount

    def attack(self, amount):
        print(f'Monster attacked, {amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print(f'Monster moved at a speed of {speed}')


class Fish:
    def __init__(self, speed, has_scales, **kwargs):
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)

    def swim(self):
        print(f'Fish swims at a speed of {self.speed}')


class Shark(Monster, Fish):
    def __init__(self, bite_strength, health, energy, speed, has_scales):
        super().__init__(func=Attacks().kick, health=health, energy=energy, speed=speed, has_scales=has_scales)
        self.bite_strength = bite_strength

    def bite(self):
        print('bite')

    def move(self, **kwargs):
        print(f'Shark moved at a speed of {self.speed}')


class Scorpion(Monster):
    def __init__(self, health, energy, poison_damage):
        super().__init__(Attacks().kick, health, energy)
        self.poison_damage = poison_damage

    def attack(self, **kwargs):
        print(f'Scorpion attacked, {self.poison_damage} poison damage was dealt')
        self.energy -= 20


class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

    def attack(self):
        self.monster.get_damage(self.damage)


class Attacks:
    def bite(self):
        print('bite')

    def strike(self):
        print('strike')

    def slash(self):
        print('slash')

    def kick(self):
        print('kick')


def update_health(amount):
    monster1.health += amount


# monster
monster1 = Monster(Attacks().kick, health=100, energy=50)
monster1.func()
update_health(amount=20)
monster1.update_energy(amount=20)
print(f'Monster health: {monster1.health}')
print(f'Monster energy: {monster1.energy}')

# shark
shark = Shark(bite_strength=50, health=100, energy=50, speed=120, has_scales=False)
print(f'Shark health: {shark.health}')
print(f'Shark energy: {shark.energy}')
print(f'Shark speed: {shark.speed}')

# scorpion
scorpion = Scorpion(health=100, energy=50, poison_damage=20)
scorpion.attack()

# hero
hero = Hero(damage=15, monster=monster1)
hero.attack()
print(f'Hero damage: {hero.damage}')
print(f'Monster health after attack: {monster1.health}')

# hasattr -> check for object attribute
if hasattr(monster1, 'health'):
    print(f'The monster has {monster1.health} health')

# setattr -> set an attribute for an object
new_attributes = (['weapon', 'Axe'], ['armor', 'Shield'], ['potion', 'mana'])
for attr, value in new_attributes:
    setattr(monster1, attr, value)
print(vars(monster1))

# doc -> read comments
print(monster1.__doc__)

# help -> info about object
help(monster1)
