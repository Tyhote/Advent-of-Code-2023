import argparse
import re
parser = argparse.ArgumentParser("Day-1")
parser.add_argument("input", help="The file to be processed", type=str)

args = parser.parse_args()
# This finds all numbers up to twenty.
expression = re.compile(r'(?:(?:four|six|seven|nine)(?:teen)?|one|two|three|five|ten|eleven|twelve|thirteen|fifteen|eighteen|eight|twenty|\d)')

def word_to_number(string):
    


def decode(line):
    numbers = expression.findall(line)
    if len(numbers) > 1:
        numbers = [numbers[0], numbers[-1]]
    else:
        numbers = [numbers[0]]


with open(args.input, "r") as inputfile:
    tot = 0
    for line in inputfile:
        numbers = decode(line)
        tot += number for number in numbers
    print(tot)
