import csv
import random 
import urllib.request
from PIL import Image
attackMultiplier1 = 0
attackMultiplier2 = 0
damage1 = 0
damage2 = 0
""" 

to run this, do "pip install pillow"
ITLL BE WORTH IT I PROMISE!!!
the images you'll get won't be the pokemon in the actual battles, but if the data base we were given was the actual pokedex in order, it would've matched up and been super cool. I hope you enjoy the added touch!

"""

file4 = open("PokemonMoves.csv", "r")
data6 = list(csv.reader(file4, delimiter = ","))


file3=open("AttackTypeMultipliers.csv", "r")
data5 = list(csv.reader(file3, delimiter = ","))

file = open("Pokemon_updated.csv", "r")
data = list(csv.reader(file, delimiter=","))

pokemon1 = random.choice(data)
pokemon2 = random.choice(data)

print(pokemon1)
print(pokemon2)

pokemonName1 = pokemon1[0]
pokemonName2 = pokemon2[0]


file2 = open("PokemonLearnableMoves.csv", "r")
data2 = list(csv.reader(file2, delimiter=","))


for x in range(len(data2)):
	find1 = data2[1][0]
	data3 = data2[x][0]
	if(data3 == pokemonName1.lower()):
		break


for y in range(len(data2)):
	find1 = data2[1][0]
	data3 = data2[y][0]
	if(data3 == pokemonName2.lower()):
		break





listMoves1 = list(data2[x][1].split("|"))
listMoves2 = list(data2[y][1].split("|"))

Moveset1 = random.sample(listMoves1, 4)
Moveset2 = random.sample(listMoves2, 4)



Type1 = pokemon1[1]
Type2 = pokemon2[1]

Stats1 = list(pokemon1[2].split("|"))
Stats2 = list(pokemon2[2].split("|"))

print(Stats1)
print(Stats2)








#PICTURES

Bruh1 = 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/'
Bruh2= str(data.index(pokemon1))
Bruh3 = '.png'

URL = Bruh1 + Bruh2 + Bruh3


urllib.request.urlretrieve(URL, "file_name.png")

img = Image.open("file_name.png")

img.show()


Bruh4 = 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/'
Bruh5= str(data.index(pokemon2))
Bruh6 = '.png'

URL2 = Bruh4 + Bruh5 + Bruh6

urllib.request.urlretrieve(URL2, "file_name2.png")

img = Image.open("file_name2.png")

img.show()

#PICTURES END





#STATS!
HP1 = Stats1[0]
HP2 = Stats2[0]
HP1 = HP1.split(":")
HP2 = HP2.split(":")
HP1 = HP1[1]
HP2 = HP2[1]
print("Pokemon1 HP ", end="")
print(HP1)
print("Pokemon2 HP ", end="")
print(HP2)

ATK1 = Stats1[1]
ATK2 = Stats2[1]
ATK1 = ATK1.split(":")
ATK2 = ATK2.split(":")
ATK1 = ATK1[1]
ATK2 = ATK2[1]
print("Pokemon1 ATK ", end="")
print(ATK1)
print("Pokemon2 ATK ", end="")
print(ATK2)

DEF1 = Stats1[2]
DEF2 = Stats2[2]
DEF1 = DEF1.split(":")
DEF2 = DEF2.split(":")
DEF1 = DEF1[1]
DEF2 = DEF2[1]
print("Pokemon1 DEF ", end="")
print(DEF1)
print("Pokemon2 DEF ", end="")
print(DEF2)

SPA1 = Stats1[3]
SPA2 = Stats2[3]
SPA1 = SPA1.split(":")
SPA2 = SPA2.split(":")
SPA1 = SPA1[1]
SPA2 = SPA2[1]
print("Pokemon1 SPA ", end="")
print(SPA1)
print("Pokemon2 SPA ", end="")
print(SPA2)

SPD1 = Stats1[4]
SPD2 = Stats2[4]
SPD1 = SPD1.split(":")
SPD2 = SPD2.split(":")
SPD1 = SPD1[1]
SPD2 = SPD2[1]
print("Pokemon1 SPD ", end="")
print(SPD1)
print("Pokemon2 SPD ", end="")
print(SPD2)



Speed1 = Stats1[5]
Speed2 = Stats2[5]
Speed1 = Speed1.split(":")
Speed2 = Speed2.split(":")
Speed1 = Speed1[1]
Speed2 = Speed2[1]
print("Pokemon1 Speed ", end="")
print(Speed1)
print("Pokemon2 Speed ", end="")
print(Speed2)


HP1 = int(HP1)
HP2 = int(HP2)
ATK1 = int(ATK1)
ATK2 = int(ATK2)
DEF1 = int(DEF1)
DEF2 = int(DEF2)


SPA1 = int(SPA1)
SPA2 = int(SPA2)
SPD1 = int(SPD2)
SPD2 = int(SPD2)
Speed1 = int(Speed1)
Speed2 = int(Speed2)


pokemon1Type = list(pokemon1[1].split("|"))
pokemon2Type = list(pokemon2[1].split("|"))
print(pokemon1Type)
print(pokemon2Type)







def TypeMatchup():
	global attackMultiplier1
	global attackMultiplier2
	global damage1
	global damage2
	global data5
	global pokemon1Type
	global Type2
	global pokemon2Type
	global Type1

	bruh21 = data5[0]
	for p in range (len(data5[0])):
		Types = data5[0][p]
		
		#if the pokemon being attacked has 2 types
		#find the index of both types in the first data5 element
		#find the type of the attack move
		#find the data5 element for that specific attackType
		#see what is in the positions for the pokemon being attacked's type
		#if they are 2 and 0.5, they become a 1 (just multiply for this!)
		#if they are 0.5 and 2, they become a 1
		#if they are 1 and 1, they become a 1
		#if they are a 2 and 1, they become a 2
		#if they are a 2 and 2, they become a 4
		#this is what 2 is doing to 1
	if (len(pokemon1Type) > 1):	
		#type of the attack
		Typeindex = bruh21.index(Type2)
		#type one of the pokemon
		Typeindex1 = bruh21.index(pokemon1Type[0])
		#type two of the pokemon
		Typeindex2 = bruh21.index(pokemon1Type[1])
		attackList = data5[Typeindex]
		attackMultiplier1 = float(attackList[Typeindex1])*float(attackList[Typeindex2])
		#if the pokemon being attacked has 1 type
	else:
		Typeindex = bruh21.index(Type2)
		Typeindex1 = bruh21.index(pokemon1Type[0])
		attackList = data5[Typeindex]
		attackMultiplier1 = float(attackList[Typeindex1])
	
	#pokemon1 attacking pokemon 2
	
	if (len(pokemon2Type) > 1):	
		#type of the attack
		Typeindex = bruh21.index(Type1)
		#type one of the pokemon
		Typeindex1 = bruh21.index(pokemon2Type[0])
		#type two of the pokemon
		Typeindex2 = bruh21.index(pokemon2Type[1])
		attackList = data5[Typeindex]
		attackMultiplier2 = float(attackList[Typeindex1])*float(attackList[Typeindex2])
		#if the pokemon being attacked has 1 type
	else:
		Typeindex = bruh21.index(Type1)
		Typeindex1 = bruh21.index(pokemon2Type[0])
		attackList = data5[Typeindex]
		attackMultiplier2 = float(attackList[Typeindex1])
		





def DamageCalc1():

	global HP1
	global damage2

	#Pokemon 1 loses HP from what 2 does to 1
	print("First Pokemon Current HP")
	print(HP1)
	HP1 = int(HP1)
	HP1 = HP1 - damage2
	print("First Pokemon New HP")
	print(HP1)

def DamageCalc2():

	global HP2
	global damage1

	#Pokemon 2 loses HP from what 1 does to 2
	print("Second Pokemon Current HP")
	print(HP2)
	HP2 = int(HP2)
	HP2 = HP2 - damage1
	print("Second Pokemon New HP")
	print(HP2)

	#Damage Calc end!
	

def CheckWin():
	if(HP1 <= 0):
		return True
	if(HP2 <=0):
		return True

	return False








#Now loop the attacks

while(HP1 > 0 and HP2 > 0):

		
	print(Moveset1)
	print("Pick a move for ", end="")
	print(pokemonName1, end="")
	print("! (Enter 1,2,3, or 4) ")
	A = input()
	A = int(A)


	print(pokemonName1, end="")
	print(" used ", end="")
	print(Moveset1[A-1],end="")
	print("!")



	print(Moveset2)
	print("Pick a move for ", end="")
	print(pokemonName2, end="")
	print("! (Enter 1,2,3, or 4) ")
	B = input()
	B = int(B)

	print(pokemonName2, end="")
	print(" used ", end="")
	print(Moveset2[B-1], end="")
	print("!")


	
	

	for b in range (len(data6)):
		ATKName = data6[b][0]
		ATKName = ATKName.replace(" ", "");
		ATKName1 = ATKName.lower()
		Accuracy1 = data6[b][1]
		BasePower1 = data6[b][2]
		Category1 = data6[b][3]
		PP1 = data6[b][4]
		Type1 = data6[b][5]
		Effect1 = data6[b][6]
		if(ATKName1 == Moveset1[A-1]):
			break

	print("Attack 1 statistics")
	print(ATKName1)
	print(Accuracy1)
	print(BasePower1)
	print(Category1)
	print(PP1)
	print(Type1)
	print(Effect1)

	for b in range (len(data6)):
		ATKName = data6[b][0]
		ATKName = ATKName.replace(" ", "");
		ATKName2 = ATKName.lower()
		Accuracy2 = data6[b][1]
		BasePower2 = data6[b][2]
		Category2 = data6[b][3]
		PP2 = data6[b][4]
		Type2 = data6[b][5]
		Effect2 = data6[b][6]
		if(ATKName2 == Moveset2[B-1]):
			break

	print("Attack 2 statistics")
	print(ATKName2)
	print(Accuracy2)
	print(BasePower2)
	print(Category2)
	print(PP2)
	print(Type2)
	print(Effect2)


	BP1 = int(BasePower1)
	BP2 = int(BasePower2)



	if(Category1 == "Physical"):
		damage1 = ( (12/250) * (ATK1 / DEF2) * BP1 ) + 2
	else:
		damage1 = ( (12/250) * (SPA1 / SPD2) * BP1) + 2
 
	print("Damage1 ", end="")
	print(damage1)


	if(Category1 == "Physical"):
		damage2 = ( (12/250) * (ATK2 / DEF1) * BP2 ) + 2
	else:
		damage2 = ( (12/250) * (SPA2 / SPD1) * BP2) + 2

	print("Damage2 ", end="")
	print(damage2)


	#STAB BONUS

	if(len(pokemon1Type) > 1):
		if(pokemon1Type[0] == Type1 or pokemon1Type[1] == Type1): 
			damage1 = damage1*1.25
	elif(len(pokemon1Type) == 1):
		if(pokemon1Type[0] == Type1):
			damage1 = damage1*1.25

	if(len(pokemon2Type) > 1):
		if(pokemon2Type[0] == Type2 or pokemon2Type[1] == Type2): 
			damage2 = damage2*1.25
	elif(len(pokemon2Type) == 1):
		if(pokemon2Type[0] == Type2):
			damage2 = damage2*1.25

	
	#STAB done
	#damage1 is what pokemon1 is doing to pokemon2
	#damage2 is what pokemon2 is doing to pokemon1

	print("Damage1 ",end="") 
	print(damage1)
	print("Damage2 ",end="") 
	print(damage2)

	TypeMatchup()
	#multiply by what 1 is doing to 2
	damage1 = damage1*attackMultiplier2
	#multiply by what 2 is doing to 1
	damage2 = damage2*attackMultiplier1
	#attack multiplier done
	print("Damage1 ",end="") 
	print(damage1)
	print("Damage2 ",end="") 
	print(damage2)



	#DamageCalc()

	if(Speed1 > Speed2):
		DamageCalc2()
		if(CheckWin()):
			break
		DamageCalc1()
		if(CheckWin()):
			break
	
	elif(Speed2 > Speed1):
		DamageCalc1()
		if(CheckWin()):
			break
		DamageCalc2()
		if(CheckWin()):
			break
	


if(HP1 <=0):
	print(pokemonName2, end="") 
	print(" wins!")
elif(HP2 <= 0):
	print(pokemonName1, end="")
	print(" wins!")	









  

file.close()
file2.close()
file3.close()
file4.close()
exit()


