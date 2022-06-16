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
    hp = 15
    dmg = 5
	
class EnemyStats:
	hp = 20
	dmg = 10


def selectedClass(answer):
    for i in Class.allClasses:
        if i == answer:
            return answer

def answer():
    userinput = input("Enter your class: " + '\n').lower()
    loopCounter = 1
    for i in Class.allClasses:
        print(str(loopCounter) + ') ' + i.capitalize())
        loopCounter += 1
    return userinput

answer = answer()
selectedClass = selectedClass(answer)
print(selectedClass)

def fight():
	yourhp = YourStats.hp
	enemyhp = EnemyStats.hp
	round = 1
	while yourhp > 0 and enemyhp > 0:
		print('Round ' + str(round) + '\n')
		print(str(yourhp) + '\n' + str(enemyhp) + '\n')
		enemyhp -= YourStats.dmg
		yourhp -= EnemyStats.dmg
		print('your hp: ' + str(yourhp) + '\n')
		print('enemy hp: ' + str(enemyhp) + '\n')
		round += 1
	if yourhp > enemyhp:
		print('You won!!!')
	else: 
		print('Enemy Won :((')

fight()