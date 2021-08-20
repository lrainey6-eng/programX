import time
import random

num = random.randint(2, 100)
guessNum = 1
guess = ''

print("Guess the hidden number between 1 and 100. ")

time.sleep(0.3)

while guess != num:
	guess = int(input("Guess %d: " % (guessNum)))
	if guess == num:
		print("Correct! ")
		time.sleep(1)
	elif guess > num:
		time.sleep(0.5)
		print("Lower... ")
		time.sleep(0.5)
	elif guess < num:
		time.sleep(0.5)
		print("Higher... ")
		time.sleep(0.5)
