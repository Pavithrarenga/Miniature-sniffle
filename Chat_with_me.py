import pyttsx3
import os

pyttsx3.speak("Welcome to Pavi's Program. Explore me!!:")

#print()
#print()

while True:
	print("Chat with me your requirements : " , end='')

	p = input()
	print(p)
	# os.system(p)

	if (("run" in p) or ("execute" in p) or ("open" in p)) and ("chrome" in p):
   		os.system("chrome")

	elif (("run" in p) or ("execute" in p)or ("open" in p)) and (("notepad" in p) or ("editor" in p)):
   		os.system("notepad")

	elif (("run" in p) or ("open" in p) or ("execute" in p))and ("media" in p) and ("player" in p):
   		os.system("wmplayer")
	elif ("exit" in p) or ("quit" in p):
		break

	else:
   		print(" Did not support")

