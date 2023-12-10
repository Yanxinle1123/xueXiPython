import time


def slow_print(text, delay=0.22):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # 换行


text = "Hello, I am an AI language model."
slow_print(text)
