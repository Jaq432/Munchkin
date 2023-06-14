import time

import Types.item as item
import Types.weapon as weapon

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
        if self.personalItems != None:
            return self.personalItems
        else:
            return []

    def getAttack(self):
        attackSum = 0

        # We need to account for dual wielding
        if self.personalWeapon != None:
            for weapon in self.personalWeapon:
                attackSum += weapon.getAttack()

        if self.personalItems != None:
            for item in self.personalItems:
                attackSum += item.getAttack()

        attackSum += self.personalLevel

        return attackSum

    def getCardsInHand(self):
        if self.cardsInHand != None:
            return self.cardsInHand
        else:
            return []

    # Setters
    def setName(self, data):
        self.personalName = str(data)

    def setLevel(self, data):
        # based on the characteristics of the monster
        self.personalLevel = data
        # Make sure we can't be below level 1
        if self.personalLevel < 1:
            self.personalLevel = 1

    def setRace(self, data):
        # The game might be able to have dual-race
        self.personalRace = data

    def setClass(self, data):
        if self.personalClass == "barbarian" and (len(self.getWeapons()) < 2):
            print("Prompt to remove one of the weapons.")
        # The game might be able to have dual-class
        self.personalClass = data

    def setWeapon(self, data):
        # The game has regulations around weapon equipment
        if (self.personalClass == "barbarian") and (len(self.getWeapons()) < 2):
            self.personalWeapon = data
        elif len(self.getWeapons()) != 1:
            self.personalWeapon = data
        else:
            print("Prompt to remove the weapon.")

    def setItems(self, data):
        self.personalItems = data

    def setCardsInHand(self, data):
        self.cardsInHand.append(data)

    # Deleters
    def deleteItem(self, data):
        self.personalItems.remove(data)

    def deleteWeapon(self, data):
        self.personalWeapon.remove(data)

    # Equip Card
    def equipCard(self, data):
        # Weapon
        if isinstance(data, weapon.Weapon):
            # Is empty
            if len(self.getWeapons()) == 0:
                # Equip
                self.personalWeapon.append(data)
                # Remove from hand
                self.cardsInHand.remove(data)
            elif len(self.getWeapons()) == 1 and self.personalClass == "barbarian":
                # Equip
                self.personalWeapon.append(data)
                # Remove from hand
                self.cardsInHand.remove(data)
            else:
                print("Prompt to unequip a weapon.")

        # Item
        elif isinstance(data, item.Item):
            equipmentSlotToEquip = data.getType()
            for equipment in self.getItems():
                if equipment.getType() == equipmentSlotToEquip:
                    print("You already have something equipped in that slot.")
                    time.sleep(1)
                    print("Please unequip the item in that slot before proceeding.")
                    return
            self.personalItems.append(data)
            self.cardsInHand.remove(data)

        else:
            print("Something went wrong with equippng the card.")

    # Unequip Card
    def unequipCard(self, data):
        # the format is <class 'int'>
        if isinstance(data, weapon.Weapon):
            self.personalWeapon.remove(data)
        elif isinstance(data, item.Item):
            self.personalItems.remove(data)
        else:
            print("Something went wrong with unequippng the card.")
