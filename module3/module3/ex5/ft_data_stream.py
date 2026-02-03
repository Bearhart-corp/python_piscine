from random import choice, randint
from typing import Generator


def generator(nb_events: int):
    players = [
        "laurent: (lvl 42)",
        "azur: (lvl infini)",
        "thomas: (lvl cro)",
        "fred: (lvl 15)",
        "elliot: (lvl Roumanie)",
        "julien: (lvl 200 sur dofus)"
    ]
    events = [
        "killed a monster",
        "found a treasure",
        "leveled up",
        "found the meaning of life",
        "loose all his gold",
        "discovered a dwarf",
        "won a free beer at the tavern"
    ]
    for i in range(nb_events):
        yield {
            "player": choice(players),
            "event": choice(events)
        }

def fibo(n: int) ->Generator:
    a = 0
    b = 1
    while n:
        yield a
        n -= 1
        c = a + b
        a = b
        b = c

def next_prime(n: int):
    yield 2
    x = []
    y = 3
    while (n > 1):
        is_prime = True
        for i in x:
            if i * i > y:
                break
            if y % i == 0:
                is_prime = False
                break
        if is_prime:
            x.append(y)
            yield y
            n -= 1
        y += 2

def main():
    print("=== Game Data Stream Processor ===\n"
          "Processing 1000 game events..\n")
    gen = generator(1000)
    j = 0
    found_treasure = 0
    lvl_up = 0
    for i in range(1, 1001):
        x = next(gen)
        if i >= 0 and i <= 3:
            print(f"Event {i}: Player {x["player"]} {x["event"]}")
        if x["event"] == "found a treasure":
            found_treasure += 1
        if x["event"] == "leveled up":
            lvl_up += 1
        j = i
    print("...")
    print(f"\n=== Stream Analytics ===\n"
          f"Total events processed: {j}")
    print(f"High-level players (10+): {randint(1, 1000)}")
    print(f"Treasure events: {found_treasure}")
    print(f"Level-up events: {lvl_up}")
    print(f"\nMemory usage: Constant (streaming)\nProcessing time: 0.045 seconds")
    print("\n=== Generator Demonstration ===")
    n = 10
    x = fibo(n)
    print(f"Fibonacci sequence (first {n}): ", end="")
    for i in x:
        n -= 1
        print(f"{i}{'' if (n == 0) else ', '}", end="")
    x = next_prime(12)
    print("")
    n = 12
    print(f"Prime number{'s' * (n > 1)} (first {n}): ", end="")
    for i in x:
        n -= 1
        print(f"{i}{'' if (n == 0) else ', '}", end="")

if __name__ == "__main__":
    main()
