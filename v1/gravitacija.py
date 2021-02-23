
import sys

C = 6.674*(10**-11)
M = 5.972*(10**24)
r = 6.371*(10**6)

visina = 0

def main():
    if (len(sys.argv) > 2):
        print("Too many arguments.")
        sys.exit()
    if(len(sys.argv) == 1):
        print("Please add argument 'nadmorska visina'.")
        sys.exit()
    
    visina = sys.argv[1]
    print("OIS je zakon!")


def grav_posp():
    return (C*M)/((r+visina)**2)


if __name__ == "__main__":
    main()
