import logging

log = logging.getLogger(__name__)


class CharacterError(Exception):
    """Base class for Character error"""


class Character:
    """To implement"""
    def __init__(self, name: str):
        self._name = name
        self._life = 100.0
        self._attack = 20.0
        self._defense = 0.1

    def take_damages(self,damage_value: float):
        self._life -= damage_value * (1.0 - self._defense)

    def attack(self,target: "Character"):
        target.take_damages(self._attack)

    def __str__(self) -> str:
        return f"{self.name} <{self._life}>"


    def __repr__(self) -> str:
        return f"{self.name} <{self._life}>"
    @property
    def name(self):
        """The name property."""
        return self._name
    @property
    def is_dead(self):
        """The property to check if the character is still aliuve."""
        return self._life == 0


class Weapon:
    """To implement"""
    def __init__(self, name: str, attack: float):
        self._name = name
        self._attack = attack

    @classmethod
    def default(cls):
        return Weapon("Wood stick", 1.0)
    
    @property
    def attack(self):
        return self._attack

        
    def __str__(self) -> str:
        return f"{self._name} <{self._attack}>"


    def __repr__(self) -> str:
        return f"{self._name} <{self._attack}>"
    
    @property
    def name(self):
        """The name property."""
        return self._name


class Warrior(Character):
    """To implement"""
    def __init__(self, name: str, weapon=Weapon.default()):
        super().__init__(name)
        self.weapon = weapon
        self._life = 150.0
        self._defense = 0.12

    @property
    def is_raging(self):
        return self._life < 150 * 0.2
    
    def attack(self,target: Character):
        damage = self._attack + self.weapon.attack
        if self.is_raging:
            damage *= 1.2
        target.take_damages(damage)
    


class Magician:
    """To implement"""


def main():
    """Test your code here"""
    basic_warrior = Warrior("Test")
    print(basic_warrior.name)

if __name__ == "__main__":
    main()
