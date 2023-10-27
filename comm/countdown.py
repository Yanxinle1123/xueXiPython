import time

from comm.common import value4

start_time = 0
end_time = 0


def start_timing():
    global start_time
    start_time = time.time()


def stop_timing(round_off=2):
    global start_time, end_time
    end_time = time.time()
    elapsed_time = end_time - start_time
    if not round_off:
        return value4(elapsed_time)
    else:
        elapsed_time = value4(round(elapsed_time, round_off))
        return elapsed_time

# start_timing()
# time.sleep(2)
# a = stop_timing(0)
# print(a)
