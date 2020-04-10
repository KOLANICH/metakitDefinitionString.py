import sys

if __name__ == "__main__":
	from pprint import pprint

	from . import parse

	for el in sys.argv[1:]:
		pprint(parse(el))
