import time
sec = int(input("Seconds to count down: "))
while sec: print(sec); time.sleep(1); sec -= 1
print("Time's up!")
