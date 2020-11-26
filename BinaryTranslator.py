import time

print("""

 ______ __________       _______ _______           ________________ _______ _       _______ _       _______________________ _______ 
(  ___ \\__   __( (    /(  ___  |  ____ )\     /|  \__   __(  ____ |  ___  | (    /(  ____ ( \     (  ___  )__   __(  ___  |  ____ )
| (   ) )  ) (  |  \  ( | (   ) | (    )( \   / )     ) (  | (    )| (   ) |  \  ( | (    \/ (     | (   ) |  ) (  | (   ) | (    )|
| (__/ /   | |  |   \ | | (___) | (____)|\ (_) /      | |  | (____)| (___) |   \ | | (_____| |     | (___) |  | |  | |   | | (____)|
|  __ (    | |  | (\ \) |  ___  |     __) \   /       | |  |     __)  ___  | (\ \) (_____  ) |     |  ___  |  | |  | |   | |     __)
| (  \ \   | |  | | \   | (   ) | (\ (     ) (        | |  | (\ (  | (   ) | | \   |     ) | |     | (   ) |  | |  | |   | | (\ (   
| )___) )__) (__| )  \  | )   ( | ) \ \__  | |        | |  | ) \ \_| )   ( | )  \  /\____) | (____/\ )   ( |  | |  | (___) | ) \ \__
|/ \___/\_______//    )_)/     \|/   \__/  \_/        )_(  |/   \__//     \|/    )_)_______|_______//     \|  )_(  (_______)/   \__/
                                                                                                                                    

""")

time.sleep(2)

print("""
                                                      .---.     
                                                       |   |     
/|                                _..._                '---'.--. 
||    .-.          .-           .'     '.              .---.|__| 
||     \ \        / /          .   .-.   .             |   |.--. 
||  __  \ \      / /           |  '   '  |    __       |   ||  | 
||/'__ '.\ \    / /            |  |   |  | .:--.'.     |   ||  | 
|:/`  '. '\ \  / /             |  |   |  |/ |   \ |    |   ||  | 
||     | | \ `  /              |  |   |  |`" __ | |    |   ||  | 
||\    / '  \  /               |  |   |  | .'.''| |    |   ||  | 
 |/\'..' /   / /                |  |   |  |/ /   | |___.'   '|__| 
'  `'-'`|`-' /                 |  |   |  |\ \._,\ '/      '      
         '..'                  '--'   '--' `--'  `"|____.'       


""")

time.sleep(2)



#2 input variables
Base = input("""
What Base will you want to translate to Binary? (Don't type in the prefix btw)

Options: Hexadecimal (Base 16), Octal (Base 8), Decimal (Base 10)?

""")

print("\n")

Value = input(f"What's your {Base} value? (Please enter a valid integer value): ")

#Function to calculate Hexadecimal to Binary
def Hex_Calculate(Value):
	scale = 16
	bits = len(Value)
	Hex_Answer = bin(int(Value, scale))[2:].zfill(bits)
	print (f"Your hexadecimal value in Binary is: {str(Hex_Answer)}")
#Function to calculate Octal to Binary
def Octal_Calculate(Value):
	scale = 8
	bits = len(Value)
	Octal_Answer = bin(int(Value, scale))[2:].zfill(bits)
	print (f"Your octal value in Binary is: {str(Octal_Answer)}")
	print("\n")
#Calculates from Decimal to Binary	
def Dec_Calculate(Value):
	scale = 10
	bits = len(Value)
	Dec_Answer = bin(int(Value, scale))[2:].zfill(bits)
	print (f"Your decimal value in Binary is: {str(Dec_Answer)}")
	
#Perform input checks and calculate the value.
while True:
	try:
		if (Base == 'Hex') or (Base =='hex') or (Base == 'Hexadecimal') or (Base == 'hexadecimal'):
			Hex_Calculate(Value)
			break
		elif (Base == 'Oct') or (Base == 'oct') or (Base == 'Octal') or (Base == 'octal'):
			Octal_Calculate(Value)
			break
		elif (Base == 'Dec') or (Base == 'dec') or (Base == 'Decimal') or (Base == 'decimal'):
			Dec_Calculate(Value)
			break
	except:
		print("Invalid Value Entered. Please Try Again.")
		break
