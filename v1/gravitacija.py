import sys

C = 6.674*(10**-11)
M = 5.972*(10**24)
r = 6.371*(10**6)


def main():
    if (len(sys.argv) > 2):
        print("Too many arguments.")
        sys.exit()
    if(len(sys.argv) == 1):
        print("Please add argument 'height'.")
        sys.exit()
    
    height = float(sys.argv[1])
    print("OIS je zakon!")

    print_data(height)


def gravitational_accelaration(height):
    return (C*M)/((r+height)**2)

def print_data(height):
    print("Height is", height)

    print("Gravitational accelaration is", gravitational_accelaration(height))

if __name__ == "__main__":
    main()
