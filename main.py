# This is a sample Python script.
from AverageCoord import AverageCoord

from AnimalInfo import AnimalInfo

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print("Welcome to Animal Sorter!")
animal = input("Enter animal name: ")
date = input("Enter date you found animal: ")
time = input("Enter time you found animal (Military Time): ")
coordinates = input("Enter coordinates of animal (Ex. (50, -50)): ")

latitude = ""
for i in range(1, coordinates.find(",")):
    latitude += coordinates[i]

longitude = ""
for i in range(coordinates.find(",") + 2, coordinates.find(")")):
    longitude += coordinates[i]
AnimalInfo(animal, date, time, longitude, latitude)