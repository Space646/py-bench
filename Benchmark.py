from random import *
import time
times = []
average = 0
for x in range(3):
	start = time.perf_counter()
	for i in range(10000000):
		something = []
		something.append(randint(10, 10000))
	stop = time.perf_counter()
	times.append(stop - start)
	print(str(x + 1) + " run complete")
for n in range(3):
	average = average + times[n]
average = average / 3
print("Time: " + str(average))

