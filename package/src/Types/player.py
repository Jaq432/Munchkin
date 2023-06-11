class Player:
    def __init__(self,
        name,
        level,
        race,
        personalClass,
        weapon,
        items,
        attack,
        cardsInHand
    ):
        # Define all of the default attributes of the player
        self.personalName = name
        self.personalLevel = level
        self.personalRace = race
        self.personalClass = personalClass
        self.personalWeapon = weapon
        self.personalItems = items
        self.attack = attack
        self.cardsInHand = cardsInHand

        # This is here for testing
        if False:
            print("Initialized character with the following attributes: ")
            print("Name: " + str(name))
            print("Level: " + str(level))
            print("Race: " + str(race))
            print("Class: " + str(personalClass))
            print("Weapons: " + str(weapon))
            print("Items: " + str(items))
            print("Attack: " + str(attack))
            print("Cards in hand: " + str(cardsInHand))

    # Getters
    def getName(self):
        return self.personalName

    def getLevel(self):
        return self.personalLevel

    def getRace(self):
        return self.personalRace

    def getClass(self):
        return self.personalClass

    def getWeapons(self):
        return self.personalWeapon
    
    def getItems(self):
        return self.personalItems

    def getAttack(self):
        attackSum = self.attack

        # We need to account for dual wielding
        if self.personalWeapon != None:
            for weapon in self.personalWeapon:
                attackSum += weapon.getAttack()

        if self.personalItems != None:
            for item in self.personalItems:
                attackSum += item.getAttack()

        return attackSum

    def getCardsInHand(self):
        if self.cardsInHand != None:
            return self.cardsInHand
        else:
            return None

    # Setters
    def setName(self, data):
        self.personalName = str(data)

    def setLevel(self, data):
        # This does relative level adjustments based on the characteristics of the monster
        self.personalLevel += data

    def setRace(self, data):
        # The game might be able to have dual-race
        self.personalRace = data

    def setClass(self, data):
        if self.personalClass is "barbarian" and (self.getWeaponCount < 2):
            print("Prompt to remove one of the weapons.")
        # The game might be able to have dual-class
        self.personalClass = data

    def setWeapon(self, data):
        # The game has regulations around weapon equipment
        if (self.personalClass == "barbarian") and (self.getWeaponCount < 2):
            self.personalWeapon = data
        elif self.getWeaponCount != 1:
            self.personalWeapon = data
        else:
            print("Prompt to remove the weapon.")

    def setItems(self, data):
        self.personalItems.append(data)

    def setCardsInHand(self, data):
        self.cardsInHand.append(data)

    # Deleters
    def deleteItem(self, data):
        self.personalItems.remove(data)

    def deleteWeapon(self, data):
        self.personalWeapon.remove(data)

    # Equip Card
    def equipCard(self, data):
        # the format is <class 'datatype'>
        if type(data) == "<class 'Weapon'>":
            self.personalWeapon.append(data)
        elif type(data) == "<class 'Item'>":
            self.personalItems.append(data)
        else:
            print("Something went wrong with equippng the card.")

    # Unequip Card
    def unequipCard(self, data):
        # the format is <class 'int'>
        if type(data) == "<class 'Weapon'>":
            self.personalWeapon.remove(data)
        elif type(data) == "<class 'Item'>":
            self.personalItems.remove(data)
        else:
            print("Something went wrong with unequippng the card.")
