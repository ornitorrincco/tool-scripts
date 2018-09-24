import subprocess

def logForCommands(commands = ['ipconfig'], filename = 'datos.txt'):
    with open(filename, 'wb') as file:
        subprocess.run(commands, stdout = file, shell = True)

def main():
    logForCommands()

if __name__ == "__main__":
    print('Main')
    main()
else:
    print('Library')
