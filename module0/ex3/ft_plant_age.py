def ft_plant_age():
    print("Enter plant age in days: ", end = "")
    age = int(input())
    #print(f"{age}")
    if (age >= 75):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow")
