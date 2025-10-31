# Задание 1.
# Напишите программу, которая создаёт 2 потока для вычисления квадратов и кубов целых чисел от 1 до 10.

import threading

def square() -> None:
    for i in range(1, 11):
        print(f"{i}-th square: {i**2}")

def cube() -> None:
    for i in range(1, 11):
        print(f"{i}-th cube: {i**3}")

if __name__ == "__main__":
    t1 = threading.Thread(target=square)
    t1.start()

    t2 = threading.Thread(target=cube)
    t2.start()

    t1.join()
    t2.join()