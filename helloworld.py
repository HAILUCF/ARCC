import os
import time

# Get the host's name
myhost = os.uname()[1]
time.sleep(10)
print("Hello World from", myhost )