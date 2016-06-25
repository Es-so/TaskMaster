import random
import sys
import time
import random
import sys
from threading import Thread, RLock
import time

verrou = RLock()

class Afficheur(Thread):

    def __init__(self, mot):
        Thread.__init__(self)
        self.mot = mot

    def run(self):
        i = 0
        while i < 5:
            with verrou:
                for lettre in self.mot:
                    sys.stdout.write(lettre)
                    sys.stdout.flush()
                    attente = 0.2
                    attente += random.randint(1, 60) / 100
                    time.sleep(attente)
            i += 1

thread_2 = Afficheur("TORTUE")


def start_process(arg):
	i = 0
	print(arg)
	thread_1 = Afficheur(arg)
	thread_1.start(arg)
	thread_1.join()
	# while i < int(arg):
	# 	time.sleep(1)
	# 	sys.stdout.write(str(i))
	# 	sys.stdout.flush()
	# 	attente = 1
	# 	# attente += random.randint(1, 60) / 100
	# 	i += 1


