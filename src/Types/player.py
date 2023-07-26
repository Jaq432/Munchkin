import time

import Types.item as item
import Types.weapon as weapon


class Player:
    def __init__(
        self,
        personName: str,
        personLevel: int,
        personRace: list,
        personPersonalClass: list,
        personWeapon: list,
        personItems: list,
        personAttack: int,
        personCardsInHand: list,
        personalGold: int,
    ):
        # Define all of the default attributes of the player
        self.personalName = personName
        self.personalLevel = personLevel
        self.personalRace = personRace
        self.personalClass = personPersonalClass
        self.personalWeapon = personWeapon
        self.personalItems = personItems
        self.attack = personAttack
        self.cardsInHand = personCardsInHand
        self.personalGold = personalGold

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
            print("Gold: " + str(personalGold))

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
        if self.personalItems != []:
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
        
    def getGold(self):
        return self.personalGold


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
            self.personalWeapon = [data]
        elif len(self.getWeapons()) != 1:
            self.personalWeapon = [data]
        else:
            print("Prompt to remove the weapon.")

    def setItems(self, data):
        self.personalItems = [data]

    def addCardToHand(self, data):
        self.cardsInHand.append(data)

    def setGold(self, data):
        self.personalGold = data


    # Deleters
    def deleteEquippedItem(self, data):
        self.personalItems.remove(data)

    def deleteEquippedWeapon(self, data):
        self.personalWeapon.remove(data)

    def deleteItemInHand(self, data):
        self.cardsInHand.remove(data)


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
                print("You already have something equipped in the weapon slot.")
                time.sleep(1)
                print("Please unequip the item in that slot before proceeding.")

        # Item
        elif isinstance(data, item.Item):
            equipmentSlotToEquip = data.getType()
            for equipment in self.getItems():
                if equipment.getType() == equipmentSlotToEquip:
                    print("You already have something equipped in the " + str(equipmentSlotToEquip) + " slot.")
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


    # Sell Cards
    def sellEquippedCard(self, data):
        equippedItems = self.getWeapons() + self.getItems()
        currentGold = self.getGold()
        for card in equippedItems:
            print("Checking choice vs equipped cards: " + str(data.getName()) + " " + str(card.getName()))
            if card.getName() == data.getName():
                print("Selling the card that's equipped.")
                currentGold += card.getCost()
                self.setGold(currentGold)
                # Delete the item from our equipment
                if isinstance(data, item.Item):
                    self.deleteEquippedItem(data)
                    return
                if isinstance(data, weapon.Weapon):
                    self.deleteEquippedWeapon(data)
                    return

    def sellHandCard(self, data):
        handItems = self.getCardsInHand()
        currentGold = self.getGold()
        for card in handItems: 
            print("Checking choice vs hand cards: " + str(data.getName()) + " " + str(card.getName()))
            if card.getName() == data.getName():
                print("Selling the card from your hand.")
                currentGold += card.getCost()
                self.setGold(currentGold)
                # Delete the item from our hand
                self.deleteItemInHand(data)
                return


