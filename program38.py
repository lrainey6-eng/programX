import getpass
import time

pwrd = 'versecurecode'

attempt = ''
q = ''

attempt = getpass.getpass("Password: ")

while attempt != pwrd and q != 'q':
	q = input("Incorrect. if you want to quit, type 'q', if not, press enter. ")
	if q != 'q':
		attempt = attempt = getpass.getpass("Password: ")
	else:
		continue

if attempt == pwrd:
	print("Success. ")