""" 
TITLE: AreaCalculator.py
AUTHOR: Renato Lima
The program should do the following:
1- Prompt the user to select a shape
2- Depending on the shape the user selects, calculate the area of that shape
3- Print the area of that shape to the user
"""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "The calculator is starting"
print '%s/%s/%s %s:%s' % (now.month, now.day, now.year, now.hour, now.minute)
sleep(1)

hint = "Don't forget to include the correct units! \nExiting..."
option = raw_input("Enter C for Circle or T for Triangle: ")
option = option.upper()

if option == 'C':
  radius = float(raw_input("Enter radius: "))
  area = pi * radius**2
  print "The pie is baking..."
  sleep(1)
  print ("Area: %.2f. \n%s" % (area, hint))
elif option == 'T':
  base = float(raw_input("Enter the base of the triangle: "))
  height = float(raw_input("Enter the height of the triangle: "))
  area = (base * height)/2
  print "Uni Bi Tri..."
  sleep(1)
  print ("Area: %.2f. \n%s" % (area, hint))
else:
	print "Error! Invalid shape selector specified. Exiting."
