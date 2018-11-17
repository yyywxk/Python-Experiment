import time
import winsound
def happy():
   print("happy birthday to you")
def sing(person):
   happy()
   happy()
   print("happy birthday dear",person)
   happy()
person=input("input a name")
sing(person)

winsound.PlaySound("D:/birthday",winsound.SND_NOSTOP)
input("press<enter>")
