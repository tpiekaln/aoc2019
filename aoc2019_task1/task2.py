import sys
import os

def calculate_fuel(mass):
    fuel = int(mass) // 3 - 2
    if(fuel > 0):
        return fuel + calculate_fuel(fuel)
    return 0

def main():
    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()
    result = 0
    with open(filepath) as fp:
       cnt = 0
       for mass in fp:
           fuel = calculate_fuel(mass)
           print(" FINAL : mass {} -> fuel {} ".format(mass, fuel))
           result += fuel
    print ("result {}".format(result))

if __name__ == '__main__':
   main()