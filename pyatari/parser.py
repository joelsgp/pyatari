from sys import argv

import grammar


def main():
    filename = argv[1]
    tokens = grammar.LISTING.parse_file(filename, parse_all=True)
    print(tokens)


if __name__ == "__main__":
    main()
