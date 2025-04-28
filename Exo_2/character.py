import logging
import random

log = logging.getLogger(__name__)


class CharacterError(Exception):
    """Base class for Character error"""


class Character:
    """Class defining the structure of a basic character of a fight"""
    DEFAULT_LIFE = 100.0
    DEFAULT_ATTACK = 20.0
    DEFAULT_DEFENSE = 0.1
    def __init__(self, name: str):
        self._name = name
        self._life = self.DEFAULT_LIFE
        self._attack = self.DEFAULT_ATTACK
        self._defense = self.DEFAULT_DEFENSE

    def take_damages(self,damage_value: float):
        self._life = round(self._life - damage_value * (1.0 - self._defense), 2)
        if self._life < 0:
            self._life = 0

    def attack(self,target: "Character"):
        target.take_damages(self._attack)

    def __str__(self) -> str:
        return f"{self.name} <{self._life}>"


    def __repr__(self) -> str:
        return f"{self.name} <{self._life}>"
    @property
    def name(self):
        """The name property of a specific character."""
        return self._name
    @property
    def is_dead(self):
        """The property to check if the character is still alive."""
        return self._life == 0


class Weapon:
    """Class for weapon we can add to warrios"""
    DEFAULT_ATTACK = 1.0
    def __init__(self, name: str, attack: float):
        self._name = name
        self._attack = attack

    @classmethod
    def default(cls):
        """Default weapon constructor"""
        return Weapon("Wood stick",cls.DEFAULT_ATTACK)
    
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
    """Class defining a warrior who always got a weapon"""
    def __init__(self, name: str, weapon=Weapon.default()):
        super().__init__(name)
        self.weapon = weapon
        self._life = self.DEFAULT_LIFE * 1.5
        self._defense = self.DEFAULT_DEFENSE * 1.2

    @property
    def is_raging(self):
        return self._life < (self.DEFAULT_LIFE * 1.5 * 0.2)
    
    def attack(self,target: Character):
        damage = self._attack + self.weapon.attack
        if self.is_raging:
            damage *= 1.2
        target.take_damages(damage)
    


class Magician(Character):
    """Class defining a magician"""
    def __init__(self, name: str):
        super().__init__(name)
        self._life = self.DEFAULT_LIFE * 0.8
        self._attack = self.DEFAULT_ATTACK * 2
    @staticmethod
    def _activate_magical_shield() -> bool:
        values = [True, False, False]
        return random.choice(values)
    
    def take_damages(self,damage_value: float):
        if self._activate_magical_shield():
            pass
        else:
            self._life = round(self._life - damage_value * (1.0 - self._defense),2)
            if self._life < 0:
                self._life = 0
