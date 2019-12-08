import sys
import os

def main():
    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()
    result = 0
    with open(filepath) as fp:
       cnt = 0

       for mass in fp:
           fuel = int(mass) // 3 - 2
           print("mass {} -> fuel {} ".format(mass, fuel))
           result += fuel
    print ("result {}".format(result))
if __name__ == '__main__':
   main()