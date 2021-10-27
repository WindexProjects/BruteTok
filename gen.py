#Tiktok Username Gen, works with TikBrute.py!
import random
from subprocess import call
call('title Tiktok Username Gen ------Made by Windex \U0001F4A7', shell=True)
def write(name):
	with open('usernames.txt','a') as f:
		f.write(f"{name}\n")
lets = 'abcdefghijklmnopqrstuvwxyz'
options = '1) 4 Letter Usernames\n2) 5 Letter Usernames\n3) 6 Letter Usernames\n4) Custom Length Username\n'
print(options)
x = int(input("Enter Choice: "))

match x:
	case 1:
		for x in range(int(input("How many Names? "))):
			name = ''.join([random.choice(lets) for x in range(4)])
			write(name)
	case 2:
		for x in range(int(input("How many Names? "))):
			name = ''.join([random.choice(lets) for x in range(5)])
			write(name)

	case 3:
		for x in range(int(input("How many Names? "))):
			name = ''.join([random.choice(lets) for x in range(6)])
			write(name)

	case 4:
		i = int(input("How many Names? "))
		z = int(input("How many letters?: "))
		for x in range(i):
			name = ''.join([random.choice(lets) for x in range(z)])
			write(name)
