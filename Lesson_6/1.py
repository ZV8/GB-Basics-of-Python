import time
from colorama import Fore


class TrafficLight:
    def __init__(self):
        self.__color = [['red', 7, Fore.RED], ['yellow', 2, Fore.YELLOW], ['green', 5, Fore.GREEN],
                        ['yellow', 2, Fore.YELLOW]]

    def running(self):
        print("I'm running")
        while True:
            for item in self.__color:
                print(f"{item[2]}{item[0]}")
                time.sleep(item[1])


tl = TrafficLight()
tl.running()
