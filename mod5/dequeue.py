from collections import deque


class Queue:
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

    def __iter__(self):
        return iter(self._elements)

    def __len__(self):
        return len(self._elements)

    def __reversed__(self):
        return reversed(self._elements)

    def __contains__(self, element):
        return element in self._elements

    def shows(self):
        for q in self:
            print(f"{q:<3}", end="")
        print()


def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(f"\ncontain 2 in queue ? {queue.__contains__(2)}")
    queue.shows()
    print(f"len de : {len(queue)}")
    queue.__reversed__()
    queue.shows()
    queue.dequeue()
    queue.shows()


if __name__ == "__main__":
    main()
