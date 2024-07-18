from api import *
from fileRead import *
from commands import *

filename = 'pythonNextbike/login.txt'

def main():
    apiKey = getApiKey()
    print("Got API Key: " + apiKey)
    mobile, pin = readLoginData(filename)
    loginKey = getLoginKey(apiKey, mobile, pin)
    print("Login successful. You are logged in with +" + mobile)
    print("The Login Key is: " + loginKey)

    # Define the command dictionary
    commands = {
        'find-near-station': lambda *args: find_nearest_station(apiKey, loginKey, *args),
        'exit': exit_program
    }

    while True:
        input_line = input('> ')
        command_parts = input_line.split(' ')
        command = command_parts[0]
        args = command_parts[1:]
        
        if command in commands:
            try:
                commands[command](*args)
            except Exception as e:
                print(f"Error executing command: {e}")
        else:
            print(f"Unknown command: {command}")


if __name__ == '__main__':
    main()