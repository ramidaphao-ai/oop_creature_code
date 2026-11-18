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


class SwimmingCreature(Creature):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.depth = 0

    def dive_to(self, new_depth):
        self.depth = new_depth
        print(f"{self.name} dives to depth {self.depth} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return
        print(f"{self.name} attacks from underwater at depth {self.depth}!")
        print(f"It splashes {target.name} for {self.attack_power} damage!")
        target.hp = max(0, target.hp - self.attack_power)
        print(f"{target.name} HP is now {target.hp}")


class FireCreature(Creature):
    def __init__(self, name, hp, attack_power, fire_level=0):
        super().__init__(name, hp, attack_power)
        self.fire_level = max(0, min(100, fire_level))

    def emit_fire(self, new_fire_level):
        self.fire_level = max(0, min(100, new_fire_level))
        print(f"{self.name} emits fire at level {self.fire_level}!")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return
        damage = self.attack_power + self.fire_level // 10
        print(f"{self.name} attacks {target.name} with fire for {damage} damage!")
        target.hp = max(0, target.hp - damage)
        print(f"{target.name} HP is now {target.hp}")


if __name__ == "__main__":
    print("=== Creature Class Tests ===\n")

    # Test 1: Initialization
    goblin = Creature("Goblin", 30, 5)
    print("Test 1: Initialization")
    print(goblin)
    print()

    # Test 2: Basic attack
    wolf = Creature("Wolf", 40, 10)
    sheep = Creature("Sheep", 25, 3)
    print("Test 2: Wolf attacks Sheep")
    wolf.attack(sheep)
    print(f"Sheep HP should now be 15 → Actual: {sheep.hp}")
    print()

    # Test 3: HP does not go below zero
    dragon = Creature("Dragonling", 50, 100)
    mouse = Creature("Mouse", 20, 1)
    print("Test 3: Dragonling overkills Mouse")
    dragon.attack(mouse)
    print(f"Mouse HP should now be 0 → Actual: {mouse.hp}")
    print()

    # Test 4: is_alive()
    slime = Creature("Slime", 10, 2)
    print("Test 4: Slime alive?")
    print("Slime should be alive →", slime.is_alive())
    slime.hp = 0
    print("Slime should NOT be alive →", slime.is_alive())
    print()

    # Test 5: Dead creature cannot attack
    ghost = Creature("Ghost", 0, 10)
    knight = Creature("Knight", 50, 7)
    print("Test 5: Ghost tries to attack Knight")
    ghost.attack(knight)
    print(f"Knight HP should remain 50 → Actual: {knight.hp}")
    print()

    # Test 6: Multiple attacks
    print("Test 6: Goblin attacks Slime twice")
    slime.hp = 10
    goblin.attack(slime)
    goblin.attack(slime)
    print(f"Slime should be at HP 0 → Actual: {slime.hp}")
    print()

    print("=== Tests Completed ===")

    print("\n=== FlyingCreature Tests ===")
    hawk = FlyingCreature("Sky Hawk", 50, 8)
    hawk.fly_to(120)
    dummy = Creature("Practice Dummy", 40, 0)
    hawk.attack(dummy)
    assert hawk.altitude == 120
    assert dummy.hp == 32

    print("\n=== SwimmingCreature Tests ===")
    serpent = SwimmingCreature("Aqua Serpent", 60, 7)
    serpent.dive_to(30)
    dummy = Creature("Practice Dummy", 40, 0)
    serpent.attack(dummy)
    assert serpent.depth == 30
    assert dummy.hp == 33

    print("\n=== FireCreature Tests ===")
    phoenix = FireCreature("Phoenix", 80, 15)
    phoenix.emit_fire(50)
    enemy = Creature("Enemy", 100, 5)
    phoenix.attack(enemy)
    assert phoenix.fire_level == 50
    assert enemy.hp == 80
    phoenix.emit_fire(150)
    assert phoenix.fire_level == 100

    print("\nAll tests completed successfully!")
