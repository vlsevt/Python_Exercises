"""Adventurers and Monsters in the World."""

from copy import copy
from enum import Enum


class ClassType(Enum):
    """Enum for class types, default class is Fighter."""

    Fighter = 'Fighter'
    Druid = 'Druid'
    Wizard = 'Wizard'
    Paladin = 'Paladin'

    @classmethod
    def _missing_(cls, key):
        return cls.Fighter


class Adventurer:
    """Adventurer class."""

    def __init__(self, name: str, class_type: str = 'Fighter', power: int = 0, experience: int = 0):
        """Adventurer initialization."""
        self.name = name
        self._class_type = ClassType(class_type)
        self.power = power if power <= 99 else 10
        self.experience = experience if experience > 0 else 0

    @property
    def class_type(self):
        """Return string value of the class type enum."""
        return self._class_type.value

    def __repr__(self):
        """Return string representation of the adventurer."""
        return f'{self.name}, the {self.class_type}, Power: {self.power}, Experience: {self.experience}.'

    def add_power(self, power: int):
        """Add power to the adventurer."""
        self.power += power

    def add_experience(self, exp: int):
        """
        Add experience to the adventurer.

        Only non-negative values are valid. When there becomes more than 99 experience, it converts to the power in 10:1\
        ratio (rounded down) and resets.
        """
        if exp < 0:
            return
        new_experience = self.experience + exp
        if new_experience > 99:
            self.power += new_experience // 10
            self.experience = 0
        else:
            self.experience = new_experience


class Monster:
    """Monster class."""

    def __init__(self, name: str, type: str, power: int):
        """Monster initialization."""
        self.type = type
        self._name = name
        self.power = power

    @property
    def name(self):
        """Name of the monster, if type of the monster is Zombie, then it's a 'Undead {name}'."""
        return self._name if self.type != 'Zombie' else f'Undead {self._name}'

    def __repr__(self):
        """Return string representation of the monster."""
        return f"{self.name} of type {self.type}, Power: {self.power}."


class World:
    """World class."""

    def __init__(self, master: str):
        """World initialization."""
        self._master = master
        self._adventurer_list: list[Adventurer] = list()
        self._active_adventurer_list: list[Adventurer] = list()
        self._monster_list: list[Monster] = list()
        self._graveyard: list[Adventurer | Monster] = list()
        self._dead_active = False

    def remove_character(self, name: str):
        """Remove adventurer, monster, or dead by name."""
        adventurer_index = next(
            (i for i, adventurer in enumerate(self._adventurer_list) if adventurer.name == name), None
        )
        if adventurer_index is not None:
            self._adventurer_list.pop(adventurer_index)
            return

        monster_index = next(
            (i for i, monster in enumerate(self._monster_list) if monster.name == name), None
        )
        if monster_index is not None:
            self._monster_list.pop(monster_index)
            return

        graveyard_index = next(
            (i for i, dead in enumerate(self._graveyard) if dead.name == name), None
        )
        if graveyard_index is not None:
            self._graveyard.pop(graveyard_index)

    def necromancers_active(self, status: bool):
        """Change status of the dead."""
        self._dead_active = status

    def revive_graveyard(self):
        """
        Revive graveyard if dead are active.

        Corpses become monsters, previously monster return the same but as Zombies, and adventurers also become zombies,
        but of their previous class.
        """
        if not self._dead_active:
            return

        for corpse in self._graveyard:
            if isinstance(corpse, Monster):
                self._monster_list.append(Monster(corpse.name, 'Zombie', corpse.power))
            elif isinstance(corpse, Adventurer):
                self._monster_list.append(Monster(f'Undead {corpse.name}', f'Zombie {corpse.class_type}', corpse.power))
        self._graveyard.clear()
        self._dead_active = False

    def get_python_master(self):
        """Get name of the python master."""
        return self._master

    def get_adventurer_list(self):
        """Get copy of the adventurer list."""
        return copy(self._adventurer_list)

    def get_active_adventurers(self):
        """Get copy of the active adventurer list."""
        return copy(self._active_adventurer_list)

    def add_strongest_adventurer(self, class_type: str):
        strongest_adventurer = max(
            (adventurer for adventurer in self._adventurer_list if adventurer.class_type == class_type),
            key=lambda adventurer: adventurer.power
        )

    def get_monster_list(self):
        """Get copy of the monster list."""
        return copy(self._monster_list)

    def add_adventurer(self, adventurer: Adventurer):
        """Add adventurer to the list if it's of Adventurer class."""
        if isinstance(adventurer, Adventurer):
            self._adventurer_list.append(adventurer)

    def add_monster(self, monster: Monster):
        """Add monster to the list if it's of Monster class."""
        if isinstance(monster, Monster):
            self._monster_list.append(monster)

    def get_graveyard(self):
        """Get graveyard list."""
        return self._graveyard


if __name__ == "__main__":
    print("Kord oli maailm.")
    world = World("Sõber")
    print(world.get_python_master())  # -> "Sõber"
    print(world.get_graveyard())  # -> []
    print()
    print("Tutvustame tegelasi.")
    hero = Adventurer("Sander", "Paladin", 50)
    friend = Adventurer("Peep", "Druid", 25)
    another_friend = Adventurer("Toots", "Wizard", 40)
    annoying_friend = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)
    print(hero)  # -> "Sander, the Paladin, Power: 50, Experience: 0."
    # Ei, tüütu sõber, sa ei saa olla tulevikurändaja ja ninja, nüüd sa pead fighter olema.
    # Ei maksa liiga tugevaks ka ennast alguses teha!
    print(annoying_friend)  # -> "XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 10, Experience: 0."
    print(friend)  # -> "Peep, the Druid, Power: 25, Experience: 0."
    print(another_friend)  # -> "Toots, the Wizard, Power: 40, Experience: 0."
    print()

    print("Peep, sa tundud kuidagi nõrk, ma lisasin sulle natukene tugevust.")
    friend.add_power(20)
    print(friend)  # -> "Peep, the Druid, Power: 45, Experience: 0."
    print()

    world.add_adventurer(hero)
    world.add_adventurer(friend)
    world.add_adventurer(another_friend)
    print(world.get_adventurer_list())  # -> Sander, Peep ja Toots

    world.add_monster(annoying_friend)
    # Ei, tüütu sõber, sa ei saa olla vaenlane.
    print(world.get_monster_list())  # -> []
    world.add_adventurer(annoying_friend)
    print()

    print("Oodake veidikene, ma tekitan natukene kolle.")
    zombie = Monster("Rat", "Zombie", 10)
    goblin_spear = Monster("Goblin Spearman", "Goblin", 10)
    goblin_archer = Monster("Goblin Archer", "Goblin", 5)
    big_ogre = Monster("Big Ogre", "Ogre", 120)
    gargantuan_badger = Monster("Massive Badger", "Animal", 1590)

    print(big_ogre)  # -> "Big Ogre of type Ogre, Power: 120."
    print(zombie)  # -> "Undead Rat of type Zombie, Power: 10."

    world.add_monster(goblin_spear)

    print()
    print("Mängime esimese seikluse läbi!")
    world.add_strongest_adventurer("Druid")
    world.add_strongest_monster()
    print(world.get_active_adventurers())  # -> Peep
    print(world.get_active_monsters())  # -> [Goblin Spearman of type Goblin, Power: 10.]
    print()

    world.go_adventure(True)

    world.add_strongest_adventurer("Druid")
    print(world.get_active_adventurers())  # -> [Peep, the Druid, Power: 45, Experience: 20.]
    print("Surnuaias peaks üks goblin olema.")
    print(world.get_graveyard())  # ->[Goblin Spearman of type Goblin, Power: 10.]
    print()

    world.add_monster(gargantuan_badger)
    world.add_strongest_monster()

    world.go_adventure(True)
    # Druid on loomade sõber ja ajab massiivse mägra ära.
    print(world.get_adventurer_list())  # -> Kõik 4 mängijat.
    print(world.get_monster_list())  # -> [Massive Badger of type Animal, Power: 1590.]

    world.remove_character("Massive Badger")
    print(world.get_monster_list())  # -> []
    print()

    print("Su sõber ütleb: \"Kui kõik need testid andsid sinu koodiga sama tulemuse "
          "mille ma siin ette kirjutasin, peaks kõik okei olema, proovi testerisse pushida! \" ")
