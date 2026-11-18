# Creature Battle Project (OOP + Git Branching Practice)

This project is designed to help me learn **object-oriented programming** in Python — especially **inheritance** — while also practicing key **Git concepts** like branching, merging, conflict resolution, and version history.

I will begin with a base class (`Creature`) and create additional subclasses on separate Git branches to simulate a real development workflow.

---

## Learning Objectives

### Python / OOP
- Understand and implement **classes**
- Use **inheritance** to extend behaviors
- Override and extend methods (e.g., `attack()`)
- Practice writing simple test code in `main`

### Git / Version Control
- Create and switch branches
- Merge branches into `main`
- Resolve merge conflicts
- View commit history (`git log --graph --all`)

---

## Project Structure

```text
oop_creature_code/
├── creature_simulation.py
└── README.md
```

## Creature Classes

- Creature: Base class with HP and attack power.
- FlyingCreature: Can fly and attack from above.
- SwimmingCreature: Can dive and attack underwater.
- FireCreature: Can emit fire and perform fire attacks.

## How to Run

1. Install Python 3.
2. Open a terminal in the project directory.
3. Run:

```bash
python3 creature_simulation.py
```

## Testing

The program contains tests for the base class and all subclasses.

Run:

```bash
python3 creature_simulation.py
```

The tests use assertions to verify creature behavior.

## Git History

View the branches and commit history with:

```bash
git log --all --graph --oneline
```
