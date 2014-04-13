import argparse

parser = argparse.ArgumentParser(description="Chemistry-cc argparser")

# Actual arguments for argparser
parser.add_argument("-t", dest="chtest", required=False,
                    help="Use it if you want to run tests of chemistry-cc",
                    default=i)

args = parser.parse_args()
