import sys

from ArgParser import ArgParser
from Minimizer import Minimizer

parser = ArgParser(sys.argv)

sequence_length = int(input("Sequence length: "))

if sequence_length <= 0:
    print("Sequence length has to be a positive integer!")
    sys.exit(-1)

sequence = []

for i in range(sequence_length):
    sequence.append(str(input()))

minimizer = Minimizer(sequence, parser)
minimizer.run()