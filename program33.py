
import time

print("This is Program 33.")
print("This program will ask for an input and display it out on the screen an inputted number of times.")

time.sleep(1)

sentance = input("Sentance for copying: ")

times = int(input("How many times copied? "))

for i in range(1, times):
	print(sentance)

