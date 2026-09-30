class Plants:

    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, zombie):
        if self.health > 0:
            print (f"{self.name} is being attacked by {self.damage}")
            zombie.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            print ("Oh no!! Patay kana!")

class Zombie:
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def move(self):
        if self.distance > 0:
            self.distance -= 1
            print(f"{self.name} Current Distance: {self.distance}")

    def attack(self, plant):
        print(f"--> {self.name} attacks {plant.name} for {self.damage} damage!")
        plant.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
            print(f"{self.name} took {amount} damage! Current HP: {self.health}")

plant1 = Plants("Pea", 20, 15)
plant2 = Plants("sunflower", 20, 10)
zombie = Zombie("Zombie1", 80, 15, 2)

turn = 1
while True:
    print(f"\n--- Turn {turn} ---")

    if plant1.health > 0:
        plant1.attack(zombie)
        if zombie.health == 0:
            print("\nPlants win!")
            break

    if plant2.health > 0:
        plant2.attack(zombie)
        if zombie.health == 0:
            print("\nPlants win!")
            break

    if zombie.distance > 0:
        zombie.move()
    elif plant1.health > 0:
        zombie.attack(plant1)
    elif plant2.health > 0:
        zombie.attack(plant2)

    if plant1.health == 0 and plant2.health == 0:
        print("\nZombie wins!")
        break

    turn = turn + 1