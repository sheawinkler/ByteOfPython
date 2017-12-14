import sys
import time

f = None
try:
    #change to any text file to test
    f = open("poem.txt")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print("Press ctrl+c now")
        #this ensures that it runs for a while
        time.sleep(2)

except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file !!")
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")
