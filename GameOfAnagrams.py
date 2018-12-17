import random
class Colour:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Player():
	def __init__(self, coins, attempts):
		self.attempts = attempts
		self.coins = coins        

def HintMaker(source, index):
	dest = ''
	for i in range(0, len(word)):
    		if i == index:
        		dest += word[i]
    		else:
        		dest += source[i] 
	return dest	

P = Player(attempts = 3, coins = 50.0)
f = open('Dictionary.txt')
content = f.read().split()
f.close()    

print(Colour.BLUE + 'WELCOME TO THE GAME OF ANAGRAMS. EACH TIME YOU WILL BE GIVEN A WORD WHICH IS FORMED BY JUMBLING THE LETTERS OF A MEANINGFUL WORD. FOR EXAMPLE : "LALIRNBTI" IS FORMED BY JUMLING THE ORIGINAL WORD "BRILLIANT". YOU HAVE TO GUESS THE ORIGINAL WORD. YOU WILL BE GIVEN A HINT WHICH WILL SHOW YOU A FEW LETTERS OF THE ORIGINAL WORD AND YOU WILL GET 3 ATTEMPTS BY DEFAULT FOR EACH WORD. YOU CAN OPT FOR MORE HINT AND ATTEMPTS BY USING COINS, SO USE YOUR COINS WISELY. ALSO YOU WILL WIN COINS ON EVERY CORRECT GUESS, WINNING AMOUNT DEPENDS ON IN HOW MANY TOTAL ATTEMPTS YOU GUESSED CORRECTLY:\nGUESSED CORRECTLY IN 1st ATTEMPT = 100% HIKE IN COINS\nGUESSED CORRECTLY IN 2nd ATTEMPT = 50% HIKE IN COINS\nGUESSED CORRECTLY IN 3rd ATTEMPT = 33.33% HIKE IN COINS\nGUESSED CORRECTLY IN 4th ATTEMPT = 25% HIKE IN COINS....and so on\nYOU CAN OF COURSE QUIT THE GAME ANYTIME YOU WANT\n' + Colour.END)
input('Press ENTER to begin\n')
while True:
	i = random.randint(19, len(content)-1)	
	word = content[i]
	if '\'' in word or len(word) < 5:
    		continue 
	shuffled_word = list(word)
	while ''.join(shuffled_word) == word:	
		random.shuffle(shuffled_word)
	p1 = random.randint(0, len(word)-1)
	p2 = random.randint(0, len(word)-1)
	while abs(p1 - p2) < 2:
    		p2 = random.randint(0, len(word)-1)
	hint = ''
	for i in range(0, len(word)):
    		if i == p1 or i == p2:
        		hint += word[i]
    		else:
        		hint += '*'
	
	P.attempts = 3
	turns = 0
	while True:
		print('Your word - {}'.format(Colour.RED + '"' + ''.join(shuffled_word).upper() + '"' + Colour.END))
		print('(Hint : {})'.format(Colour.GREEN +'"' + hint.upper() + '"' + Colour.END))
		print('\n1. Guess\n2. Reveal the 1st letter in hint(cost - 40% of total coins)\n3. Reveal any new letter in hint(cost - 20% of total coins)\n4. Show no of attempts left\n5. Show available coins\n6. Get an extra attempt(cost - 10% of total coins)\n7. Show answer and go to next word\n8. Quit game')
		try:
			choice = int(input('Enter a choice\n'))
		except:
			print('Please enter valid choice\n')
			continue
		if choice == 1:
			if P.attempts:
				turns += 1
				user_word = input('Your Guess please:\n')
				if user_word == word.upper():
					print('Correct! Congrats, you have won some coins\nAvailable coins = {}'.format(P.coins))
					P.coins = P.coins + P.coins/turns
					break
			
				else:
           		        	P.attempts -= 1
           		        	print('Incorrect\n')
			else:
				print('Sorry no of attempts expired\n')
		elif choice == 2:
			if hint[0] == '*':
				hint = HintMaker(hint, 0)
				P.coins = P.coins - P.coins * (40/100) 
		elif choice == 3:
			while hint[p2] != '*' or p2 == 0:
    				p2 = random.randint(0, len(word)-1)
			hint = HintMaker(hint, p2)
			P.coins = P.coins - P.coins * (20/100) 
		elif choice == 4:
			print('Attempts left = {}'.format(P.attempts))
		elif choice == 5:
			print('Available coins = {}'.format(P.coins))
		elif choice == 6:
			P.attempts += 1
			print('No of attempts increased by one\n')
			P.coins = P.coins - P.coins * (10/100)
		elif choice == 7:
			print('Correct word is {}\n'.format(Colour.RED + '"' + word.upper() + '"' + Colour.END))
			break
		elif choice == 8:
			exit()
		else:
			print('Please enter valid choice\n')
