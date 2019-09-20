import random

#Class to control the movements in a gacha game. Every character has 2 movements.
class Moves:
	def __init__(self, unicId, name, power, element):
		self.unicId = unicId
		self.name = name
		self.power = power
		self.element = element

	#Auto explain
	def returnMoveName(self):
		return self.name

#Class of the characters in a gacha game. Characters has ID, Name, Color(type), Rarity, Attack, Defense and Movements.
class Char:
	def __init__(self, unicId, name, color, rarity, attack, defense, move1, move2):
		self.unicId = unicId
		self.name = name
		self.color = color
		self.rarity = rarity
		self.attack = attack
		self.defense = defense
		self.move = []
		self.move.append(move1)
		self.move.append(move2)

	#Function to print the information of a character. When the game has graphics this functions will be useless.
	def printChar(self):
		print(self.unicId, "|", self.name, "|", self.color, "|", self.rarity, "|", self.attack, "|", self.defense,
			"|", self.move[0].printMove(), "|", self.move[1].printMove())

	#Function to calculate the power of the move, used in battles in a gacha game. Receives de stat of the move (attack or defense) and
	def powerCalculator(self, stat, numMove):
		if stat == "attack":
			return random.randint(self.attack, self.attack+self.move[numMove-1].power)
		if stat == "defense":
			return random.randint(self.defense, self.defense+self.move[numMove-1].power)

#Examples of movements and characters, don't will be on the final version of the software.
moveList = []
moveList.append(Moves("H000", "None", 0, "NUL"))
moveList.append(Moves("H001","Movement 1", 10, "RED"))
moveList.append(Moves("H002","Movement 2", 10, "GND"))
charList = []
charList.append(Char("C001", "Character 1", "RED", "SR", 1, 1, moveList[1], moveList[0]))
charList.append(Char("C002", "Character 2", "BLU", "SR", 1, 1, moveList[2], moveList[0]))