import pyttsx3
import os

pyttsx3.speak("Welcome to Pavi's file. Please Enter your choice :")

print()
print("Press 1: To open chrome browser")
print("Press 2: To open notepad")
print("Press 3: To open media player")
print()

print("Enter ur choice" , end='')

p = input()
print(p)
# os.system(p)

if int(p) == 1:
   os.system("chrome")

elif int(p) == 2:
   os.system("notepad")

elif int(p) == 3:
   os.system("wmplayer")


else:
   print(" Did not support")

