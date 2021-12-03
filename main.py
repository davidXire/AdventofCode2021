import time
from day1 import day1
from day2 import day2
from day3 import day3

if __name__ == "__main__":
  start_time = time.time()
  day3.s1()
  print("--- %s seconds ---" % (time.time() - start_time))