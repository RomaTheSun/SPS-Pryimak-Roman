class Army:
    army_type='Basic'

    swordsman_name = None
    lancer_name = None
    archer_name = None

    def train_swordsman(self, name):
       return Swordsman(name, self.army_type, self.swordsman_name)
    def train_lancer(self, name):
        return Lancer(name, self.army_type, self.lancer_name)
    def train_archer(self, name):
        return Archer(name, self.army_type, self.archer_name)

class Soldier:
    def __init__(self, name, army_type, spec, soldier_type):
        self.name = name
        self.army_type = army_type
        self.spec = spec
        self.soldier_type = soldier_type

    def introduce(self):
        return f"{self.soldier_type} {self.name}, {self.army_type} {self.spec}"

class Swordsman(Soldier):
    def __init__(self, name, army_type, soldier_type):
        super().__init__(name, army_type, 'swordsman', soldier_type )

class Lancer(Soldier):
    def __init__(self, name, army_type, soldier_type):
        super().__init__(name, army_type, 'lancer', soldier_type)

class Archer(Soldier):
    def __init__(self, name, army_type, soldier_type):
        super().__init__(name, army_type, 'archer', soldier_type)

class AsianArmy(Army):
    army_type = "Asian"
    swordsman_name = "Samurai"
    lancer_name = "Ronin"
    archer_name = "Shinobi"

class EuropeanArmy(Army):
    army_type = "European"
    swordsman_name = "Knight"
    lancer_name = "Raubritter"
    archer_name = "Ranger"

if __name__ == "__main__":
    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    assert soldier_1.introduce() == "Knight Jaks, European swordsman"
    assert soldier_2.introduce() == "Raubritter Harold, European lancer"
    assert soldier_3.introduce() == "Ranger Robin, European archer"

    assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"

    print("Coding complete? Let's try tests!")
