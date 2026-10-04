import time

print("Doing some computation...")

total = 0

for i in range(10_000_000):
    total += i

time.sleep(2)

print("Done!")