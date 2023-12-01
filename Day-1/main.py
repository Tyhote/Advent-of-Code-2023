import argparse
import re
parser = argparse.ArgumentParser("Day-1")
parser.add_argument("input", help="The file to be processed", type=str)

args = parser.parse_args()
# This finds all numbers up to twenty.
expression = re.compile(r'(?:(?:four|six|seven|nine)(?:teen)?|one|two|three|five|ten|eleven|twelve|thirteen|fifteen|eighteen|eight|twenty|\d)')

def decode(line):
    return expression.findall(line)

with open(args.input, "r") as inputfile:
    tot = 0
    for line in inputfile:
        numbers = decode(line)
        tot += number for number in numbers
    print(tot)
