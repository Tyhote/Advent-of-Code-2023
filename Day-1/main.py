import argparse
import re
parser = argparse.ArgumentParser("Day-1")
parser.add_argument("input", help="The file to be processed", type=str)

args = parser.parse_args()
expression = re.compile(r'(?:(?:one|two|three|four|five|six|seven|eight)(?:teen)?|nine|ten|twenty|\d)')

def decode(line):
    return expression.findall(line)

with open(args.input, "r") as inputfile:
    tot = 0
    for line in inputfile:
        numbers = decode(line)
        tot += number for number in numbers
    print(tot)
