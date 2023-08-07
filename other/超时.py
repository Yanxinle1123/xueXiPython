import threading


def timeout_handler():
    print("Timeout!")


timeout = 2  # 10 seconds
print("You have %d seconds to enter input:" % timeout)

# Create a timer thread
timer = threading.Timer(timeout, timeout_handler)
timer.start()

try:
    user_input = input()
except Exception as e:
    print("Error:", e)

# Cancel the timer if user input is received
timer.cancel()

print("You entered: %s" % user_input)
