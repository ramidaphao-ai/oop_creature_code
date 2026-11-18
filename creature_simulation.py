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

class FlyingCreature(Creature):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.altitude = 0

    def fly_to(self, new_altitude):
        self.altitude = new_altitude
        print(f"{self.name} flies to altitude {self.altitude} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return
        print(f"{self.name} swoops down from altitude {self.altitude}!")
        print(f"{self.name} performs an aerial attack on {target.name} for {self.attack_power} damage!")
        target.hp = max(0, target.hp - self.attack_power)
        print(f"{target.name} HP is now {target.hp}")


if __name__ == "__main__":
    wolf = Creature("Wolf", 40, 10)
    sheep = Creature("Sheep", 25, 3)
    wolf.attack(sheep)
    print(sheep)
    assert sheep.hp == 15
    assert sheep.is_alive()

    hawk = FlyingCreature("Sky Hawk", 50, 8)
    hawk.fly_to(120)
    dummy = Creature("Practice Dummy", 40, 0)
    hawk.attack(dummy)
    assert hawk.altitude == 120
    assert dummy.hp == 32
