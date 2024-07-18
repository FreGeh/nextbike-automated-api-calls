def readLoginData(filename):
    with open(filename, 'r') as file:
        line = file.readline()
        mobile, pin = line.split(',')
        return mobile.strip(), pin.strip()