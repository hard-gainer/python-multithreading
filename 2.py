# Задание 2.
# Напишите программу, которая создаёт несколько потоков для выполнения функции, которая
# выводит целые числа от 1 до 10 с задержкой в 1 секунду.

import threading
import time

counter = 1
lock = threading.Lock()

def print_numbers(thread_name: str) -> None:
    global counter
    while True:
        with lock:
            if counter > 10:
                break
            print(f"{thread_name}: {counter}")
            counter += 1
        time.sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=print_numbers, args=("Поток 1",))
    t2 = threading.Thread(target=print_numbers, args=("Поток 2",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    print("Все потоки завершены!")