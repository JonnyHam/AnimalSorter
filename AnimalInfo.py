def AnimalInfo(animal, date, time, longitude, latitude):
    file1 = open("Animals.txt", "w")
    file1.write(animal + "\n")
    file1.write(date + "\n")
    file1.write(longitude + "\n")
    file1.write(latitude + "\n")
    print("Awesome!, all info has been inputted on file!")