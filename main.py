#!/usr/bin/env python3

import os
import shutil
import time as t


print("this program will ask for sudo access this is to move it into usr/local/bin")
print("to make sure this works add usr/local/bin to your paths")
print("if you're on a non-intel based mac you may have to run:")
print("sudo mkdir -p /usr/local/bin")
print("this program will run in 5 seconds")

t.sleep(5)

fileName = input("name WITHOUT file extension ")
lang = input("What language did you code your program in? ").lower()
dir = input("What is the path to your project? ")
commandName = input("What do you want to name your command ")

email = "jacob.a.rinaldi@gmail.com"

validLang = [
    "python",
    "javascript",
    "bash",
    "ruby",
    "lua",
    "php",
    "perl",
    "applescript",
]


def install(extension, interpreter_message):
    """Copy the source file to /usr/local/bin and restore the original directory."""
    original_dir = os.getcwd()
    project_dir = os.path.abspath(os.path.expanduser(dir))

    print(interpreter_message)
    t.sleep(2)

    source = os.path.join(project_dir, f"{fileName}{extension}")
    destination = os.path.join("/usr/local/bin", commandName)

    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file not found: {source}")

    try:
        os.chdir(project_dir)
        shutil.copy2(source, destination)
        os.chmod(destination, 0o755)
    finally:
        os.chdir(original_dir)


def python():
    install(".py", "MAKE SURE YOUR PROGRAM HAS THE SHEBANG LINE OF #!/usr/bin/env python3")


def javascript():
    install(".js", "MAKE SURE YOUR PROGRAM HAS THE SHEBANG LINE OF #!/usr/bin/env node")


def bash():
    install(".sh", "MAKE SURE YOUR PROGRAM HAS THE SHEBANG LINE OF #!/usr/bin/env bash")


def ruby():
    install(".rb", "MAKE SURE YOUR PROGRAM HAS THE SHEBANG LINE OF #!/usr/bin/env ruby")


def lua():
    install(".lua", "MAKE SURE YOUR PROGRAM HAS THE SHEBANG LINE OF #!/usr/bin/env lua")


def php():
    install(".php", "MAKE SURE YOUR PROGRAM HAS THE SHEBANG LINE OF #!/usr/bin/env php")


def perl():
    install(".pl", "MAKE SURE YOUR PROGRAM HAS THE SHEBANG LINE OF #!/usr/bin/env perl")


def applescript():
    print("MAKE SURE YOUR CODE IS .applescript")
    install(".applescript", "MAKE SURE YOUR PROGRAM HAS THE SHEBANG LINE OF #!/usr/bin/env osascript")


def main():
    if lang not in validLang:
        print(f"Unsupported language: {lang}")
        return

    functions = {
        "python": python,
        "javascript": javascript,
        "bash": bash,
        "ruby": ruby,
        "lua": lua,
        "php": php,
        "perl": perl,
        "applescript": applescript,
    }

    functions[lang]()


if __name__ == "__main":
    main()
