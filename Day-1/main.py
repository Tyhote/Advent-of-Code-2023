import argparse
import re
from enum import Enum
parser = argparse.ArgumentParser("Day-1")
parser.add_argument("input", help="The file to be processed", type=str)

args = parser.parse_args()
# This finds all numbers up to twenty.
expression = re.compile(r'one|two|three|four|five|six|seven|eight|nine|\d')

def word_to_number(string):
    class NumberWord(Enum):
        ONE = "1"
        TWO = "2"
        THREE = "3"
        FOUR = "4"
        FIVE = "5"
        SIX = "6"
        SEVEN = "7"
        EIGHT = "8"
        NINE = "9"
        TEN = "10"
        ELEVEN = "11"
        TWELVE = "12"
        THIRTEEN = "13"
        FOURTEEN = "14"
        FIFTEEN = "15"
        SIXTEEN = "16"
        SEVENTEEN = "17"
        EIGHTEEN = "18"
        NINETEEN = "19"
        TWENTY = "20"
    return NumberWord[(string.upper())].value


def decode(line):
    numbers = expression.findall(line)
    #Making sure we have at least two numbers
    # and then reducing to just the first and last
    print(numbers)
    if len(numbers) > 1:
        numbers = [numbers[0], numbers[-1]]
    else:
        numbers = [numbers[0]]
    #Convert all to numeric
    for number in numbers:
        if not number.isnumeric():
            numbers[numbers.index(number)] = word_to_number(number)
    return numbers

with open(args.input, "r") as inputfile:
    tot = 0
    for line in inputfile:
        print("Total: " + str(tot))
        print(line)
        numbers = decode(line)
        if len(numbers) > 1:
            tot += int( numbers[0]+numbers[1] )
            print(int(numbers[0]+numbers[1]))
        else:
            tot += int(numbers[0])
            print(int(numbers[0]))
        print(numbers)
    print(tot)
