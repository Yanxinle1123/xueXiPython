import time

characters = ["|", "/", "-", "\\"]
while True:
    try:
        for char in characters:
            print(f"\r{char}", end='', flush=True)
            time.sleep(0.25)
    except KeyboardInterrupt:
        break
