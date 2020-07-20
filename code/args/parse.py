import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search some files')
    # positional arguments, which cares about the position without any '-'
    # nargs specifies the number of command-line arguments that should be consumed.
    parser.add_argument(dest='filenames', metavar='filename', nargs='*')
    # optional arguments
    # append action stores a list
    parser.add_argument('-p', '--pat', metavar='pattern', required=True,
                        dest='patterns', action='append',
                        help='text pattern to search for')
    parser.add_argument('-v', dest='verbose', action='store_true',
                        help='verbose mode')
    # store is the default action
    parser.add_argument('-o', dest='outfile', action='store',
                        help='output file')
    parser.add_argument('--speed', dest='speed', action='store',
                        choices={'slow', 'fast'}, default='slow',
                        help='search speed')

    args = parser.parse_args()

    # Output the collected arguments
    print(args.filenames)
    print(args.patterns)
    print(args.verbose)
    print(args.outfile)
    print(args.speed)
