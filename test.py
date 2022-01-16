from time import sleep
import threading as th

def process_one():
    for i in range (3):
        print("OOOOOOOOOOOOO")
        sleep(0.3)


def process_two():
    for i in range (3):
        print("OOOOOOOOOOOOO")
        sleep(0.3)

th1 = th.Thread(target=process_one)
th2 = th.Thread(target=process_two)

th1.start()
th2.start()

print("Fin du programme")