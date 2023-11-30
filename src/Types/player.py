import time

import Types.item as item
import Types.weapon as weapon
import Types.classes as classes


class Player:
    def __init__(
        self,
        personName: str,
        personLevel: int,
        personRace: list,
        personClass: list,
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
        self.personalClass = personClass
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
    def getName(self) -> str:
        return self.personalName

    def getLevel(self) -> int:
        return self.personalLevel

    def getRace(self) -> list:
        return self.personalRace

    def getClass(self) -> list:
        return self.personalClass

    def getWeapons(self) -> list:
        return self.personalWeapon
    
    def getItems(self) -> list:
        if self.personalItems != []:
            return self.personalItems
        else:
            return []

    def getAttack(self) -> int:
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

    def getCardsInHand(self) -> list:
        if self.cardsInHand != None:
            return self.cardsInHand
        else:
            return []
        
    def getGold(self) -> int:
        return self.personalGold


    # Setters
    def setName(self, data) -> None:
        self.personalName = str(data)

    def setLevel(self, data) -> None:
        # based on the characteristics of the monster
        self.personalLevel = data
        # Make sure we can't be below level 1
        if self.personalLevel < 1:
            self.personalLevel = 1

    def setRace(self, data) -> None:
        # The game might be able to have dual-race
        self.personalRace = data

    def setClass(self, data) -> None:
        self.personalClass = [data]

    def setWeapon(self, data) -> None:
        self.personalWeapon = [data]

    def setItems(self, data) -> None:
        self.personalItems = [data]

    def addCardToHand(self, data) -> None:
        self.cardsInHand.append(data)

    def setGold(self, data) -> None:
        self.personalGold = data


    # Deleters
    def deleteEquippedItem(self, data) -> None:
        self.personalItems.remove(data)

    def deleteEquippedWeapon(self, data) -> None:
        self.personalWeapon.remove(data)

    def deleteEquippedClass(self, data) -> None:
        self.personalClass.remove(data)

    def deleteItemInHand(self, data) -> None:
        self.cardsInHand.remove(data)


    # Equip Card
    def equipCard(self, data) -> None:
        # Weapon
        if isinstance(data, weapon.Weapon):
            # Is empty
            if len(self.getWeapons()) == 0:
                # Equip
                self.personalWeapon.append(data)
                # Remove from hand
                self.cardsInHand.remove(data)
            elif len(self.getWeapons()) == 1:
                for personalClass in self.getClass():
                    if personalClass.getName() == "barbarian":
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

        # Class
        elif isinstance(data, classes.Class):
            if self.getClass() != []:
                print("You can only have one class equipped at a time.")
                time.sleep(1)
                print("Please unequip the class before proceeding.")
                return
            self.personalClass.append(data)
            self.cardsInHand.remove(data)

        else:
            print("Something went wrong with equippng the card.")


    # Unequip Card
    def unequipCard(self, data) -> None:
        # the format is <class 'int'>
        if isinstance(data, weapon.Weapon):
            self.personalWeapon.remove(data)
        elif isinstance(data, item.Item):
            self.personalItems.remove(data)
        else:
            print("Something went wrong with unequippng the card.")


    # Sell Cards
    def sellEquippedCard(self, data) -> None:
        equippedItems = self.getWeapons() + self.getItems() + self.getClass()
        currentGold = self.getGold()
        for card in equippedItems:
            if card.getName() == data.getName():
                currentGold += card.getCost()
                print(currentGold)
                self.setGold(currentGold)
                # Delete the item from our equipment
                if isinstance(data, item.Item):
                    self.deleteEquippedItem(data)
                    return
                if isinstance(data, weapon.Weapon):
                    self.deleteEquippedWeapon(data)
                    return
                if isinstance(data, classes.Class):
                    self.deleteEquippedClass(data)
                    return

    def sellHandCard(self, data) -> None:
        handItems = self.getCardsInHand()
        currentGold = self.getGold()
        for card in handItems: 
            if card.getName() == data.getName():
                print("Selling the card from your hand.")
                currentGold += card.getCost()
                self.setGold(currentGold)
                # Delete the item from our hand
                self.deleteItemInHand(data)
                return