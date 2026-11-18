class Creature:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.hp = max(0, target.hp - self.attack_power)

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} (HP: {self.hp})"

if __name__ == "__main__":
    wolf = Creature("Wolf", 40, 10)
    sheep = Creature("Sheep", 25, 3)
    wolf.attack(sheep)
    print(sheep)
    assert sheep.hp == 15
    assert sheep.is_alive()
