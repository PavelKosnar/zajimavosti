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
    hp = 0
    dmg = 0

def selectedClass(answer):
    for i in Class.allClasses:
        if i == answer:
            return answer

def answer():
    answer = input("Enter your class: ").lower()
    loopCounter = 1
    for i in Class.allClasses:
        print(str(loopCounter) + ') ' + i.capitalize())
        loopCounter += 1
    return answer

answer = answer()
selectedClass = selectedClass(answer)
print(selectedClass)
while selectedClass == None:
    answer = answer()
    selectedClass = selectedClass()
    print(selectedClass)