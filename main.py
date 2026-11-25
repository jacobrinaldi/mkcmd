#!/usr/bin/env python3

from fileinput import filename
import os
import time as t



print("this program will ask for sudo access this is to move it into usr/local/bin")
print("to make sure this works add usr/local/bin to your paths")
print("if your on a none intel based mac you may have to run:")
print("sudo mkdir -p usr/local/bin")
print("this program will run in 5 seconds")
t.sleep(5)
fileName = input("name WITHOUT file extension ")
lang = input("What langue did you code your program in? ")
dir = input("What is the path do you project ")
commandName = input("What do you want to name your command ")
installSH = input("Do you want an install.sh file along with your command")

email = "jacob.a.rinaldi@gmail.com"


#valid langues
validLang = [
    "python",
    "javascript",
    "bash",
    "ruby",
    "lua",
]

#python function

def python():
    print("MAKE SURE YOUR PROGRAM HAS THE SHEBANG LINE OF #!/usr/bin/env python3")
    t.sleep(2)
    os.chdir(dir)
    os.system(f"mv {fileName}.py {commandName}")
    os.system(f"chmod +x {commandName}")
    os.system(f"sudo mv {commandName} /usr/local/bin")
    os.chdir(dir)
    os.system(f'sudo cp "{fileName}.py" "/usr/local/bin/{commandName}"')
    os.system(f'sudo chmod +x "/usr/local/bin/{commandName}"')

#javascript function

def javascript():
    print("MAKE SURE YOUR PROGRAM HAS THE SHEBANG LINE OF #!/usr/bin/env node")
    t.sleep(2)
    os.chdir(dir)
    os.system(f"mv {fileName}.js {commandName}")
    os.system(f"chmod +x {commandName}")
    os.system(f"sudo mv {commandName} /usr/local/bin")
    os.chdir(dir)
    os.system(f'sudo cp "{fileName}.js" "/usr/local/bin/{commandName}"')
    os.system(f'sudo chmod +x "/usr/local/bin/{commandName}"')


#bash function

def bash():
    print("MAKE SURE YOUR PROGRAM HAS THE SHEBANG LINE OF #!/usr/bin/env bash")
    t.sleep(2)
    os.chdir(dir)
    os.system(f"mv {fileName}.sh {commandName}")
    os.system(f"chmod +x {commandName}")
    os.system(f"sudo mv {commandName} /usr/local/bin")
    os.chdir(dir)
    os.system(f'sudo cp "{fileName}.sh" "/usr/local/bin/{commandName}"')
    os.system(f'sudo chmod +x "/usr/local/bin/{commandName}"')


#ruby function

def ruby():
    print("MAKE SURE YOUR PROGRAM HAS THE SHEBANG LINE OF #!/usr/bin/env ruby")
    t.sleep(2)
    os.chdir(dir)
    os.system(f"mv {fileName}.rb {commandName}")
    os.system(f"chmod +x {commandName}")
    os.system(f"sudo mv {commandName} /usr/local/bin")
    os.chdir(dir)
    os.system(f'sudo cp "{fileName}.rb" "/usr/local/bin/{commandName}"')
    os.system(f'sudo chmod +x "/usr/local/bin/{commandName}"')


#lua function

def lua():
    print("MAKE SURE YOUR PROGRAM HAS THE SHEBANG LINE OF #!/usr/bin/env lua")
    t.sleep(2)
    os.chdir(dir)
    os.system(f"mv {fileName}.lua {commandName}")
    os.system(f"chmod +x {commandName}")
    os.system(f"sudo mv {commandName} /usr/local/bin")
    os.chdir(dir)
    os.system(f'sudo cp "{fileName}.lua" "/usr/local/bin/{commandName}"')
    os.system(f'sudo chmod +x "/usr/local/bin/{commandName}"')


#main function

def main():
    #checks if langue is valid
    if lang.lower() in validLang:
        if lang.lower() == "python":
            python()
    elif lang.lower()== "javascript":
        javascript()
    elif lang.lower() == "bash":
        bash()
    elif lang.lower() == "ruby":
        ruby()
    elif lang.lower() == "lua":
        lua()
    else:
        print(f"langue not supported... If you would like to add it please email me at {email}")


main()
