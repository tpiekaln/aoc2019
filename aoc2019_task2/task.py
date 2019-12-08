import sys
import os

END = 99
ADD = 1
MUL = 2

ADD_NEXT = 4
MUL_NEXT = 4
EXPECTED_RESULT = 19690720

def handle_opt_code(opcode, arg1 = None, arg2 = None):
    if opcode == ADD :
        return arg1 + arg2, ADD_NEXT
    elif opcode == MUL :
        return arg1 * arg2, MUL_NEXT
    else:
        print("unknown opcode {}".format(opcode))
        sys.exit()


def main():
    filepath = sys.argv[1]

    str_memmap = None
    with open(filepath) as fp:
       for data in fp:
           str_memmap = data.split(',')
    memmap = [int(i) for i in str_memmap]

    print ("input data {}".format(memmap))
    original_program = memmap.copy();

    for noun in range(0, 99) :
        for verb in range (0, 99):

            # this is initial space rocket program...
            memmap[1] = noun
            memmap[2] = verb
            initial_pos = 0
            while True:
                opcode = memmap[initial_pos]
                if opcode == END :
                    break

                arg1 = memmap[memmap[initial_pos + 1]]
                arg2 = memmap[memmap[initial_pos + 2]]
                dst = memmap[initial_pos + 3]

                rv, next = handle_opt_code(opcode, arg1, arg2)
                memmap[dst] = rv
                initial_pos += next

            print ("result {}".format(memmap))
            if(memmap[0] == EXPECTED_RESULT):
                sys.exit()
            memmap = original_program.copy();
            initial_pos = 0

if __name__ == '__main__':
   main()