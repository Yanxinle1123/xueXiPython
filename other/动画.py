import threading
import time


def show_progress(text, characters, switch_interval, task_func, *args, **kwargs):
    if characters is None:
        characters = ["/", "-", "\\", "|"]

    if switch_interval is None:
        switch_interval = 0.25

    characters = [str(text) + char for char in characters]

    def run_task():
        nonlocal result
        result = task_func(*args, **kwargs)

    result = None
    task_thread = threading.Thread(target=run_task)
    task_thread.start()

    while task_thread.is_alive():
        for char in characters:
            print(f"\r{char}", end='', flush=True)
            time.sleep(float(switch_interval))

    task_thread.join()
    print(f"\r{result}")
