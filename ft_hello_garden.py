def hello_garden():
    print("hello")

def ft_plot_area():
    print('enter lenght')
    print('enter width')
    len = int(input())
    width = int(input())
    print(len * width)

def ft_harvest_total():
    print("enter day 1")
    day1 = int(input())
    print("enter day 2")
    day2 = int(input())
    print("enter day 3")
    day3 = int(input())
    print(f'Day 1 harvest: {day1}')
    print(f'Day 2 harvest: {day2}')
    print(f'Day 3 harvest: {day3}')
    print(f'total = {day1 + day2 + day3}')

def ft_plant_age():
    print("Enter plant age in days: ", end = "")
    age = int(input())
    #print(f"{age}")
    if (age >= 75):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow")

def ft_water_reminder():
    print("days since last watering: ")
    day = int(input())
    if (day > 2):
        print("water the plants!")
    else:
        print("Plants are fine")

def ft_count_harvest_iterative(n):
    print(f"Days until harvest: {n}")
    for x in range(1, n + 1):
        print(f"Day {x}")
    print("Harvest time!")

def recur(n):
    if n > 1 :
        recur(n - 1)
    print(f"Day {n}")
    

def ft_count_harvest_recursive(n):
    print(f"Days until harvest: {n}")
    recur(n)
    print("Harvest time!")
   

if __name__ == "__main__":
    ft_count_harvest_recursive(5)


#Days since last watering: 4
#Water the plants!
#>>> ft_water_reminder()
#Days since last watering: 1
#Plants are fine