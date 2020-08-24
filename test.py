import time

for i in range(5):
    print("Loading" + "."*i, end="\r")
    time.sleep(0.1)
print('\n', end='\r')
time.sleep(10)