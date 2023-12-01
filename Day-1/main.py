import argparse
parser = argparse.ArgumentParser("Day-1")
parser.add_argument("input", help="The file to be processed", type=str)
args = parser.parse_args()


def decode(line):
    numbers = [char for char in line if char.isdigit()]
    return numbers[0] + numbers[-1]

with open(args.input, "r") as inputfile:
    tot = 0
    for line in inputfile:
        tot += int(decode(line))
    print(tot)
