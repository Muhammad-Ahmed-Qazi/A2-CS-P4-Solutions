import datetime

# 2a
class Character:
    # PRIVATE CharacterName : STRING
    # PRIVATE DateOfBirth : DATE
    # PRIVATE Intelligence : REAL
    # PRIVATE Speed : INTEGER

    def __init__(self, CharacterName, DateOfBirth, Intelligence, Speed):
        self.__CharacterName = CharacterName
        self.__DateOfBirth = DateOfBirth
        self.__Intelligence = Intelligence
        self.__Speed = Speed

    def GetIntelligence(self):
        return self.__Intelligence
    
    def GetName(self):
        return self.__CharacterName
    
    def SetIntelligence(self, Intelligence):
        self.__Intelligence = Intelligence

    def Learn(self):
        self.__Intelligence = self.__Intelligence * 1.1
    
    def ReturnAge(self):
        YearsOld = 2023 - self.__DateOfBirth.year
        return YearsOld

# 2c
class MagicCharacter(Character):
    # PRIVATE Element : STRING

    def __init__(self, Element, CharacterName, DateOfBirth, Intelligence, Speed):
        super().__init__(CharacterName, DateOfBirth, Intelligence, Speed)
        self.__Element = Element
    
    def Learn(self):
        if self.__Element == "fire" or self.__Element == "water":
            self.SetIntelligence(self.GetIntelligence() * 1.2)
        elif self.__Element == "earth":
            self.SetIntelligence(self.GetIntelligence() * 1.3)
        else:
            self.SetIntelligence(self.GetIntelligence() * 1.1)

# 2b
# Main program
# FirstCharacter = Character("Royal", datetime.date(2019, 1, 1), 70, 30)

# FirstCharacter.Learn()

# print("Name:", FirstCharacter.GetName())
# print("Age:", FirstCharacter.ReturnAge())
# print("Intelligence:", FirstCharacter.GetIntelligence())

FirstMagic = MagicCharacter("fire", "Light", datetime.date(2018, 3, 3), 75, 22)

FirstMagic.Learn()
print("Name:", FirstMagic.GetName())
print("Age:", FirstMagic.ReturnAge())
print("Intelligence:", FirstMagic.GetIntelligence())