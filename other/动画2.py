import threading
import time

from googletrans import Translator
from openpyxl.formula.translate import TranslatorError


def translate_text(text, src='zh-cn', dest='en'):
    try:
        translator = Translator()
        translation = translator.translate(text, src=src, dest=dest)

        return translation.text
    except TranslatorError as e:
        return f"Translation error: {e}"


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

    task_thread.join()  # 确保任务线程已经完成
    print(f"\r{result}")


if __name__ == "__main__":
    chinese_text = (
        "Python is a high-level, interpreted programming language that has gained immense popularity since"
        " its creation by Guido van Rossum and its first release in 1991. Known for its simplicity and"
        " readability, Python has become a favorite among both beginners and experienced developers."
        " Its design philosophy emphasizes code readability and simplicity, making it an ideal choice"
        " for a wide range of applications, from web development to data science, artificial intelligence,"
        " and more. One of the key features of Python is its clean and straightforward syntax, which allows"
        " developers to express concepts in fewer lines of code compared to other programming languages"
        " like C++ or Java. This simplicity not only makes Python easy to learn but also enhances"
        " productivity, as developers can write and maintain code more efficiently. Python's syntax is"
        " often described as being close to human language, which reduces the learning curve for new"
        " programmers and allows them to focus on solving problems rather than struggling with complex"
        " syntax. Python is an interpreted language, meaning that code is executed line by line, which"
        " facilitates interactive testing and debugging. This feature is particularly useful during the"
        " development process, as it allows developers to test small code snippets and see immediate"
        " results. Additionally, Python's interactive shell, known as the REPL (Read-Eval-Print Loop), "
        "provides an environment where developers can experiment with code and receive instant feedback, "
        "further enhancing the learning experience. One of Python's greatest strengths is its extensive "
        "standard library, which provides modules and functions for a wide variety of tasks, including "
        "file I/O, system calls, and even web development. This rich library allows developers to "
        "accomplish complex tasks with minimal effort, as they can leverage pre-built modules rather than "
        "writing code from scratch. Furthermore, Python's package management system, pip, makes it easy to "
        "install and manage third-party libraries, expanding the language's capabilities even further. "
        "Python's versatility is evident in its wide range of applications. In web development, frameworks "
        "like Django and Flask enable developers to build robust and scalable web applications quickly. "
        "These frameworks provide tools and libraries for handling common web development tasks, such as "
        "database interactions, user authentication, and URL routing, allowing developers to focus on "
        "building unique features for their applications."
    )
    show_progress(
        "Translation in progress...",
        None,
        0.25,
        translate_text,
        chinese_text,
        src='en',
        dest='zh-cn'
    )
