"""
TITLE: Madlibs.py
UNIT: 2
AUTHOR: Renato Lima
Mad Libs are stories with blank spaces that a reader can fill in with their own words. The result is usually a funny (or strange) story.
"""

print "The program is started"

main = raw_input("What is the name of the main character? ")
adj1 = raw_input("Pick one adjective: ")
adj2 = raw_input("Pick another adjective: ")
adj3 = raw_input("Pick the last adjective: ")

verb1 = raw_input("Pick one verb: ")
verb2 = raw_input("Pick another verb: ")
verb3 = raw_input("Pick the last verb: ")


noun1 = raw_input("Pick one noun: ")
noun2 = raw_input("Pick another noun: ")
noun3 = raw_input("Pick one more noun: ")
noun4 = raw_input("Pick the last noun: ")

animal = raw_input("Pick one animal: ")
food = raw_input("Pick one food: ")
fruit = raw_input("Pick one fruit: ")
number = raw_input("Pick one number: ")
superhero = raw_input("Pick one superhero: ")
country = raw_input("Pick one country: ")
dessert = raw_input("Pick one dessert: ")
year = raw_input("Pick one year: ")



#The template for the story

STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world." % (adj1, main, verb1, adj2, noun1, noun2, animal, food, verb2, noun3, fruit, adj3, main, verb3, number, main, superhero, superhero, main, country, main, dessert, main, year, noun4)

print STORY
