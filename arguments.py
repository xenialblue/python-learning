import argparse

parser = argparse.ArgumentParser(
    description="This Program is printing the name of my dogs"
)
parser.add_argument("-c", "--color", metavar="color", required=True, help="the color to search for", choices={"red", "green"})

args = parser.parse_args()
print(args.color)